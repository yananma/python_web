
一节课一行笔记  

## Django 入门  

#### 前期配置  
创建项目：`django-admin startproject mysite`  
Django 项目生成的各个文件介绍  
配置 MySQL，不用记，代码 settings 里面有网址，复制就行  
创建应用：`django-admin startapp polls`  
添加到 INSTALLED_APPS 中  
项目是应用的容器  
BASE_DIR 就是项目文件夹  

创建模型，继承自 models.Model，添加一些字段  
生成迁移表：`python manage.py makemigrations polls`  
查看 SQL 语句：`python manage.py sqlmigrate polls 0001`  
迁移到数据库：`python manage.py migrate`  


#### 模型操作  
模型是你的数据的唯一的，权威的信息源，包含所存储的必要字段，通常一个模型对应数据库中的一张表，一个字段对应于数据库表中的一列  
每个字段都是 Field 子类的实例  
除了关联关系之外，一般第一个属性都是字段的自述名，就是 verbose_name  
blank 是用于前端表单的，默认是不可以输入空值的，设置了以后可以不填  
unique 唯一性约束，比如邮箱、手机号、身份证号码  
null，如果设置了 null=True，在数据库中会把空值设置为 NULL，CharField 类型不要设置，因为会有空字符串和 NULL  
choices 就是一个下拉列表  
max_length 是 CharField 的必填字段，在 \_\_init__方法中有一个 MaxLengthValidator 验证    

关联关系，多对一、一对一、多对多  

进入 shell 环境：`python manage.py shell`  
后面就是 model 操作 API，创建一个实例，save()、filter()、get()、delete()、update()、  


#### 后台管理  
创建账号：`python manage.py createsuperuser`  
输入账号密码：  
admim  
admin@qq.com  
password1234  
password1234  

配置 admin.py   
`from .models import Question`  
`admin.site.register(Question)`  

可以自己设置后台显示样式  

#### 视图  
在 views.py 中创建视图函数  
配置 url  
浏览器找的时候是通过 url 找到 urls.py，从 urls.py 的配置中找到 views 函数，通过 views 函数返回响应  
跳转到详细页面，移除硬编码，可以使用 `{% url 'detail' question.id %}`，这里单引号里的 detail 是 path 里面的 name  
在 Vote 函数中第一句做一个验证，`question = get_object_or_404(Question, pk=question_id)`  

`selected_choice = question.choice_set.get(pk=request.POST['choice'])` POST 后面的 choice 是表单里的 name，前端代码是：`<input type="radio" name="choice">`  
这种方式 request.POST，就是一个 MultiValueDict，就是一个字典，[''] 就是字典取值，key 就是前端表单的名字，value 就是表单提交内容   

最后返回，`HttpResponseRedirect(reverse('result'))` 这里 result 也是 path 里面的 name，会根据 url 配置找到 result 视图函数  

generic 通用视图  

FILE 上传文件用  

Django 内建视图类：TemplateView 最简单，直接显示页面，传一个 html 就可以了；
```python
class AboutView(TemplateView):
    template_name = 'myapp/about.html'

class PersonList(ListView):
    model = Person
    template_name = 'myapp/personlist.html'

class PersonDetailView(DetailView):
    model = Person
    template_name = "myapp/detail.html"
```


#### 表单  
浏览器提交内容就要用到表单  

在 forms.py 中定义 form，最后生成的 form 不是 HTML 写的 form，是 Django forms.py 生成的 form  
在 view 函数里面使用 form  
映射到模板中，{{ form }}  


#### 模板  

变量  
{{}}  

标签  
{% if 或 for %}  
{% url 'detail' %}
{% block title，extends 'base.html'，include %}  

过滤器  
读源码最容易  

`choice{{ forloop.counter }}` 拿到 choice1，choice2，choice3  


## 留言板项目  

[models.py](https://github.com/yananma/python_web/blob/main/%E4%B8%8D%E5%B8%B8%E7%94%A8/Django%20%E9%A1%B9%E7%9B%AE/%E7%95%99%E8%A8%80%E6%9D%BF/models.py)  
[forms.py](https://github.com/yananma/python_web/blob/main/%E4%B8%8D%E5%B8%B8%E7%94%A8/Django%20%E9%A1%B9%E7%9B%AE/%E7%95%99%E8%A8%80%E6%9D%BF/forms.md)  
[views.py](https://github.com/yananma/python_web/blob/main/%E4%B8%8D%E5%B8%B8%E7%94%A8/Django%20%E9%A1%B9%E7%9B%AE/%E7%95%99%E8%A8%80%E6%9D%BF/views.py)  

## 博客项目  




创建项目 File -> New Project -> Django -> 填写 Location -> 选择 Existing interpreter -> 选择解释器(好像有些问题，选择已有环境以后还会显示安装 django，不知道为什么)  

Ctrl + Shift + r 清除缓存刷新，很多问题都是因为有缓存  

