-- 创建数据库 Library
-- DROP DATABASE IF EXISTS Library;
CREATE DATABASE IF NOT EXISTS Library;
USE Library;

-- 创建book表
CREATE TABLE IF NOT EXISTS book (
    bid INT PRIMARY KEY,
    cover LONGBLOB, -- 二进制存放图片
    bname VARCHAR(50) NOT NULL,
    author VARCHAR(50) NOT NULL,
    publisher VARCHAR(50) NOT NULL,
    status INT DEFAULT 0  -- 0表示在馆，1表示已预约，2表示已借出
);

-- 创建student表
CREATE TABLE IF NOT EXISTS student (
    sid INT PRIMARY KEY,
    sname VARCHAR(50) NOT NULL,
    major VARCHAR(50) NOT NULL,
    tel VARCHAR(50) NOT NULL
);

-- 创建admin表
CREATE TABLE IF NOT EXISTS admin (
    aid INT PRIMARY KEY,
    aname VARCHAR(50) NOT NULL,
    tel VARCHAR(50) NOT NULL
);

-- 创建reserve表
CREATE TABLE IF NOT EXISTS reserve (
    sid INT,
    bid INT,
    reserve_date DATE NOT NULL,
    take_date DATE NOT NULL,
    PRIMARY KEY (sid, bid),
    FOREIGN KEY (sid) REFERENCES student(sid),
    FOREIGN KEY (bid) REFERENCES book(bid)
);

-- 创建borrow表
DROP TABLE IF EXISTS borrow;
CREATE TABLE IF NOT EXISTS borrow (
    sid INT,
    bid INT,
    borrow_date DATE NOT NULL,
    due_date DATE NOT NULL,
    return_date DATE,
    PRIMARY KEY (sid, bid, borrow_date),
    FOREIGN KEY (sid) REFERENCES student(sid),
    FOREIGN KEY (bid) REFERENCES book(bid)
);

-- user表
CREATE TABLE IF NOT EXISTS user (
    username VARCHAR(50) PRIMARY KEY,
    password VARCHAR(50) NOT NULL,
    uid INT NOT NULL,
    role INT NOT NULL, -- 0表示学生，1表示管理员
    status INT DEFAULT 0 -- 0表示正常，1表示被冻结
);