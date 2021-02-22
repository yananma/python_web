#### 1、创建项目 创建应用  
cd desktop  

mkdir elearning  

cd elearning  

conda env list  

activate django  

django-admin startproject xxkt  

python manage.py startapp myapp  

配置数据库  

在 xxkt 应用的 settings.py 里有数据库配置的文档  

删除数据库：DROP DATABASE xxkt_db;  

创建数据库：CREATE DATABASE xxkt_db;  

python manage.py makemigrations  

python manage.py migrate  

USE xxkt_db;  

SHOW tables;  

创建超级用户  
python manage.py createsuperuser  
admin  
admin@qq.com  
password1234  
password1234  

python manage.py runserver  

xxkt settings.py 最下面 LANGUAGE_CODE = 'zh-hans'; TIME_ZONE = 'Asia/Shanghai'  


#### 2、创建课程相关模型  

myapp 的 models.py 添加 Banner 类  

在 xxkt 的 settings.py 中的 INSTALLED_APPS 列表中添加 myapp 才能生成数据表  

python manage.py makemigrations 生成 banner 中间表  

然后执行 python manage.py migrate 根据中间表生成数据库中的一张 table  

后面大部分都是这样一个流程  


#### 3、创建课程相关模型  



#### 4、重写用户模型  
DROP DATABASE xxkt_db;  

create database xxkt_db;  

这里一定要注意，在 makemigrations 的时候，后面一定要加上 myapp，否则一直报错  


#### 5、创建博客相关模型  



#### 6、

