
再听完一遍就可以写：读过部分 Django 源码，了解 Django ORM、视图、模板、表单、路由、中间件的运行原理  

多查

读目录 20 遍，熟悉了目录，看到这个知识点，才会想到来查：
2021.03.03：1 遍      

### 第1章 初识Django框架  

Django框架将交互过程拆分为Model（模型）、Template（模板）和View（视图），即MTV设计模式，主要包括以下内容。  

（1）M（Model）：数据存取层，这一层处理所有与数据相关的事务，提供在数据库中管理（添加、修改、删除）和查询记录的机制。  

（2）T（Template）：表现层，处理页面的显示，即所有与表现相关的决定都由这一层去处理。  

（3）V（View）：业务逻辑层，负责处理业务逻辑，会在适当的时候将Model与Template组合在一起，通常被认为是联通M与T的桥梁。


ORM（Object Relational Mapping，对象关系映射）把对象与数据库中的表关联起来，对象的属性映射到表的各个字段，同时，还把对表的操作对应到对对象的操作，实现了对象到SQL、SQL到对象的过程转换。  

User.objects.all()  
User.objects.filter(name__contains='a')  
User.objects.create(name='b', password='c')  


### 第3章 Django项目框架搭建  

django-admin startproject my_bbs  

可以通过 python manage.py shell 进入项目环境  


