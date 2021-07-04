
一节课一行笔记，写实现某项功能的关键  

### 排错清单  
单词写错了  
缺括号  
Ctrl + Shift + r 清除缓存刷新，很多问题都是因为有缓存  
类中的方法没写 self  


#### 固定步骤  
创建模型，添加到 admin，后台添加数据，在视图函数中，从数据库取值，共享到前端，前端替换     
写完视图函数添加 url   
修改 models.py 以后，要 makemigrations、migrate  
创建应用以后，在 INSTALLED_APPS 中添加  


#### 想法  
是一个具体的东西，就要创建 model，比如合作机构，比如友情链接，这些都是类的实例   
添加数据的本质就是创建一个类的实例  


## Django 基础知识  
框架的作用：  
封装：大量功能的封装  
简化：复杂功能封装以后做到了简化  
优化：框架做了大量的优化  
安全：框架有完善的安全机制  
管理：模块化，层次划分清晰，易于管理维护  

Django 是一个重度框架，大而全，适合大型团队管理。学习成本高一些。  
Django 可以做网站开发、微信公众号、小程序后端开发等，只要是有 HTTP 的地方，都可以用 Django  
人工智能平台融合，前面是打车微信小程序，中间是 Django，后面是人工智能系统。  

MTV 核心思想就是解耦，便于开发维护，增加模块的可重用性。  


#### 前期配置  
python manage.py 的所有可用命令都在 django/core/management/commands 文件夹下面  

创建项目：`django-admin startproject mysite`  
配置 MySQL，不用记，代码 settings 里面有网址，复制就行  
创建应用：`django-admin startapp polls`  
添加到 INSTALLED_APPS 中，就是源码中的 app_label    
项目是应用的容器  
BASE_DIR 就是项目文件夹  

创建模型，继承自 models.Model，添加一些字段  
生成迁移表：`python manage.py makemigrations polls`  
查看 SQL 语句：`python manage.py sqlmigrate polls 0001`  
迁移到数据库：`python manage.py migrate`  


#### 模型操作  
模型是你的数据的唯一的，权威的信息源，包含所存储的必要字段，一个模型对应数据库中的一张表，一个字段对应于数据表中的一列  
Django ORM 可以用相同的接口操作不同的数据库，做了底层封装；更加安全；易读性更高；不用因为修改数据库而修改代码  
每个字段都是 Field 子类的实例；每个字段都是模型的类属性    
在 model.py 的模型类中，class Meta 的 verbose_name，是类显示的名字，是点进去之前显示的。  
def \_\_str__(self)，是点进去以后实例显示的内容  
字段的 verbos_name 是再点进去编辑的时候，左侧显示的名字  
DateField 日期  
DateTimeField 时间  
auto_now_add 创建时间  
auto_now 修改时间   
修改属性：模型对象.属性 = 新值，然后 save()  
除了关联关系之外，一般第一个属性都是字段的自述名，就是 verbose_name  
blank 是用于前端表单的，默认是不可以输入空值的，设置了以后可以不填  
unique 唯一性约束，比如邮箱、手机号、身份证号码  
null，如果设置了 null=True，在数据库中会把空值设置为 NULL，CharField 类型不要设置，因为会有空字符串和 NULL  
choices 就是一个下拉列表  
max_length 是 CharField 的必填字段，在 \_\_init__方法中有一个 MaxLengthValidator 验证    

关联关系：多对一、一对一、多对多  
ForeignKey，Comment 中的 ForeignKey 是 Blog，所以 Comment 直接就有 Blog 字段，所以取值的时候直接取，comment.blog.title  
Blog 中没有 Comment 字段，所以取的时候是反向查询，blog = Blog.objects.get(id=1)，blog.comment_set.all()，其中 comment_set 是自动添加的查询管理器  

进入 shell 环境：`python manage.py shell`  
model 操作 API，创建一个实例，save()、filter()、get()、delete()、update()、  


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
admin.site.site_header = '在线教育平台后台管理系统'  
django/contrib/admin/templates/admin/base_site.html  
在文件夹下面有很多 HTML 页面  


#### 视图  
在 views.py 中创建视图函数，写完视图函数配置 url  
浏览器找的时候是通过 url 找到 urls.py，从 urls.py 的配置中找到 views 函数，通过 views 函数返回响应  
路由列表必须叫 urlpatterns，因为源码里是 `getattr(urlconf_module, 'urlpatterns')`  
views 后面接函数名，不加括号是函数，加括号是函数的返回值；  
继承 View 类的时候，as_view() 加括号，加括号源码最后返回的是 as_view 内部定义的 view 函数，所以还是函数  
跳转到详细页面，移除硬编码，可以使用 `{% url 'detail' question.id %}`，这里单引号里的 detail 是 path 里面的 name  
在 View 函数中第一句做一个验证，`question = get_object_or_404(Question, pk=question_id)`  
`selected_choice = question.choice_set.get(pk=request.POST['choice'])` ['choice'] 中的 choice 是表单里的 name，前端代码是：`<input type="radio" name="choice">`  
request.POST 得到的就是一个 QueryDict，就是一个字典，[''] 就是字典取值，key 就是前端表单的名字，value 就是表单提交内容   

最后返回，`HttpResponseRedirect(reverse('result'))` 这里 result 也是 path 里面的 name，会根据 url 配置找到 result 视图函数  


#### 模板  
要看是不是要有一个新的页面，如果是一个全新的页面，比如 vip 页面，就要添加一个 html 模板，然后要添加视图  

变量：{{ }}  
标签：{% if 或 for、url、block、extends、include %}  
过滤器：读源码最容易  

`choice{{ forloop.counter }}` 拿到 choice1，choice2，choice3  


#### 表单  
浏览器提交内容就要用到表单  

在 forms.py 中定义 form，最后生成的 form 不是 HTML 写的 form，是 Django forms.py 生成的 form  
在 view 函数里面使用 form  
映射到模板中，{{ form }}  


#### 用户  
user 的方法和属性都在 django/contrib/auth/models.py 的 AbstractUser 和它的父类 AbstractBaseUser 中，比如 username、is_active，比如 is_authenticated  


#### 路由  
路由就是给谁  



## 留言板项目  

[models.py](https://github.com/yananma/python_web/blob/main/%E4%B8%8D%E5%B8%B8%E7%94%A8/Django%20%E9%A1%B9%E7%9B%AE/%E7%95%99%E8%A8%80%E6%9D%BF/models.py)、[forms.py](https://github.com/yananma/python_web/blob/main/%E4%B8%8D%E5%B8%B8%E7%94%A8/Django%20%E9%A1%B9%E7%9B%AE/%E7%95%99%E8%A8%80%E6%9D%BF/forms.md)、[views.py](https://github.com/yananma/python_web/blob/main/%E4%B8%8D%E5%B8%B8%E7%94%A8/Django%20%E9%A1%B9%E7%9B%AE/%E7%95%99%E8%A8%80%E6%9D%BF/views.py)  
视图函数全部都是使用 View 创建的，读完就学会 View 类写视图了  

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
```html
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
    <h2>【推荐】<a href="/blog/{{post.id}}" title="{{post.title}}">{{post.title}}</a></h2>
    <p class="note">{{post.content}}</p>
</article>
{% endfor %}
```

#### 最新博客列表   
`post_list = Post.objects.order_by('pub_date').all()[:3]`

主外键关联关系，category 是 post 的 ForeignKey，在 post 模型中 `category = models.ForeignKey(Category, on_delete=True)`  
`<a class="cat" href="/category/{{post.category.id}}" title="{{post.category.name}}" >{{post.category.name}}<i></i></a>`  

评论数  
`{{post.views}}`  

浏览数  
`{{post.comment_set.count}}`  

#### 博客分类的显示  
先创建 Category 类：  
```python 
class Category(models.Model):
    name = models.CharField('分类名称', max_length=20, default='')
```
在 Post 类中外键关联  
`category = models.ForeignKey(Category, on_delete=True)`  
在 views.py 的 index 函数中取值  
`category_list = Category.objects.all()`  
在前端页面显示  
```python
{% for c in category_list %}
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
前端展示，关联关系，Comment 类中有 post 字段：`post = models.ForeignKey(Post, verbose_name='博客', on_delete=True)`    
```python
{% for c in comment_list %}
<li>
  <a title="{{c.post.title}}" href="#" >
            <img class="thumb" data-original="/{{c.post.cover}}" src="/{{c.post.cover}}" alt="{{c.post.cover}}">
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
        <input type="text" name="keyword" (views 函数中是用这里的 name 取的输入的值) placeholder="请输入关键字" maxlength="15">
        <button class="btn btn-default btn-search" name="search" type="submit">搜索</button>
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
  <article><a class="focus" href="/blog/{{post.id}}" title="{{post.title}}" target="_blank" >
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
    <a href="{{link.link}}" title="{{link.title}}" target="_blank">{{link.title}}</a>
{% endfor %}
```

#### 列表页  
就是写一个视图函数，取出所有的值  

#### 分页功能  
安装 django-pure-pagination  
照着 github 官方文档一步一步写就能运行成功。  
前端在 \_pagination.html 中 `<li><a href="?{{ page.querystring }}" class="btn-squae">{{ page }}</a></li>`
```python 
try:
    page = request.GET.get('page', 1)
except PageNotAnInteger:
    page = 1
p = Paginator(course_list, per_page=1, request=request)
course_list = p.page(page)   # 最重要的就是 Paginator 的 page 方法，
                             # page 方法的核心就是对列表切片 self.object_list[bottom:top]  
```


#### 标签云展示  
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
    <li><a href="/tags/{{t.tid}}" title="{{t.title}}">{{t.title}}{{t.count}}</a></li>
{% endfor %}
```

#### 分类查询功能  
在视图中获取数据  
```python
def blog_list(request, cid=-1):
    post_list = None
    if cid != -1:    # 分类查询，核心就是下面这两句    
        category = BlogCategory.objects.get(id=cid)
        post_list = category.post_set.all()    
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
    if tid!=-1:    # 拿到这个 tag，找到这个 tag 的所有文章
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
    post.views = post.views + 1    # 访问一次 url 即 blog_detail 函数，浏览数就加 1 
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

评论功能  
前端 detail.html 页面  
```python 
<form name="comment-form" action="/comment/{{post.id}}/" method="POST">
    <div class="comment">
        <input name="username" value="{{user.username}}" placeholder="您的昵称（必填）" type="text">
	<div class="comment-box">
		<textarea placeholder="您的评论（必填）" name="content"></textarea>
		<button type="submit" name="comment-submit">评论</button>
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
        return HttpResponseRedirect(reverse("blog_detail", kwargs={"bid":bid}))    
	# comment 有视图，没有自己 HTML  
```
配置 url：`path('comment/<int:bid>', views.CommentView.as_view(), name='comment')`  
在 blog_detail 视图函数中取值，`comment_list = post.comment_set.all()`
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
        if user:    # 如果通过，就是说已经匹配成功了
            if user.is_active:    # 这里的 login 就是前端显示用的，并没有验证功能
                login(request, user)    # 读源码，是先 user = request.user，添加 session，然后 request.user = user  
                return HttpResponseRedirect(reverse("index"))
            else:
                return render(request, 'login.html', {'error_msg':'用户未激活'})
        else:
            return render(request, 'login.html', {'error_msg':'用户名或密码错误！'})
```
最开始走的是 get 方法，展示页面以后，填写提交，走的是 post 方法  
登录成功以后，前端右上角显示用户名  
```python 
{% if user.is_authenticated %}
<div class="group-sign-in">
  <a href="#" class="login">欢迎，{{user.username}}</a>
  <a href="{% url 'logout' %}" class="logout">注销</a>
</div>
{% else %}
<div class="group-sign-in">
  <a href="{% url 'login' %}" class="login">登录</a>
  <a href="{% url 'register' %}" class="register">注册</a>
</div>
{% endif %}
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
        user.password = make_password(password)    # 加密
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
EMAIL_HOST_USER = 'mayanan@163.com'
EMAIL_HOST_PASSWORD = ''
EMAIL_FROM = '描述的几个字<mayanan@163.com>'
```
创建 email 的 model  
```python 
class EmailVerifyRecord(models.Model):
    code = models.CharField(verbose_name='验证码', max_length=50, default='')
    email = models.EmailField('邮箱', max_length=50)
    choices = (("register", "注册"), ('forget', '找回密码'), ("update_email", '修改邮箱'))
    send_type = models.CharField('验证码模型', choices=choices, max_length=30)
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
        email_title = "博客-注册激活链接"  # 可以点击下面这个链接，说明收到邮件了，说明邮箱是对的，就可以激活
        email_body = "请点击下面的链接激活你的账号: http://127.0.0.1:8000/active/{0}".format(code)    
        send_status = send_mail(email_title, email_body, EMAIL_FROM, [email])
        if send_status:
            pass
    elif send_type == "forget":
        email_title = "博客-注册密码重置链接"
        email_body = "请点击下面的链接重置密码: http://127.0.0.1:8000/reset/{0}".format(code)
        send_status = send_mail(email_title, email_body, EMAIL_FROM, [email])
        if send_status:
            pass
    elif send_type == "update_email":
        email_title = "博客-邮箱修改验证码"
        email_body = "你的邮箱验证码为: {0}".format(code)
        send_status = send_mail(email_title, email_body, EMAIL_FROM, [email])
        if send_status:
            pass
```
url 是 `path('active', ActiveView.as_view(), name='active')`  
视图函数，点击链接就访问了 ActiveView，就把 user.is_active 设置为 True  
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
读 logout 源码，设置了 `user = None`  

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

## 在线教育平台  

#### 创建项目 创建应用  
`cd desktop`  
`mkdir elearning`  
`cd elearning`  
`conda env list`  
`activate django`  
`django-admin startproject xxkt`  
`python manage.py startapp myapp`  
在 INSTALLED_APPS 列表中添加 myapp   

配置数据库  
在 settings.py 里有数据库配置的文档  
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


#### 创建课程相关模型  
myapp 的 models.py 添加 Banner 类  
python manage.py makemigrations myapp 生成中间表  
然后执行 python manage.py migrate 根据中间表生成数据库中的一张 table  

[models.py](https://github.com/yananma/python_web/blob/main/%E4%B8%8D%E5%B8%B8%E7%94%A8/Django%20%E9%A1%B9%E7%9B%AE/%E5%9C%A8%E7%BA%BF%E6%95%99%E8%82%B2%E5%B9%B3%E5%8F%B0/models.py)  


#### 重写用户模型  
settings.py 中，添加 AUTH_USER_MODEL = 'myapp.XXUser'  
models.py   
```python 
class XXUser(AbstractUser):
    nikename = models.CharField('昵称', max_length=20)
```
看 AbstractUser，这个类就在原来的基础上多了一个 nikename 字段  

#### 模板  
配置模板，创建 templates 文件夹，os.path.join(BASE_DIR, 'templates')、创建视图函数，配置应用 url，include 到项目 url  
模板继承  

#### 轮播图  
创建模型，添加到 admin，后台添加数据，在 index 视图函数中，从数据库取值，共享到前端，前端替换   

#### 课程分类展示  
这个是展示，不是查询，展示就是从数据库取值  
`category_list = Category.objects.all()[:6]`  

#### 数据统计  
```python
teacher_count = Teacher.objects.count()
course_count = Course.objects.count()
user_count = XXUser.objects.count()
category_count = Category.objects.count()
```

#### 最新课程  
后台设置  
```python 
class CourseAdmin(admin.ModelAdmin):
    fields = ['category', 'level', 'title', 'body', 'cover', 'attachment',
            'is_free', 'teacher', 'star', 'price', 'recommend', 'published']

admin.site.register(Course, CourseAdmin)
```
`course_list = Course.objects.order_by('-pub_date').all()`  

#### 明星学员  
在前端有一个判断，active 的展示出来，如果不设置，最后就会像一个栈一样，都显示出来了  
```html
{%for stu in  starstudent_list %}
{% if forloop.counter == 1 %}
<div class="peopel-item item active"><p class="peopel-comment">{{stu.comment}}</p>
	<div class="peopel-name">{{stu.name}}</div>
</div>
{%else %}
<div class="peopel-item item"><p class="peopel-comment">{{stu.comment}}</p>
	<div class="peopel-name">{{stu.name}}</div>
</div>
{%endif%}
{%endfor%}
```

#### 课程分类查询  
views.py 的 course  
```python 
category_list = Category.objects.all()
category_id = request.GET.get('category_id')    # 这个 category_id 是从 href 的查询字符串中得到的  
if category_id:
    course_list = course_list.filter(category_id=category_id)    # 实现查询的核心就是这一行，根据前面传进来的 id 去数据库中查    
    category_id = int(category_id)
```
```html
{%for category in category_list %}
{%if category_id == category.id %}    # category.id 是从数据库中取到的  
  <li class="active"><a href="?category_id={{category.id}}" class="text">{{category.title}}</a></li>
{%else%}
  <li><a href="?category_id={{category.id}}" class="text">{{category.title}}</a></li>
{%endif%}
{% endfor %}
 ```
```html
<li {% if request.path == '/' %} class="active" {%endif%}><a href="/" class="main-menu">首页</a></li>
<li {% if request.path == '/course' or request.path == '/course-detail/1' %} class="active" {%endif%}>
	<a href="/course" class="main-menu">课程</a></li>
```

#### 课程详细页面  
不使用 DetailView，而是写函数  
```python 
def course_detail(request, cid):
    course = Course.objects.get(pk=cid)    # 这里不是 course_list，因为只有一篇文章；
                                           # 前端取值直接取就可以了比如星级 {{course.level}}    
    ctx = {
        'course':course,
    }
    return render(request, 'courses-detail.html', ctx)
```
配置 url `path('course-detail/<int:cid>', views.course_detail, name='course-detail')`  
这个 id 是从前面的 HTML 里来的；`<a href="course-detail/{{course.id}}" class="title">{{course.title}}</a>`  
根据 course.id 进入 course_detail 视图函数，然后从数据库中根据特定 id 取到这一篇 course  

取出课程所有的章节 `{% for section in course.section_set.all %}`  

#### 推荐课程  
课程详细页面右侧的推荐课程，不是最新课程  
在 course_detail 视图函数中取值就可以了  
`course_list = Course.objects.filter(recommend=True)[:3]`  

课程详细页面右侧的分类，也可以做查询，前端的路由的写法`<a href="{% url 'course' %}?category_id={{category.id}}">`  

#### 视频播放  
GitHub 搜 videojs  
使用 cdn  
```python
{%block custom_css%}
<link href="http://vjs.zencdn.net/5.19/video-js.css" rel="stylesheet">
{%endblock%}

{%block custom_js%}
<script src="http://vjs.zencdn.net/5.19/video.js"></script>
{%endblock%}
```
```html
<div class="course-video">
    <video id="preview-player" class="video-js" width="847px" height="400px" controls preload="auto" >
    </video>

    <script type="text/javascript">
	var player = videojs(document.querySelector('video'));
	function play_video(url){
	  player.src(url);
	  player.play()
	}
    </script>
</div>

<a href="javascript:play_video('http://localhost:8000/{{video.video}}')">{{video.title}}</a>
```


 
