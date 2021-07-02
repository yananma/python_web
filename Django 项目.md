
一节课一行笔记，写实现某项功能的关键  

### 排错清单  
单词写错了  
缺括号  
创建应用以后，没在 INSTALLED_APPS 中添加  
Ctrl + Shift + r 清除缓存刷新，很多问题都是因为有缓存  
类中的方法没写 self  


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
视图函数全部都是使用 View 创建  

## 博客项目  

#### 前期准备  
项目演示  
下载安装  
创建项目，创建应用  

[models.py](https://github.com/yananma/python_web/blob/main/%E4%B8%8D%E5%B8%B8%E7%94%A8/Django%20%E9%A1%B9%E7%9B%AE/%E5%8D%9A%E5%AE%A2/models.py)  
```python
STATIC_URL = '/static/'    # 这个是 url 用的

STATICFILES_DIRS = [
    os.path.join(BASE_DIR, 'static')    # 这个是目录  
]
```

配置视图和 url  
后台注册  

### 首页  

#### 轮播图替换  
is_active 发挥作用  
```python
{% for banner in banner_list %}
{% if banner.is_active %}
<li data-target="#focusslide" data-slide-to="{{banner.idx}}" class="active"></li>
{% else %}
<li data-target="#focusslide" data-slide-to="{{banner.idx}}"></li>
{% endif %}
{% endfor %}
```

#### 推荐博客  
models.py 中的 blog 模型有一个 recommend 字段：` recommend = models.BooleanField('推荐博客', default=False)`  
views.py `recommend_list = Post.objects.filter(recommend=1)`  
前端页面  
```python 
{% for post in recommend_list %}
<article class="excerpt-minic excerpt-minic-index">
    <h2><span class="red">【推荐】</span><a target="_blank" href="/blog/{{post.id}}" title="{{post.title}}" >{{post.title}}</a>
    </h2>
    <p class="note">{{post.content}}</p>
</article>
{% endfor %}
```

#### 最新博客列表   
`post_list = Post.objects.order_by('pub_date').all()[:3]`

主外键关联关系，category 是 post 的 ForeignKey  
`<a class="cat" href="/category/{{post.category.id}}" title="{{post.category.name}}" >{{post.category.name}}<i></i></a>`  

评论数  
`{{post.views}}`  

浏览数  
`{{post.comment_set.count}}`  

#### 博客分类  
先创建 BlogCategory 类：  
```python 
class BlogCategory(models.Model):
    name = models.CharField('分类名称', max_length=20, default='')
```
在 Post 类中外键关联  
`category = models.ForeignKey(BlogCategory, verbose_name='博客分类', default=None, on_delete=True)`  
在 views.py 的 index 函数中取值  
`blogcategory_list = BlogCategory.objects.all()`  
在前端页面显示  
```python
{% for c in blogcategory_list %}
    <a href="/category/{{c.id}}" title="{{c.name}}" >{{c.name}}</a>
{% endfor %}
```      

#### 右侧最新评论文章  
一篇文章 20 个评论都是最新的，但是不能把这篇文章显示 20 次，所以要去重  
views.py   
```python
comment_list = Comment.objects.order_by('pub_date').all()[:10]    # 取出最新的评论  
comment_list1 = []
post_list1 = []
for c in comment_list:
    if c.post.id not in post_list1:
        comment_list1.append(c)
        post_list1.append(c.post.id)
ctx = {
    'comment_list':comment_list1,
}
```
前端展示，关联关系，comment 类中有 post 字段：`post = models.ForeignKey(Post, verbose_name='博客', on_delete=True)`    
```python
{% for c in comment_list %}
<li>
  <a title="{{c.post.title}}" href="#" >
    <span class="thumbnail">
            <img class="thumb" data-original="/{{c.post.cover}}" src="/{{c.post.cover}}" alt="{{c.post.cover}}"  style="display: block;">
        </span>
    <span class="muted"><i class="glyphicon glyphicon-time"></i>
            {{c.post.pub_date|date:'Y-m-d'}}
        </span>
  </a>
</li>
{% endfor %}
```

#### 搜索功能
要创建一个视图函数，用的是 list 列表页模板  
前端 index.html 是一个 form 表单    	
```python
<form class="navbar-form" action="/search" method="post">
  <div class="input-group">
        <input type="text" name="keyword" (views 函数中是用这里的 name 取的输入的值) class="form-control" size="35" placeholder="请输入关键字" maxlength="15">
        <span class="input-group-btn">
        <button class="btn btn-default btn-search" name="search" type="submit">搜索</button>
        </span>
  </div>
</form>
```
```python 
class SearchView(View):
    def get(self, request):
        pass
    def post(self, request):
        kw = request.POST.get('keyword')
        post_list = Post.objects.filter(Q(title__icontains=kw)|Q(content__icontains=kw))
        ctx = {
            'post_list':post_list,
        }
        return render(request, 'list.html', ctx)
```
前端 list.html 展示文章    
```python
{% for post in post_list.object_list %}
  <article class="excerpt excerpt-1"><a class="focus" href="/blog/{{post.id}}" title="{{post.title}}" target="_blank" >
	<header><a class="cat" href="#" title="{{post.category.name}}" >{{post.category.name}}<i></i></a>
	  <h2><a href="/blog/{{post.id}}" title="{{post.title}}" target="_blank" >{{post.title}}</a></h2>
	</header>
  </article>
{% endfor %}
```

#### 友情链接  
需要在 models.py 写一个类  
```python 
class FriendlyLink(models.Model):
    title = models.CharField('标题', max_length=50)
    link = models.URLField('链接', max_length=50, default='')
```    
在 admin.py 中注册  
`admin.site.register(FriendlyLink)`  
在 views.py 的 index 视图函数中取值  
`links = FriendlyLink.objects.all()`  
前端替换  
```python 
{% for link in links %}
    <a href="{{link.link}}" title="{{link.title}}" target="_blank">{{link.title}}</a>&nbsp;&nbsp;&nbsp;
{% endfor %}
```

#### 列表页  
就是写一个视图函数，去除所有的值  

#### 分页功能  
安装 django-pure-pagination  
照着 github 官方文档一步一步写就行了。  

#### 标签云功能  
views.py 中创建一个类  
```python 
class TagMessage(object):
    def __init__(self, tid, title, count):
        self.tid = tid
        self.title = title
        self.count = count
```
在 views.py 的 blog_list 视图函数中添加  
```python 
tags = Tags.objects.all()
tag_message_list = []
for t in tags:
    count = len(t.post_set.all())
    tm = TagMessage(t.id, t.title, count)
    tag_message_list.append(tm)

ctx = {
    'tags':tag_message_list,
}
```
前端 index.html 中  
```python
{% for t in tags %}
    <li><a href="/tags/{{t.tid}}" title="{{t.title}}">{{t.title}} <span class="badge">{{t.count}}</span></a></li>
{% endfor %}
```

#### 分类查询功能  
在视图中获取数据  
```python
def blog_list(request, cid=-1):
    post_list = None
    if cid != -1:    # 分类查询  
        category = BlogCategory.objects.get(id=cid)
        post_list = category.post_set.all()    # 多对多  
    else:    # 默认查询所有  
        post_list = Post.objects.all()
```
配置 url  
`path('category/<int:cid>', views.blog_list, name='category')`  
在前端页面显示  
```python
{% for c in blogcategory_list %}
    <a href="/category/{{c.id}}" title="{{c.name}}" >{{c.name}}</a>
{% endfor %}
```

#### 标签查询功能  
和上面的过程一样  
添加一个 tid  
```python 
def blog_list(request, tid=-1):
    post_list = None
    if tid!=-1:
        tag = Tags.objects.get(id=tid)
        post_list = tag.post_set.all()
    else:
        post_list = Post.objects.all()
```

### 详细页  
先创建 Comment 模型  
```python
class Comment(models.Model):
    post = models.ForeignKey(Post, verbose_name='博客', on_delete=True)    # 有两个外键  
    user = models.ForeignKey(BlogUser, verbose_name='作者', on_delete=True)
    pub_date = models.DateTimeField('发布时间')
    content = models.TextField('内容')
```

views.py  
```python
def blog_detail(request, bid):
    post = Post.objects.get(id=bid)
    post.views = post.views + 1    # 访问一次，浏览数加 1 
    post.save()
    new_comment_list = Comment.objects.order_by('-pub_date').all()[:10]    # 右侧最新博客  
    # 去重
    new_comment_list1 = []
    post_list1 = []
    for c in new_comment_list:
        if c.post.id not in post_list1:
            new_comment_list1.append(c)
            post_list1.append(c.post.id)
    comment_list = post.comment_set.all()
    tag_list = post.tags.all()
    post_recommend_list =set(Post.objects.filter(tags__in=tag_list)[:6])    # 推荐文章，选择是标签相同的 post；
                                                                            # set 去重，是因为可能包含多个标签，就会显示多次
```
post 和 tags 是多对多关系，在详细页面取博客所有标签的时候，用的是 `{{post.tags.all}}`

评论功能  
前端 detail.html 页面  
```python 
<form id="comment-form" name="comment-form" action="/comment/{{post.id}}/" method="POST">
    <div class="comment">
        <input name="username" id="" value="{{user.username}}" size="22" placeholder="您的昵称（必填）" maxlength="15" tabindex="1" type="text">
	<div class="comment-box">
		<textarea placeholder="您的评论或留言（必填）" name="content" id="comment-textarea" cols="100%" rows="3" tabindex="3"></textarea>
		<div class="comment-ctrl">
			<button type="submit" name="comment-submit" id="comment-submit" tabindex="4">评论</button>
		</div>
	</div>
    </div>
    {% csrf_token %}
</form>
```
views.py 写 comment 视图  
```python 
class CommentView(View):
    def get(self, request):
        pass
    def post(self, request, bid):
        comment = Comment()
        comment.user = request.user
        comment.post = Post.objects.get(id=bid)
        comment.content = request.POST.get('content')
        comment.pub_date = datetime.now()
        comment.save()
        return HttpResponseRedirect(reverse("blog_detail", kwargs={"bid":bid}))    # comment 有视图，没有自己 HTML，因为评论是 detail 页面的一部分，所以要跳转到 detail  
```
配置 url：`path('comment/<int:bid>', views.CommentView.as_view(), name='comment')`  
显示评论列表  
```html
 {% for comment in comment_list %}
    <li class="comment-content">
    <span class="comment-f">#{{forloop.counter}}</span>
    <div class="comment-main">
        <p>
        <a class="address" href="#" rel="nofollow" target="_blank">{{comment.user.username}}</a>
	<span class="time">({{comment.pub_date|date:'Y-m-d'}})</span><br>{{comment.content}}
	</p>
    </div>
    </li>
{% endfor %}
```
所以流程就是，先在 form 表单中写评论，写完提交跳转到 action 指定的 url，通过 url 找到 CommentView 视图类，通过 save() 保存到数据库，然后 redirect 到 blog_detail() 函数，从数据库中取 comment，然后 render 到前端页面  

#### 登录功能  
配置 url  
`path('login', views.LoginView.as_view(), name='login')`  
写视图函数  
```python 
class LoginView(View):
    def get(self, request):
        return render(request, 'login.html')
    def post(self, request):
        username = request.POST.get('username')
        password = request.POST.get('password')
        user = authenticate(username=username, password=password)
        if user:
            if user.is_active:
                login(request, user)
                return HttpResponseRedirect(reverse("index"))
            else:
                return render(request, 'login.html', {'error_msg':'用户未激活'})
        else:
            return render(request, 'login.html', {'error_msg':'用户名或密码错误！'})
```
最开始走的是 get 方法，展示页面以后，填写提交，走的是 post 方法  
登录成功以后，前端右上角显示用户名  
```python 
<ul class="nav navbar-nav navbar-right">
  {% if user.is_authenticated %}
  <li><a data-cont="用户" title="用户" href="#">欢迎，{{user.username}}</a></li>
  <li><a data-cont="注册" title="注册" href="/user/logout">注销</a></li>
  {% else %}
  <li><a data-cont="登录" title="登录" href="/user/login">登录</a></li>
  <li><a data-cont="注册" title="注册" href="/user/register">注册</a></li>
  {% endif %}
</ul>
```
#### 注册功能  
配置 url  
`path('register', views.RegisterView.as_view(), name='register')`  
写视图函数  
```python 
class RegisterView(View):
    def get(self, request):
        return render(request, 'register.html')
    def post(self, request):
        username = request.POST.get('username')
        password = request.POST.get('password')
        email = request.POST.get('email')
        my_send_email(email)    
        user = BlogUser()
        user.username = username
        user.password = make_password(password)
        user.email = email
        user.is_active = False
        user.save()    # 这里会保存一个没有激活的用户，激活以后再 update  
        return render(request, 'login.html', {})
```
最开始走的是 get 方法，展示页面以后，填写提交，走的是 post 方法  

#### 激活用户  
要先在 settings 里面配置  
```python
EMAIL_BACKEND = 'django.core.mail.backends.smtp.EmailBackend'
EMAIL_HOST = 'smtp.163.com'
EMAIL_PORT = 25
EMAIL_HOST_USER = 'mayananlzjt@163.com'
EMAIL_HOST_PASSWORD = ''
EMAIL_FROM = '描述的几个字<mayananlzjt@163.com>'
```
创建 email 的 model  
```python 
class EmailVerifyRecord(models.Model):
    code = models.CharField(verbose_name='验证码', max_length=50, default='')
    email = models.EmailField('邮箱', max_length=50)
    send_type = models.CharField('验证码模型', choices=(("register", "注册"), ('forget', '找回密码'), ("update_email", '修改邮箱')), max_length=30)
    send_time = models.DateTimeField('发送时间', default=datetime.now)
```
views.py 中写几个函数  
```python 
# 生成随机字符串
def make_random_str(randomlength=8):
    str = ''
    chars = 'AaBbCcDdEeFfGgHhIiJjKkLlMmNnOoPpQqRrSsTtUuVvWwXxYyZz0123456789'
    length = len(chars) - 1
    random = Random()
    for i in range(randomlength):
        str+=chars[random.randint(0, length)]
    return str

# 发送邮件
def my_send_email(email, send_type="register"):
    email_record = EmailVerifyRecord()
    if send_type == "update_email":
        code = make_random_str(4)
    else:
        code = make_random_str(16)
    email_record.code = code
    email_record.email = email
    email_record.send_type = send_type
    email_record.save()
    email_title = ""
    email_body = ""
    if send_type == "register":
        email_title = "享学博客-注册激活链接"
        email_body = "请点击下面的链接激活你的账号: http://127.0.0.1:8000/active/{0}".format(code)    # 可以点击这个链接，就说明邮箱是对的，就可以激活
        send_status = send_mail(email_title, email_body, EMAIL_FROM, [email])
        if send_status:
            pass
    elif send_type == "forget":
        email_title = "享学博客-网注册密码重置链接"
        email_body = "请点击下面的链接重置密码: http://127.0.0.1:8000/reset/{0}".format(code)
        send_status = send_mail(email_title, email_body, EMAIL_FROM, [email])
        if send_status:
            pass
    elif send_type == "update_email":
        email_title = "享学博客-邮箱修改验证码"
        email_body = "你的邮箱验证码为: {0}".format(code)
        send_status = send_mail(email_title, email_body, EMAIL_FROM, [email])
        if send_status:
            pass
```
url 是 `path('active', ActiveView.as_view(), name='active')`  
```python 
class ActiveView(View):
    def get(self, request, active_code):
        all_records = EmailVerifyRecords.objects.filter(code=active_code) 
        if all_records:
            for record in all_records:
                email = record.email 
                user = BlogUser.objects.get(email=email) 
                user.is_active = True     # 核心是这一句  
                user.save()    # 这个 save 其实就是 update  
        else:
            return render(request, "active_fail.html") 
        return render(request, "login.html")
```

#### 注销功能
```python
class LogoutView(View):
    def get(self, request):
        logout(request)
        return HttpResponseRedirect(reverse("index"))
```
配置 url `path('logout', LogoutView.as_view(), name='logout')`

#### 富文本编辑器  
GitHub 搜 kindeditor  
下载 zh-CN zip 包，解压  
在 static/js 下创建一个 editor 文件夹，复制包里面的 lang、plugins、themes、kindeditor-all.js  
在 editor 文件夹下创建一个 config.js，添加代码    
```js 
KindEditor.ready(function(K) {
    window.editor = K.create('#id_content',{
        // 指定大小
        width:'800px',
        height:'200px',
    });
});
```
然后要在 admin.py 中注册  
```python
class PostAdmin(admin.ModelAdmin):
    class Media:
        js = (
            'js/editor/kindeditor-all.js',
            'js/editor/config.js',
        )
admin.site.register(Post, PostAdmin)
```




创建项目 File -> New Project -> Django -> 填写 Location -> 选择 Existing interpreter -> 选择解释器(好像有些问题，选择已有环境以后还会显示安装 django，不知道为什么)  


