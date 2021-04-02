
## MySQL 基础  

MySQL 占比第一，学就对了  

MySQL 学好学精了，就不愁找不到工作了  

其他类型也可以存储，为什么要用数据库？其他的不好查询  

数据库有一套完整的管理系统  

垃圾场里的东西是不要了的，可以随便扔，但是仓库里的东西是要再次使用的，所以一定是有组织存储的  

### 数据库的相关概念

SQL 结构化查询语言 Structured Query Language，是专门用于和数据库进行通信的一门语言  

SQL 是通用的语言，不是一个软件专有的  

SQL 简单易学  

虽然简单，但是功能强大，非常灵活  

数据库和文件柜一样，一层摞一层  


一个数据库有多张表，每张表都有自己唯一的名字来标识自己  

每张表都是由列组成的，每个列称为一个字段，和机器学习里的属性是一样的  

数据库最终还是把数据存成电脑上的文件了，只不过是可以通过数据库来管理  

### 常见命令介绍

`mysql (-h主机名 -P端口号) -u用户名 -p没有空格输密码`  

`show databases;`  
`use xxkt_db;`  
`show tables;`  

    mysql> create table stuinfo(
        -> id int,
        -> name varchar(20));
        
        create table 表名(
                列名 列类型, 
                列名 列类型, 
        );    


show tables;  
desc stuinfo; 查看表结构  

    select * from stuinfo
    insert into stuinfo (id, name) values(1, 'tom');  
    insert into stuinfo (id, name) values(2, 'kite');
    select * from stuinfo;
    update stuinfo set name='rose' where id=1;
    select * from stuinfo;
    delete from stuinfo where id=1;
    select * from stuinfo;

MySQL 语法规范  
1. 不区分大小写
2. 以 ; 结尾  
3. 命令长的时候，可以缩进或换行  

**学习内容**

查; DQL(Data Query Language) 主要就是 select   
1. 基础查询
2. 条件查询
3. 排序查询
4. 常见函数
5. 分组函数
6. 连接查询
7. 子查询
8. 分页查询
9. union 联合查询

增删改; DML(Data Manipulation Language) 
* 插入语句
* 修改语句
* 删除语句

DDL(Data Define Language) 
* 库和表的管理
* 常见数据类型介绍
* 常见约束

TCL(Transaction Control Language) 
* 事务和事务处理


### 基础查询  

select 语句使用率占了 80% 以上  

要查什么，就在 select 后面跟什么 from 表名  

查询结果是一个虚拟表格，并不是真实存在的  

查询单个字段      
`select last_name from employees;`  

查询多个字段  
`select last_name, salary, email from employees;`  

查询所有字段  
`select * from employees;`  
`*` 代表所有，就是通配符，和正则表达式里是一样的  


别名; 便于理解; 多张表联合查询的时候有重名可以区分    
`select last_name as 姓, first_name as 名 from emplyees;`  


去重; 比如部门编号，不需要重复显示  
`select distinct department_id from employees;`  






<br>

*** 

<br>


#### SQL 简介  

数据库就是行列表，每一行是一个 record 记录，每一列是一个 field 字段  


数据库是先创建 database 再创建 table，一个库里可以有多张表(一个数据库就是一个盒子，一张表就是一张纸)  

先创建数据库 create database xxkt_db;  

show databases;  

use xxkt_db;  

create table UserTbl(uid integer primary key auto_increment, name varchar(20), pwd varchar(20));  

show tables;  

insert into UserTbl(name, pwd) values('tom', '123456');  

SELECT * FROM UserTbl;  

insert into UserTbl(name, pwd) values('kite', '456789');  

update UserTbl set name='big tom' where uid=1;  

desc UserTbl;  

delete from UserTbl where uid=1;  

导入数据库 source 文件地址，反斜杠  

#### SELECT 语句  

SELECT column_name1, column_name2 FROM table_name;  
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

*** 

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


