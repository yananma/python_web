
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



### 章节1 Django 预热  

虚拟环境，防止环境冲突，运行多版本软件  

pip install virtualenv  

virtualenv django_env(先 cd 到文件夹下面，比如 cd /home；这个命令会创建文件夹)  
source django_env/bin/activate  
deactivate  

virtualenvwrapper 更简单  

pycharm 改虚拟环境：右下角 interpreter  

第一次添加虚拟环境：右下角 Interpreter Settings > 齿轮 > show all > + > 选择 Conda Environment > Existing environment >  

pycharm 创建 Django 项目的时候，选择 existing environment，不要创建新的 environment  

IP 地址和 url 的关系就是手机号码和备注名的关系  

web服务器：负责处理http请求，响应静态文件，常见的有Apache，Nginx以及微软的IIS.  
应用服务器：负责处理逻辑的服务器。比如php、python的代码，是不能直接通过nginx这种web服务器来处理的，只能通过应用服务器来处理，常见的应用服务器有 uwsgi、tomcat 等。  


### 章节2 Django URL  

只有自己本机运行才使用 127.0.0.1，如果想要让其他用户访问，就必须改成 0.0.0.0  

动态页面的意思就是页面的内容都是可以动态变化的，是从数据库里取出来的  

豆瓣网站就是一个项目，图书、电影、音乐就是应用  

debug 模式，修改内容以后自动重启，不用每次自己手动重启；出现错误会打印在浏览器或控制台中    

视图的第一个参数永远都是 request(一个 HttpRequest)对象。这个对象**存储了请求过来的所有信息**，包括携带的参数以及一些头部信息等。  

django urls 的 path 中不配置域名，只配置文件路径  

指定 id 可以访问特定的详情页面，是动态的  

? 查询字符串的方式不需要在 views 的函数中指定参数 id，urls 里也不用指定 id，而是在 views 的函数中使用 `book_id = request.GET.get('id')` 或 `book_id = request.GET.get['id']`   

指定 name，url 是经常变化的，那么如果改了 url 前面的 route，别的地方也不用更改，否则工作量就非常大了。比如原来是 `path('login/', views.login, name='login')` 后来改成了 `path('signin/', views.login, name='login')` 那么别的地方都不用改，比如首页中视图函数中，如果没有登录，就返回登录页面。reverse('login') 就不用改，reverse('login') 的结果就是 /signin/，可以在返回前 print 看一下  

namesapce 命名空间，用以区分不同的应用和不同的应用实例   

reverse 可以传递参数  

可以自己自定义 converter，实现动态路由  

可以在 url 映射的时候指定默认参数  


### 第3章 Django 模板  

使用 render 最简单  

print(BASE_DIR) 看路径  

查找路径，可以是在 DIRS 中自己配置，可以在应用中创建 templates 文件夹，Django 自己就可以查找到  

`{{ 变量 }}`  

`{{ if 标签、for 标签 }}`  

PyCharm 在编写标签的时候，输入 if 按 Tab 键，就可以自动创建标签，非常方便  

过滤器，在 django/template/defaultfilters.py 中查看，最全的，过滤器的实现都非常简单  

自定义过滤器   

静态文件  


多写注释  
改一改，看变化，比如 models.py 中的 verbose_name 的作用  
在报错位置使用 pysnooper  
用 python manage.py -h 查看命令  
print(Banner.objects.all().query) 看 sql 命令  
可以在 views 中使用 pysnooper  
可以看别人的网站的源码  

