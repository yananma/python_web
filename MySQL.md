
#### SQL 简介  

SQL 结构化查询语言 Structured Query Language  

数据库就是行列表  

每一行是一个 record 记录，每一列是一个 field 字段  

先创建数据库 create database xxkt_db;  

数据库是先有库后有表，一个库里可以有多张表(一个数据库就是一个盒子，一张表就是一张纸)  

show databases;  

再 use xxkt_db;  

再 create table UserTbl(uid integer primary key auto_increment, name varchar(20), pwd varchar(20));  

show tables;  

insert into UserTbl(name, pwd) values('tom', '123456');  

SELECT * FROM UserTbl;  

insert into UserTbl(name, pwd) values('kite', '456789');  

update UserTbl set name='big tom' where uid=1;  

desc UserTbl;  

delete from UserTbl where uid=1;  

导入数据库 source 文件地址，反斜杠  

#### SELECT 语句  

SELECT column_name, column_name FROM table_name;  
或
SELECT * FROM table_name;  

#### WHERE 语句  

就是设置查询条件  

SELECT \*(column_name) FROM Custmers WHERE Country='Mexico';  

条件可以设置 AND OR 等，设置多个条件  

#### ORDER BY GROUP BY  

ORDER BY 排序  

GROUP BY 分组  

SELECT * FROM CustomerTbl order by age ASC(DESC);  

#### SQL 增删改  

INSERT INTO table_name VALUES (value1, value2, value3...)  

删除数据库：DROP DATABASE xxkt_db;   

#### 通配符  

#### Like in between  

#### 连接查询(Joins)  

表格之间的相互关联关系  

#### 联合查询(Union)

#### 子查询  

#### 事务  


<br>  
<br>  


### 原来笔记  

数据库常用语句：  

删除数据库：DROP DATABASE xxxx;  
删除表：DROP TABLE xxxx;  

创建表：CREATE TABLE mytable (name char(20));  

插入数据：INSERT INTO mytable(name) VALUES ('马亚南');  



增：  
创建一张表  
CREATE table qsbk_tbl(qid integer primary key auto_increment, author varchar(100), text text, vote integer, comments integer);  

插入一条  
INSERT INTO myapp_person (id,name) VALUES (1, 'mayanan');  


删：  
删除一条  
DELETE FROM myapp_person WHERE id=1  

删除连续多条  
DELETE FROM myapp_person WHERE id BETWEEN 4 and 15;  

删除一张表里的全部内容  
DELETE FROM myapp_person  


查：  
查询所有记录：  
SELECT * FROM person  

相等条件查询：  
SELECT * FROM person WHERE age=20   

使用查询操作符：  
SELECT * FROM person WHERE salary in (6000, 8000)   

AND条件  
SELECT * FROM   

连接数据库  
    conn = MySQLdb.connect(  
        user = 'root',  
        passwd = '123456',  
        port = 3306,  
        db = 'spider_db',  
        host = 'localhost',  
        charset = 'utf-8',  
    )  


