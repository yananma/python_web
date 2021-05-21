
写：精通 Django，读过 Django 源码，对 Django 的 ORM、后台、视图、模板系统、表单系统、路由系统、中间件和信号机制的底层实现和运行原理有清晰的认识。  
两个项目，用到哪部分内容，就专读那一章  

目标是 200 个小时以上，用到的时候就能想起在书中的位置、相关连得内容和源码实现。源码结合 debug 弄明白  

## 指导思想：1、精通一个，不要摊大饼，杂而不精是一直以来的问题。聚焦一切力量，攻击一个‘城墙口’；2、勤奋  

建一个文件夹，记录使用 pysnooper 的结果  

Django 是立身之本，要非常精通，读源码是核心优势  

原理：还是项目少，项目简单，工作还是很多的，如果能展示出自己有能力，那就是可以的  
做法：做大项目  


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



### 第10章 Django 路由系统  



#### 10.2 路由系统工作原理  

##### 10.2.2 实现路由分发的 include 函数  

网站中创建了一个 book 应用，include(book.urls)  

    include 函数 Elapsed time: 00:00:00.402920
    include 函数 Starting var:.. arg = 'book.urls'
    include 函数 Starting var:.. namespace = None
    include 函数 06:22:07.246083 call        14 def include(arg, namespace=None):
    include 函数 06:22:07.270016 line        15     app_name = None
    include 函数 New var:....... app_name = None
    include 函数 06:22:07.274007 line        16     if isinstance(arg, tuple):
    include 函数 06:22:07.285980 line        33         urlconf_module = arg
    include 函数 New var:....... urlconf_module = 'book.urls'
    include 函数 06:22:07.289964 line        35     if isinstance(urlconf_module, str):
    include 函数 06:22:07.302929 line        36         urlconf_module = import_module(urlconf_module)
    include 函数 Modified var:.. urlconf_module = <module 'book.urls' from 'C:\\Users\\MI\\Desktop\\04\\chapter02\\first_project\\book\\urls.py'>
    include 函数 06:22:07.320881 line        37     patterns = getattr(urlconf_module, 'urlpatterns', urlconf_module)
    include 函数 New var:....... patterns = [<URLPattern '' [name='index']>, <URLPattern 'book_list/' [name='book_list']>]
    include 函数 06:22:07.323880 line        38     app_name = getattr(urlconf_module, 'app_name', app_name)
    include 函数 06:22:07.336838 line        39     if namespace and not app_name:
    include 函数 06:22:07.345814 line        46     namespace = namespace or app_name
    include 函数 06:22:07.360775 line        49     if isinstance(patterns, (list, tuple)):
    include 函数 06:22:07.375736 line        50         for url_pattern in patterns:
    include 函数 New var:....... url_pattern = <URLPattern '' [name='index']>
    include 函数 06:22:07.376731 line        51             pattern = getattr(url_pattern, 'pattern', None)
    include 函数 New var:....... pattern = <django.urls.resolvers.RoutePattern object at 0x000001EE4C2588D0>
    include 函数 06:22:07.390695 line        52             if isinstance(pattern, LocalePrefixPattern):
    include 函数 06:22:07.405654 line        50         for url_pattern in patterns:
    include 函数 Modified var:.. url_pattern = <URLPattern 'book_list/' [name='book_list']>
    include 函数 06:22:07.408647 line        51             pattern = getattr(url_pattern, 'pattern', None)
    include 函数 Modified var:.. pattern = <django.urls.resolvers.RoutePattern object at 0x000001EE4C258C50>
    include 函数 06:22:07.423606 line        52             if isinstance(pattern, LocalePrefixPattern):
    include 函数 06:22:07.438566 line        50         for url_pattern in patterns:
    include 函数 06:22:07.439563 line        56     return (urlconf_module, app_name, namespace)
    include 函数 06:22:07.449547 return      56     return (urlconf_module, app_name, namespace)
    include 函数 Return value:.. (<module 'book.urls' from 'C:\\Users\\MI\\Desktop\\04\\chapter02\\first_project\\book\\urls.py'>, None, None)
    include 函数 Elapsed time: 00:00:00.214428

可以看到 include 函数，主要做的事情就是 import 应用的 urls.py，然后把列表拆分  




