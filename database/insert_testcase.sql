USE library;
-- 插入book表数据
INSERT INTO book (bid, cover, bname, author, publisher, status) VALUES
(1, 'cover1.jpg', '西游记', '吴承恩', '人民文学出版社', 0),
(2, 'cover2.jpg', '红楼梦', '曹雪芹', '人民文学出版社', 1),
(3, 'cover3.jpg', '三国演义', '罗贯中', '人民文学出版社', 2),
(4, 'cover4.jpg', '水浒传', '施耐庵', '人民文学出版社', 0),
(5, 'cover5.jpg', '资治通鉴', '司马光', '中华书局', 0);

-- 插入student表数据
INSERT INTO student (sid, sname, major, tel) VALUES
(1, '张三', '计算机科学与技术', '13812345678'),
(2, '李四', '软件工程', '13898765432'),
(3, '王五', '网络工程', '13812345679'),
(4, '赵六', '计算机科学与技术', '13898765433'),
(5, '钱七', '软件工程', '13812345670');

-- 插入admin表数据
INSERT INTO admin (aid, aname, tel) VALUES
(1, '老王', '13912345678'),
(2, '老李', '13998765432');

-- 插入reserve表数据
INSERT INTO reserve (sid, bid, reserve_date, take_date) VALUES
(1, 2, '2023-05-01', '2023-05-15'),
(3, 3, '2023-05-03', '2023-05-20');

-- 插入borrow表数据
INSERT INTO borrow (sid, bid, borrow_date, due_date, return_date) VALUES
(2, 3, '2023-04-15', '2023-05-15', NULL),
(4, 1, '2023-05-01', '2023-06-01', NULL);

-- 插入user表数据
INSERT INTO user (username, password, uid, role) VALUES
('student1', 'pass1', 1, 0),
('student2', 'pass2', 2, 0),
('admin1', 'admin1', 1, 1),
('admin2', 'admin2', 2, 1);