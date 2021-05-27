
激活环境：`activate django_rest`  
退出环境：`deactivate`  
查看已有环境 `conda env list`
#### 1、创建项目 创建应用  
`cd desktop`  
`mkdir elearning`  
`cd elearning`  
`conda env list`  
`activate django`  
`django-admin startproject xxkt`  
`python manage.py startapp myapp`  

配置数据库  

在 xxkt 应用的 settings.py 里有数据库配置的文档  

删除数据库：`drop database xxkt_db;`  

创建数据库：`create database xxkt_db;`  

`python manage.py makemigrations`  
`python manage.py migrate`  
`USE xxkt_db;`  
`SHOW tables;`  

创建超级用户  
`python manage.py createsuperuser`  
admin  
admin@qq.com  
password1234  
password1234  

`python manage.py runserver`  


#### 2、创建课程相关模型  

myapp 的 models.py 添加 Banner 类  

在 xxkt 的 settings.py 中的 INSTALLED_APPS 列表中添加 myapp 才能生成数据表  

python manage.py makemigrations 生成 banner 中间表  

然后执行 python manage.py migrate 根据中间表生成数据库中的一张 table  

后面大部分都是这样一个流程  



LANGUAGE_CODE = 'zh-hans';  
TIME_ZONE = 'Asia/Shanghai'  
admin.site.site_header = '在线教育平台后台管理系统'  



多写注释  
改一改，看变化，比如 models.py 中的 verbose_name 的作用  
在报错位置使用 pysnooper  
用 python manage.py -h 查看命令  
print(Banner.objects.all().query) 看 sql 命令  
可以在 views 中使用 pysnooper  
可以看别人的网站的源码  

