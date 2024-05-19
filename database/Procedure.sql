-- 存储过程设计
USE library;
-- 删除书籍
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