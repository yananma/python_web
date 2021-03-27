

## 第1章 构建博客应用程序  
隔离环境，要好得多  

创建虚拟环境  
`pip install virtualenv`  

`virtualenv django_env`(先 cd 到文件夹下面，比如 cd /home；这个命令会创建文件夹；可以指定 python 版本)  
`source django_env/bin/activate`  
`deactivate`  

创建项目：  
`django-admin startproject mysite`  
`cd mysite`  
`pycharm .`  

misite 是项目目录  

`python manage.py migrate`  

settings 参数的意义  

`python manage.py startapp blog`  

为 blog 应用添加 model  

博客和评论，ForeignKey 写到评论里；ForeignKey 多对一  

在 INSTALLED_APPS 中加入 blog.apps.BlogConfig  

`python manage.py makemigrations blog`  

`python manage.py sqlmigrate blog 0001`  

表名自动生成，默认：小写 应用名_模型名，可以自己指定  

自动生成主键，也可以自己设定，primary_key=True  

`python manage.py migrate`  

`python manage.py createsuperuser`  

`admin.site.register(Post)`  

可以自己定制 admin，遇到细看  

python manage.py shell 

    >>> from django.contrib.auth.models import User
    >>> from blog.models import Post
    >>> user = User.objects.get(username='admin')
    >>> post = Post(title='Another post',
    ...             slug='another-post',
    ...             body='Post body',
    ...             author=user)
    >>> post.save()

操作数据库  


视图函数，接收 Web 请求，返回 Web 响应，处理逻辑全部位于视图中  

渲染模板，就是传递变量，就是 render 做的事情；render() 接收 request 对象、模板路径以及上下文变量，就是把变量传给模板  

配置 url  

创建视图模板  

分页功能  
 




