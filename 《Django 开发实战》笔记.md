

## 指导思想：1、精通一个，不要摊大饼，杂而不精是一直以来的问题。聚焦一切力量，攻击一个‘城墙口’。；2、勤奋  
原理：还是项目少，项目简单，工作还是很多的，如果能展示出自己有能力，那就是可以的；90 天 1500 个小时，可以做 12 个大项目了，肯定能找到工作  
做法：多做项目，增加已有项目的功能；深化对 Django 的理解，《Django》开发实战，听 10 遍；  


再听完一遍就可以写：读过部分 Django 源码，了解 Django ORM、视图、模板、表单、路由、中间件的运行原理  

多查

读目录 20 遍，熟悉了目录，看到这个知识点，才会想到来查：
2021.03.03：1 遍   
2021.03.04：1 遍   


### 第1章 初识Django框架  


User.objects.all()  
User.objects.filter(name__contains='a')  
User.objects.create(name='b', password='c')  


### 第2章 Django开发环境配置  

创建虚拟环境  
pip install virtualenv  

virtualenv django_env(先 cd 到文件夹下面，比如 cd /home；这个命令会创建文件夹；可以指定 python 版本)  
source django_env/bin/activate  
deactivate  



### 第3章 Django项目框架搭建  

django-admin startproject my_bbs  

可以通过 python manage.py shell 进入项目环境  


### 第4章 Django ORM 应用与原理剖析  

ForeignKey，多对一  

class Comment:  
&emsp; topic = models.ForeignKey(Topic, on_delete=True)  


创建好 model 以后，要迁移到数据库中  

python manage.py makemigrations 应用名称，比如 python manage.py makemigrations post  
执行完以后，可以执行 python manage.py sqlmigrate post 0001 查看 sql 命令，sqlmigrate 不会迁移到数据库  
可以用 python manage.py check 检查正确性，不会影响数据库；如果直接执行 migrate，遇到错误可能要删除 database 重新做，如果有数据，可能就会对已有数据产生影响    
check 没有问题以后，可以执行迁移操作，python manage.py migrate  

Django 数据表名称的默认命名规则是：应用名_小写类名  

objects 是 Manager 类的实例，被称为查询管理器，是数据库查询的入口  

如果没有 \_\_str__ 方法，返回的是内存地址  


4.2 有 Meta、Field、model、关系类型 参数的详细说明  

多对多的时候，可以使用 sqlmigrate 查看中间表的创建过程  








