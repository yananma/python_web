
## MySQL 基础  

MySQL 占比第一，学就对了  

MySQL 学好学精了，就不愁找不到工作了  

其他类型也可以存储，为什么要用数据库？数据库可以持久化保存(相对于列表、元组); 其他的不好查询，数据库管理非常方便  

数据库有一套完整的管理系统  

垃圾场里的东西是不要了的，可以随便扔，但是仓库里的东西是要再次使用的，所以一定是有组织存储的  

### 数据库的相关概念

SQL 结构化查询语言 Structured Query Language，是专门用于和数据库进行通信的一门语言  

SQL 是通用的语言，不是一个软件专有的  

SQL 简单易学  

虽然简单，但是功能强大，非常灵活  

数据库和文件柜一样，一层摞一层  

数据放在表中，表放在库中  

一个数据库有多张表，每张表都有自己唯一的名字来标识自己  

每张表都是由列组成的，每个列称为一个字段，就相当于 Python 类中的属性，这就是 ORM 的核心  

每一行，相当于一个对象  

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


### 1、基础查询  

    select 查询列表 from 表名  

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


去重; 比如部门编号，不需要重复显示; distinct 后面只能跟单个字段  
`select distinct department_id from employees;`  


拼接  
`select concat(last_name, ' ', first_name) as 姓名 from employees;`  


### 2、条件查询  

    select 查询列表 from 表名 where 筛选条件  
    
where 无论在什么情况下都要放在 from 之后  

这里的 where 和 if 是一样的，作用就是筛选，结果是 true 或 false  

执行顺序是先执行 from 表名，然后是 where 条件，最后是 select 查询列表  

分类：  
* 按条件表达式筛选，条件运算符：`> < = <>(不等于) >= <=`  
* 按逻辑表达式筛选，逻辑运算符：`and(&&) or(||) not(!)`  
* 模糊查询，like、between and、in、is null  

select 后面跟的，就是一句话最后的部分  

案例  
条件表达式  

1. 筛选出工资大于 12000 的员工信息  
`select * from employees where salary>12000;`  

2. 查询部门编号不等于 90 的员工名和部门编号  
`select last_name, department_id from employees where department_id<>90;`  

逻辑表达式，逻辑表达式的作用就是条件比较多的时候连接条件表达式    

3. 查询工资在 10000 到 20000 之间的员工名字、工资和奖金  
`select last_name, commission_pct, salary from employees where salary >= 10000 and salary <= 20000 ;`  

4. 查询部门编号不再 90 到 110 之间的，或者工资大于 15000 的员工信息  
`select * from employees where department_id<90 or department>110 or salary>15000;`  

模糊查询  

5. 查询员工名中包含字符 a 的员工信息; like，经常和转义字符结合使用，转义字符 % 表示任意多字符，包含 0 个，_ 表示任意单个字符   
`select * from employees where last_name like '%a%';`  

6. 查询员工名中第 3 个字母为 n 第 5 个字符为 l 的员工名和工资  
`select last_name, salary from employees where last_name like '__n_l%';`  
如果是查名字中包含下划线的，就要用转义字符  

7. 查询员工编号在 100 到 120 之间的员工信息; between and 更简洁，包含临界值; 
`select * from employees where employee_id between 100 and 120;`  

8. 查询员工的工种编号是 IT_PROG 或 AD_VP 的员工名和工种编号; in 用来判断某字段是否属于 in 列表中的某一项，更简洁，列表中的类型必须统一，不支持通配符   
`select last_name, job_id from employees where job_id in ('IT_PROG', 'AD_VP')`  

9. 查询没有奖金的员工名和奖金率; is null 条件运算符=不能判断 null，要判断 null 只能用 is 或 is not   
`select last_name, commission_pct from employees where commission_pac is null;`  


### 3、排序查询

    select 查询列表 from 表名 where 筛选条件 order by 排序列表 asc | desc  

1. 按工资从高到底排序  
`select * from employees order by salary desc;`  

2. 查询部门编号 >= 90 的员工信息，按照入职时间先后排序  
`select * from employees where department_id >= 90 order by hiredate asc;`  

3. 年薪从高到低排序(按表达式排序) commission_pct 奖金  
`select *, salary*12*(1+ifnull(commission_pct, 0)) as 年薪 from employees order by salary*12*(1+ifnull(commission_pct, 0)) desc;`  

4. 年薪从高到低排序(按别名排序)  
`select *, salary*12*(1+ifnull(commission_pct, 0)) as 年薪 from employees order by 年薪 desc;`  

5. 按 last_name 长度显示姓名和工资(按函数排序)  
`select length(last_name) as 姓名长度, last_name, salary from employees order by length(last_name) desc;`  

6. 按工资升序，再按员工编号降序(多字段排序)  
`select * from employees order by salary asc, employee desc;`  

### 4、常见函数

将一组逻辑封装在方法体中，对外显示方法名; 好处：1 隐藏函数实现细节，简洁 2 提高代码复用性  

    select 函数名(实参列表) (from 表;)
    
要关注的就是两点：①叫什么(函数名) ②干什么(函数功能)  

分类：  
* 单行函数，比如 concat、length、ifnull，输入一个值，返回一个值  
* 分组函数，也叫统计函数、聚合函数、组函数，主要功能是做统计使用，输入一组值，返回一个值  

#### 单行函数  

字符函数  

1. length 获取参数值的字节个数(utf8 英文字母占 1 个字节，汉字占 3 个字节)  
`select length('john')`  
`select length('你好john')`  
查看使用的字符编码  
`show variables like '%char%'`  

2. concat 拼接字符串  
`select concat(last_name, '_', first_name) as 姓名 from employees;`  

3. upper、lower  
`select upper('john')`  
`select lower('joHn')`  
`select concat(upper(last_name), ' ', lower(first_name)) as 姓名 from employees;`  

4. substr、substring 截取字符串; 索引从 1 开始  
截取从索引处到后面的所有字符  
`select sbustr('铁马冰河入梦来', 5) as output;`  
截取指定位置指定长度  
`select substr('铁马冰河入梦来', 1, 4) as output;`  
实现姓名首字母大写  
`select concat(upper(substr(last_name, 1,1)), lower(substr(last_name, 2)),' ', lower(first_name)) as 姓名 from employees;`  

5. instr 返回字符串第一次出现时的位置索引，如果没有则返回 0  
`select instr('铁马冰河入梦来', '冰河') as output;`  

6. replace 替换
`select replace('僧推月下门', '推', '敲') AS output;`  

7. trim 去除前后空格  

8. lpad 左填充，rpad 右填充  


数字函数  
* round 四舍五入
* ceil 向上取整
* floor 向下取整
* truncate 截断
* mod 取余

日期函数; 日期 date 就是日历，年月日; 时间 time 就是钟表，就是时分秒  
* now() 日期加时间 `select now()`  
* curdate 日期  
* curtime 时间 `select distinct(year(hiredate)) as 入职年份 from employees;`  
* str_to_date 前端网页用户输入的日期是字符串格式的  `select * from employees where hiredate = str_to_date('4-3 1992', '%m-%d %Y');`   
* date_format `select date_format(now(), '%Y年%m月%d日') as 日期`  



流程控制函数  
* if 函数控制流程 `select last_name, commission_pct, if(commission_pct is null, '没奖金 呵呵', '有奖金') as 备注 from employees;`  
* case 语句  

        select salary,  
        case
        when salary>20000 then 'A' 
        when salary>15000 then 'B' 
        when salary>10000 then 'C'
        else 'D' 
        end as 工资级别 
        from employees;  

其他函数  
`select version();`  
`select database();`  
`select user();`  

#### 分组函数

sum 求和、avg  平均值、max 最大值、min 最小值、count 计算个数  

`select sum(salary) as 和, round(avg(salary), 2) as 平均值, max(salary) as 最大值, min(salary) as 最小值, count(salary) as 个数 from employees;`  

可以结合其他函数使用  

`select count(*) from employees;` 统计行数  

查询员工入职的最大入职时间和最小入职时间相差的天数  
`select datediff(max(hiredate), min(hiredate)) difference from employees;`  

查询部门编号为 90 的员工个数  
`select count(*) as 个数 from employees where department_id=90;`  


### 5、分组函数  

    select 列, 分组函数(列) from 表名 where 筛选条件 group by 分组表达式 order by 排序列表 asc | desc  

比如要查询每个部门的平均工资  

简单查询  
1. 查询每个部门的最高工资  
`select max(salary), job_id from employees group by job_id;`  

2. 查询每个地方的部门个数  
`select count(*), location_id from departments group by location_id;`  

添加分组前的筛选条件; 筛选条件在原始表中就有，是真实存在的，放在 group by 前面，使用 where  

3. 查询邮箱中包含 a 字符的，每个部门的平均工资  
`select avg(salary), department_id from employees where email like '%a%' group by department_id;`  

4. 查询有奖金的每个领导管理的员工的最高工资  
`select max(salary), manager_id from employees where commission_pct is not null group by manager_id;`  


添加分组后的筛选条件; 筛选条件在原始表中没有，要以筛选完的结果集为表格进行筛选，放在 group by 后面，使用 having  

5. 查询哪个部门的员工数 \> 2  
`select count(*), department_id from employees group by department_id having count(*)>2;`  

6. 查询每个工种有奖金的员工的最高工资 \> 12000 的工种编号和最高工资  
`select max(salary), job_id from employees where commission_pct is not null group by job_id having max(salary)>12000;`  

7. 按姓名长度分组，查询每一组的员工个数，筛选出员工个数 \> 5 的  
`select count(*), length(last_name) from employees group by length(last_name) having count(*)>5;`  


多字段分组查询  

8. 查询每个部门每个工种的员工的平均工资  
`select avg(salary), department_id, job_id from employees group by department_id, job_id;`  

9. 查询每个部门每个工种的员工的平均工资，并按平均工资降序排列  
`select avg(salary), department_id, job_id from employees group by department_id, job_id order by avg(salary) desc;`  


### 6、连接查询  

又称多表查询，当查询的字段来自多张表时，就要用到连接查询  

笛卡尔乘积现象：表 1 有 m 行，表 2 有 n 行，结果为 m * n 行  















