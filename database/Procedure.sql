-- 存储过程设计
USE library;
-- 删除书籍
DROP PROCEDURE IF EXISTS deleteBook;
CREATE PROCEDURE IF NOT EXISTS deleteBook(IN bookId INT)
BEGIN
    START TRANSACTION;
    SET FOREIGN_KEY_CHECKS = 0;
    DELETE FROM book WHERE bid = bookId;
    DELETE FROM reserve WHERE bid = bookId;
    DELETE FROM borrow WHERE bid = bookId;
    SET FOREIGN_KEY_CHECKS = 1;
    COMMIT;
END;

-- 更新学生学号
DROP PROCEDURE IF EXISTS updateStudentId;
CREATE PROCEDURE IF NOT EXISTS updateStudentId(IN oldId INT, IN newId INT)
BEGIN
    START TRANSACTION;
    SET FOREIGN_KEY_CHECKS = 0;
    UPDATE student SET sid = newId WHERE sid = oldId;
    UPDATE borrow SET sid = newId WHERE sid = oldId;
    UPDATE reserve SET sid = newId WHERE sid = oldId;
    UPDATE user SET uid = newId WHERE uid = oldId;
    SET FOREIGN_KEY_CHECKS = 1;
    COMMIT;
END;

-- 删除学生
DROP PROCEDURE IF EXISTS deleteStudent;
CREATE PROCEDURE IF NOT EXISTS deleteStudent(IN studentId INT)
BEGIN
    START TRANSACTION;
    SET FOREIGN_KEY_CHECKS = 0;
    DELETE FROM student WHERE sid = studentId;
    DELETE FROM borrow WHERE sid = studentId;
    DELETE FROM reserve WHERE sid = studentId;
    DELETE FROM user WHERE uid = studentId;
    SET FOREIGN_KEY_CHECKS = 1;
    COMMIT;
END;

-- 创建添加学生的触发器，添加学生时自动添加对应用户
DROP TRIGGER IF EXISTS addUser;
CREATE TRIGGER IF NOT EXISTS addUser
AFTER INSERT ON student
FOR EACH ROW
BEGIN
    # 默认用户名为 0+sid，密码为 123456
    INSERT INTO user(uid, username, password, role) VALUES (NEW.sid, CONCAT('0', NEW.sid), '123456', 0);
END;

-- 创建删除学生的触发器，删除学生时自动删除对应用户
DROP TRIGGER IF EXISTS deleteUser;
CREATE TRIGGER IF NOT EXISTS deleteUser
AFTER DELETE ON student
FOR EACH ROW
BEGIN
    DELETE FROM user WHERE uid = OLD.sid and role = 0;
END;

-- 取消预约的触发器
DROP TRIGGER IF EXISTS cancelReserve;
CREATE TRIGGER IF NOT EXISTS cancelReserve
AFTER DELETE ON reserve
FOR EACH ROW
BEGIN
    UPDATE book SET status = 0 WHERE bid = OLD.bid;
END;

-- 预约过期的触发器
DROP TRIGGER IF EXISTS passReserve;
CREATE TRIGGER IF NOT EXISTS passReserve
AFTER UPDATE ON reserve
FOR EACH ROW
BEGIN
    -- 判断是否过期
    if NEW.take_date < CURDATE() THEN
        UPDATE book SET status = 0 WHERE bid = NEW.bid;
    END IF;
END;

-- 还书的触发器
DROP TRIGGER IF EXISTS returnBook;
CREATE TRIGGER IF NOT EXISTS returnBook
AFTER UPDATE ON borrow
FOR EACH ROW
BEGIN
    -- 区分续借和还书
    if NEW.return_date is not null THEN
        UPDATE book SET status = 0 WHERE bid = NEW.bid;
    END IF;
END;

-- 取消借阅的触发器
DROP TRIGGER IF EXISTS cancelBorrow;
CREATE TRIGGER IF NOT EXISTS cancelBorrow
AFTER DELETE ON borrow
FOR EACH ROW
BEGIN
    UPDATE book SET status = 0 WHERE bid = OLD.bid;
END;

-- 预约书籍的存储过程
DROP PROCEDURE IF EXISTS reserveBook;
CREATE PROCEDURE IF NOT EXISTS reserveBook(IN studentId INT, IN bookId INT, IN takeDate DATE)
label: BEGIN
    START TRANSACTION;
    -- 判断是否处于冻结状态
    IF (SELECT status FROM student, user WHERE student.sid = studentId AND student.sid = user.uid AND user.role = 0) = 1 THEN
        SIGNAL SQLSTATE '45000' SET MESSAGE_TEXT = '您的账号已被冻结，无法操作！';
        -- 回滚事务
        ROLLBACK;
        -- 结束存储过程
        LEAVE label;
    END IF;
    -- 插入预约记录
    INSERT INTO reserve(sid, bid, reserve_date, take_date) VALUES (studentId, bookId, CURDATE(), takeDate);
    -- 更新书籍状态
    UPDATE book SET status = 1 WHERE bid = bookId;
    COMMIT;
END;

-- 借阅书籍的存储过程
DROP PROCEDURE IF EXISTS borrowBook;
CREATE PROCEDURE IF NOT EXISTS borrowBook(IN studentId INT, IN bookId INT, IN dueDate DATE)
label: BEGIN
    START TRANSACTION;
    -- 判断是否处于冻结状态
    IF (SELECT status FROM student, user WHERE student.sid = studentId AND student.sid = user.uid AND user.role = 0) = 1 THEN
        SIGNAL SQLSTATE '45000' SET MESSAGE_TEXT = '您的账号已被冻结，无法操作！';
        -- 回滚事务
        ROLLBACK;
        -- 结束存储过程
        LEAVE label;
    END IF;
    -- 插入借阅记录
    INSERT INTO borrow(sid, bid, borrow_date, due_date) VALUES (studentId, bookId, CURDATE(), dueDate);
    -- 更新预约记录
    UPDATE reserve SET pass_date = CURDATE() WHERE sid = studentId AND bid = bookId AND pass_date IS NULL;
    -- 更新书籍状态
    UPDATE book SET status = 2 WHERE bid = bookId;
    COMMIT;
END;

-- Kill
DROP PROCEDURE IF EXISTS killUser;
CREATE PROCEDURE IF NOT EXISTS killUser(IN studentId INT)
label: BEGIN
    START TRANSACTION;
    -- 设置预约记录过期时间
    UPDATE reserve SET pass_date = CURDATE() WHERE sid = studentId AND take_date < CURDATE() AND pass_date IS NULL;
    -- 冻结用户
    UPDATE user SET status = 1 WHERE uid = studentId and role = 0;
    COMMIT;
END;

-- 创建函数，统计本月最热门的书籍
DROP FUNCTION IF EXISTS hotBook;
CREATE FUNCTION IF NOT EXISTS hotBook()
RETURNS INT
READS SQL DATA
BEGIN
    DECLARE hotBookId INT;
    SELECT bid INTO hotBookId FROM borrow WHERE MONTH(borrow_date) = MONTH(CURDATE()) GROUP BY bid ORDER BY COUNT(*) DESC LIMIT 1;
    RETURN hotBookId;
END;

-- 创建函数，统计本月最活跃的学生
DROP FUNCTION IF EXISTS activeStudent;
CREATE FUNCTION IF NOT EXISTS activeStudent()
RETURNS INT
READS SQL DATA
BEGIN
    DECLARE activeStudentId INT;
    SELECT sid INTO activeStudentId FROM borrow WHERE MONTH(borrow_date) = MONTH(CURDATE()) GROUP BY sid ORDER BY COUNT(*) DESC LIMIT 1;
    RETURN activeStudentId;
END;