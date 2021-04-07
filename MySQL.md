
select 跟的是一句话最后的部分，统计个数一律用 count(\*)  
from 表名是永远不变的  
where 永远在 from 后面，where 修饰的是 select 后面的内容，有条件运算符 > < = 还有模糊查询的首先就想到 where  
group by 关注的是每个后面的内容  
order by 关注的是从按到排序之间的内容，order by 一般放在最后    



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

数据放在表中，表放在库中；就像一个大库房里，像是晒床单一样，挂着一张张表格；use 数据库名，就是进入了库房，可以查询库房里的所有表的数据  

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

select 跟的是一句话最后的部分  

where 无论在什么情况下都要放在 from 之后  

这里的 where 和 if 是一样的，作用就是筛选，结果是 true 或 false  

执行顺序是先执行 from 表名，然后是 where 条件，最后是 select 查询列表  

分类：  
* 按条件表达式筛选，条件运算符：`> < = <>(不等于) >= <=`  
* 按逻辑表达式筛选，逻辑运算符：`and(&&) or(||) not(!)`  
* 模糊查询，like、between and、in、is null  

条件表达式  

1. 筛选出工资大于 12000 的员工信息  
`select * from employees where salary>12000;`  

2. 查询部门编号不等于 90 的员工名和部门编号  
`select last_name, department_id from employees where department_id<>90;`  

逻辑表达式，逻辑表达式的作用就是条件比较多的时候连接条件表达式    

3. 查询工资在 10000 到 20000 之间的员工名字、工资和奖金  
`select last_name, commission_pct, salary from employees where salary >= 10000 and salary <= 20000 ;`  

4. 查询部门编号不在 90 到 110 之间的，或者工资大于 15000 的员工信息  
`select * from employees where department_id<90 or department>110 or salary>15000;`  

模糊查询  

5. 查询员工名中包含字符 a 的员工信息  
like，经常和转义字符结合使用，转义字符 % 表示任意多字符，包含 0 个，_ 表示任意单个字符   
`select * from employees where last_name like '%a%';`  

6. 查询员工名中第 3 个字母为 n 第 5 个字符为 l 的员工名和工资  
`select last_name, salary from employees where last_name like '__n_l%';`  
如果是查名字中包含下划线的，就要用转义字符  

7. 查询员工编号在 100 到 120 之间的员工信息  
between and 更简洁，包含临界值;   
`select * from employees where employee_id between 100 and 120;`  

8. 查询员工的工种编号是 IT_PROG 或 AD_VP 的员工名和工种编号  
in 用来判断某字段是否属于 in 列表中的某一项，更简洁，列表中的类型必须统一，不支持通配符   
`select last_name, job_id from employees where job_id in ('IT_PROG', 'AD_VP')`  

9. 查询没有奖金的员工名和奖金率  
is null 条件运算符=不能判断 null，要判断 null 只能用 is 或 is not   
`select last_name, commission_pct from employees where commission_pac is null;`  


### 3、排序查询

    select 查询列表 from 表名 where 筛选条件 order by 排序列表 asc | desc  

order by 关注的是从按到排序之间的内容  

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
`select * from employees order by salary asc, employee_id desc;`  

### 4、常见函数

将一组逻辑封装在方法体中，对外显示方法名; 好处：1 隐藏函数实现细节，简洁 2 提高代码复用性  

    select 函数名(实参列表) from 表;
    
要关注的就是两点：①叫什么(函数名) ②干什么(函数功能)  

分类：  
* 单行函数，比如 concat、length、ifnull，输入一个值，返回一个值  
* 分组函数，也叫统计函数、聚合函数、组函数，主要功能是做统计使用，输入一组值，返回一个值  

#### 4.1 单行函数  

##### 4.1.1 字符函数  

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
`select replace('僧推月下门', '推', '敲') as output;`  

7. trim 去除前后空格  

8. lpad 左填充，rpad 右填充  


##### 4.1.2 数字函数  
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
* datediff 返回两个日期相差的天数  


##### 4.1.3 流程控制函数  
* if 函数控制流程 `select last_name, commission_pct, if(commission_pct is null, '没奖金 呵呵', '有奖金') as 备注 from employees;`  
* case 语句  

        case 变量、表达式或字段 
        when 常量1 then 值1 
        when 常量2 then 值2  
        when 常量3 then 值3  
        else 默认值  
        end

        select salary,  
        case
        when salary>20000 then 'A' 
        when salary>15000 then 'B' 
        when salary>10000 then 'C'
        else 'D' 
        end as 工资级别 
        from employees;  

##### 4.1.4 其他函数  
`select version();`  
`select database();`  
`select user();`  

#### 4.2 聚合函数

sum 求和、avg  平均值、max 最大值、min 最小值、count 计算个数  

`select sum(salary) as 和, round(avg(salary), 2) as 平均值, max(salary) as 最大值, min(salary) as 最小值, count(salary) as 个数 from employees;`  

都会忽略 null，可以结合其他函数使用  

`select count(*) from employees;` 统计行数  

查询员工入职的最大入职时间和最小入职时间相差的天数  
`select datediff(max(hiredate), min(hiredate)) difference from employees;`  

查询部门编号为 90 的员工个数  
`select count(*) as 个数 from employees where department_id=90;`  


### 5、分组函数  

    select 列, 分组函数(列) from 表名 where 分组前的筛选条件 group by 分组表达式 having 分组后的筛选条件 order by 排序列表 asc | desc  

group by 关注的是每个后面的内容  

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

#### 6.1 sql92 语法(默认用 sql99)  

又称多表查询，当查询的字段来自多张表时，就要用到连接查询  

笛卡尔乘积现象：表 1 有 m 行，表 2 有 n 行，结果为 m * n 行，因为没有有效的连接条件，导致多张表完全连接  

解决办法：添加有效的连接条件，找两张表中意义相同的条件  

##### 6.1.1 等值连接  

    select 查询列表 from 表1 as 别名1, 表2 as 别名2 where 表1.key=表2.key and 筛选条件 group by 分组字段 having 分组后的筛选 order by 排序字段  

使用表中交集部分作为连接条件，两张表都有的字段  

1. 查询员工名和对应的部门名  
`select last_name, department_name from employees, departments where employees.department_id = departments.department_id;`  

2. 查询员工名、工种号、工种名  
表名较长，联合查询一般都要起别名，一个是简洁，一个是区分多个重名字段; 起了别名就不能再用原来的表名限定，因为先执行 from 后面，执行完以后就已经变成了别名    
`select e.last_name, e.job_id, j.job_title from employees as e, jobs as j where e.job_id=j.job_id;`  

加筛选条件用 and，因为 where 已经被占用了  
3. 查询有奖金的员工名、部门名、奖金  
`select last_name, department_name, commission_pct from employees as e, departments as d where e.department_id = d.department_id and e.commission_pct is not null;`  

4. 查询城市名中第二个字母为 o 的部门名和城市名  
`select department_name, city from departments as d, locations as l where d.location_id = l.location_id and city like '_o%';`  

添加分组  
5. 查询每个城市的部门个数  
`select count(*) as 个数, city from departments as d, locations as l where d.location_id = l.location_id group by city;`  

添加排序  
6. 查询每个工种的工种名和员工个数，并且按员工个数降序排列  
`select job_title, count(*) from employees as e, jobs as j where e.job_id = j.job_id group by job_title order by count(*) desc;`  

三张表连接  
7. 查询员工名、部门名和所在的城市中以 s 开头的城市，并且按部门名字母排序  
`select last_name, department_name, city from employees as e, departments as d, locations as l where e.department_id = d.department_id and d.location_id = l.location_id and city like 's%' order by department_name asc;`   


##### 6.1.2 非等值连接  

    select 查询列表 from 表1 as 别名1, 表2 as 别名2 where 非等值连接条件 and 筛选条件 group by 分组字段 having 分组后的筛选 order by 排序字段  

先创建工资等级表，复制执行下面代码  

        CREATE TABLE job_grades 
        (grade_level VARCHAR(3), 
        lowest_sal INT, 
        highest_sal INT); 

        INSERT INTO job_grades 
        VALUES('A', 1000, 2999); 

        INSERT INTO job_grades 
        VALUES('B', 3000, 5999); 

        INSERT INTO job_grades 
        VALUES('C', 6000, 9999); 

        INSERT INTO job_grades 
        VALUES('D', 10000, 14999); 

        INSERT INTO job_grades 
        VALUES('E', 15000, 24999); 

        INSERT INTO job_grades 
        VALUES('F', 25000, 40000); 

1. 查询员工的工资和工资级别  
`select salary, grade_level from employees as e, job_grades as g where salary between g.lowest_sal and g.highest_sal;`  

2. 查询员工的工资和工资级别，刷选出级别等于 A 的  
``select salary, grade_level from employees as e, job_grades as g where salary between g.lowest_sal and g.highest_sal and g.`grade_level`='A';``  

##### 6.1.3 自连接  

其实就是前面的等值连接，不过等值连接是多张不同的表，自连接是连接自己  

1. 查询员工名和上级的名字  
``select e.employee_id, e.last_name, m.employee_id, m.last_name from employees as e, employees as m where e.`manager_id`=m.`employee_id`;``  


#### 6.2 sql99 语法  

sql99 支持的语法更广，而且实现了连接条件和筛选条件的分离，可读性更高  

    select 查询列表 from 表1 as 别名1 连接类型 join 表2 as 别名2 on 表1.key=表2.key where 筛选条件 group by 分组字段 having 分组后的筛选 order by 排序字段  
    
其中连接类型，内连接 inner inner 可以省略，因为用的非常多; 外连接 左外 left 右外 right; 交叉连接 cross  

* 内连接：等值连接、非等值连接、自连接  
* 外连接：左外连接、右外连接、全外连接  
* 交叉连接  

内连接是两张表的交集，左外连接是 A 全集，当然也包括 A B 的交集，右连接是 B 全集，当然也包括 A B 的交集；如果要实现 A 和 A B 交集的差集，就要加筛选条件，where B.key is null    

##### 6.2.1 内连接  

又分为等值连接、非等值连接和自连接  

###### 6.2.1.1 等值连接  
1. 查询员工名和对应的部门名  
``select last_name, department_name from employees as e inner join departments as d on e.`department_id` = d.`department_id`;``

添加筛选  
2. 查询工种名和名字中包含 e 的员工名  
``select job_title, last_name from employees as e inner join jobs as j on e.`job_id` = j.`job_id` where e.last_name like '%e%';``  

添加筛选和分组  
3. 查询部门个数 \>3 的城市名和部门个数  
``select city, count(*) as 部门个数 from departments as d inner join locations as l on d.`location_id`=l.`location_id` group by city having count(*)>3;``  

添加排序  
4. 查询员工个数 >3 的部门名和对应的员工个数，并且按员工个数降序排列  
``select count(*), department_name from employees as e inner join departments as d on e.`department_id` = d.`department_id` group by department_name having count(*)>3 order by count(*) desc;``  

多表查询  
5. 查询员工名、部门名和工种名，并且按部门名字母排序  
``select last_name, department_name, job_title from employees as e inner join departments as d on e.`department_id` = d.`department_id` inner join jobs as j on e.`job_id` = j.`job_id` order by department_name asc;``  


###### 6.2.1.2 非等值连接  

1. 查询员工的工资级别  
``select salary, grade_level from employees as e inner join job_grades as g on e.`salary` between g.`lowest_sal` and g.`highest_sal`;``  

2. 查询员工的工资级别，并统计每个级别中员工个数，按个数降序排列    
``select count(*), grade_level from employees as e inner join job_grades as g on e.`salary` between g.`lowest_sal` and g.`highest_sal` group by grade_level order by count(*) desc;``  

3. 查询员工的工资级别，并统计每个级别中员工个数，显示个数 \>20 的级别，按个数降序排列    
``select count(*), grade_level from employees as e inner join job_grades as g on e.`salary` between g.`lowest_sal` and g.`highest_sal` group by grade_level having count(*)>20 order by count(*) desc;``  

###### 6.2.1.3 自连接  

1. 查询员工名和上级的名字  
``select e.last_name, m.last_name from employees as e inner join employees as m on e.`manager_id` = m.`employee_id`;``  

2. 查询员工名和上级的名字，查询某一个上级管理的人员名单  
``select e.last_name, m.last_name from employees as e inner join employees as m on e.`manager_id` = m.`employee_id` having m.last_name='K_ing';``  

3. 查询员工名和上级的名字，并按领导管理人员个数降序排列  
``select count(*), m.last_name from employees as e inner join employees as m on e.`manager_id` = m.`employee_id` group by m.last_name order by count(*) desc;``  

##### 6.2.2 外连接  

用于查询一个表中有，而另一个表中没有的记录  

* 外连接的查询结果为主表中的所有记录，如果从表中有和主表匹配的，则显示匹配的值，如果从表中没有和它匹配的，则显示 null。外连接查询结果=内连接结果+主表中有而从表中没有的记录  
* 左外连接，left join 左边的是主表，右外连接，right join 右边的是主表  
* 

想查询哪一张表中所有的信息，哪一张表就是主表  

1. 查询男朋友不在 boys 表中的人的名字  
``select b.name, bo.* from beauty as b left outer join boys as bo on b.`boyfriend_id` = bo.`id`;`` 先运行看结果  
``select b.name, bo.* from beauty as b left outer join boys as bo on b.`boyfriend_id` = bo.`id` where bo.`id` is null;`` where 后面筛选用 id 是因为 id 是主键，主键唯一且非空    

2. 查询哪个部门没有员工  
``select d.*, e.employee_id from departments as d left outer join employees as e on d.`department_id` = e.`department_id`;`` 先运行看结果   
``select d.*, e.employee_id from departments as d left outer join employees as e on d.`department_id` = e.`department_id` where e.`employee_id` is null;``     

MySQL 不支持全外连接，全外连接=内连接结果+表1中有而表2中没有的+表2中有而表1中没有的    


##### 6.2.3 交叉连接  

交叉连接就是笛卡尔乘积  
`select b.*, bo.* from beauty as b cross join boys as bo;`  


### 7、子查询  







