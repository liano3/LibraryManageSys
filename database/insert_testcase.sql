USE library;
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

-- 插入user表数据
INSERT INTO user (username, password, uid, role) VALUES
('student1', 'pass1', 1, 0),
('student2', 'pass2', 2, 0),
('admin1', 'admin1', 1, 1),
('admin2', 'admin2', 2, 1);