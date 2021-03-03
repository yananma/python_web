
再听完一遍就可以写：读过部分 Django 源码，了解 Django ORM、视图、模板、表单、路由、中间件的运行原理  

多查

读目录 20 遍，熟悉了目录，看到这个知识点，才会想到来查：
2021.03.03：1 遍      



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







