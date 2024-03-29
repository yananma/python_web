
一节课一行笔记，写实现某项功能的关键  

### 常见错误清单  

单词写错了  

缺括号  

Ctrl + Shift + r 清除缓存刷新，很多问题都是因为有缓存，因为 Django 只会自动刷新 Django 后台，而不会更新 HTML 页面  

类中的方法没写 self  

#### 固定步骤  

创建模型，添加到 admin，后台添加数据，在视图函数中，从数据库取值，共享到前端，前端替换     

写完视图函数添加 url   

修改 models.py 以后，要 makemigrations、migrate  

创建应用以后，在 INSTALLED_APPS 中添加  

想法  
是一个具体的东西，就要创建 model，比如合作机构，比如友情链接，这些都是类的实例   

添加数据的本质就是创建一个类的实例  


## Django 基础知识  

Django 是一个重度框架，大而全，适合大型团队管理。学习成本高一些。  

Django 可以做网站开发、微信公众号、小程序后端开发等，只要是有 HTTP 的地方，都可以用 Django  

浏览器本质上就是一个 socket 客户端，就是 TCP。HTTP 建立在 TCP 之上，其实就是 TCP  

HTTP 无状态，短连接。HTTP 是无状态的，本质上就是因为 TCP 连接断开以后，再次连接不知道对方原来是否连接过，所以就有了 cookie 和 session 来解决这个问题  

短连接是 conn.close() 实现的  

浏览器（socket 客户端），GitHub 网站（也就是 web 应用程序）（socket 服务器），服务器先运行起来，会一直监听 IP 和 80，客户端连接以后，客户端发数据，服务器返回响应  

服务器，my_server.py，所有的框架，所有的网站，本质上就是这几行代码    
```python 
import socket

socket = socket.socket()    # 可以读源码  
socket.bind(('127.0.0.1', 8000))
socket.listen(5)

while True:
    conn, addr = socket.accept()  # 阻塞，等待连接
    data = conn.recv(8096)
    print(data)   # 可以看到 HTTP 报文  
    conn.send(b'HTTP/1.1 200 ok\r\n\r\n')   # Chrome 浏览器要加 start line，否则没有办法访问  
    conn.send(b'connect server successfully')
    conn.close()
```

HTTP 协议规定了请求和响应的格式  

网络框架的核心代码  

```python 
import socket
import pymysql

socket = socket.socket()
socket.bind(('127.0.0.1', 8000))
socket.listen(5)


def f1(request):
    '''
    处理用户的请求，返回响应
    :param request: 用户请求的所有信息
    :return: 返回的内容，可以是数据库内容，可以是内存中的 html 文档
    '''
    f = open('index.html', 'rb')  # index.html 可以写登录表单，可以写 table 表格
    data = f.read()  # 后缀名没有任何关系，写什么都可以，写 .myn 都可以
    f.close()  # 静态网站是不变的，动态网站去数据库取值
    return data  # 返回的是字符串，能看到效果，是因为浏览器做了解析


def f2(request):
    f = open('article.html', 'r', encoding='utf-8')
    data = f.read()
    f.close()
    import time
    ctime = time.time()  # 这是自己生成的动态数据，数据完全可以是从数据库取的数据
    data.replace('@@myn@@', str(ctime))  # 就完成了动态替换，模板里放的是占位符，完成占位符替换
    return bytes(data, encoding='utf-8')


def f3(request):
    conn = pymysql.connect(host='127.0.0.1', port=3306, user='root', passwd='123', db='user')
    cursor = conn.cursor(cursor=pymysql.cursor.DictCursor)
    cursor.excute("select id, name, password from userinfo")
    user_list = cursor.fetchall()
    cursor.close()
    conn.close()
    print(user_list)
    content_list = []
    for user in user_list:
        tp = '<tr><td>%s</td><td>%s</td><td>%s</td></tr>' % (user['id'], user['name'], user['password'])
        content_list.append(tp)
    content = ''.join(content_list)

    f = open('user_list.html', 'r', encoding='utf-8')
    template = f.read()  # 前端写了一个 @@content@@
    # 到这里就拿到了两个数据，数据库取的 user_list 和磁盘的 template
    # 要做的把拼接的字符串，替换到前端
    # 这里就是模板渲染，拿到模板和数据，把数据放到模板里
    data = template.replace('@@content@@', content)
    return bytes(data, encoding='utf-8')


def f4(request):
    conn = pymysql.connect(host='127.0.0.1', port=3306, user='root', passwd='123', db='user')
    cursor = conn.cursor(cursor=pymysql.cursor.DictCursor)
    cursor.excute("select id, name, password from userinfo")
    user_list = cursor.fetchall()
    cursor.close()
    conn.close()

    f = open('user_list1.html', 'r', encoding='utf-8')
    data = f.read()
    f.close()

    # 基于第三方工具实现的模板渲染
    from jinja2 import Template
    template = Template(data)
    data = template.render(user_list=user_list)
    return data.encode('utf-8')


# 不配置 url，访问网址，不管后面输入什么，返回的都是同样的内容
routers = [
    ('/index/', f1),
    ('/detail/', f2),
    ('/sql/', f3),
    ('/jinja2/', f4),
]


def run_server():
    while True:
        conn, addr = socket.accept()
        data = conn.recv(8096)
        data = str(data, encoding='utf-8')
        header, body = data.split('\r\n\r\n')
        start_line, header = header.split('\r\n')
        method, url, schema = start_line.split(' ')
        # header 按 ： split，可以取到请求头的信息
        conn.send(b'HTTP/1.1 200 ok\r\n\r\n')
        # 拿到 url，就可以做判断
        func_name = None
        for router in routers:
            if router[0] == url:
                func_name = router[1]  # 就是 path 函数的作用，通过 url 找到视图函数

        if func_name:
            response = func_name(data)  # 这里传了 request
        else:
            response = b'404 not found'
        conn.send(response)
        conn.close()  
# HTTP 短连接，比如打开百度，看到百度页面的时候，其实是没有连接的，因为如果所有的显示都连接，百度的服务器承受不了，看到的只是返回结果
# 短连接就是最后的 conn.close() 实现的，发送完就关闭，实现以后，还是 True，还会在服务端等待连接


if __name__ == '__main__':
    run_server()
```

nginx 就是 socket 服务端  

MTV 核心思想就是解耦，便于开发维护，增加模块的可重用性。  


#### 前期配置  

python manage.py 的所有可用命令都在 django/core/management/commands 文件夹下面  

创建项目：`django-admin startproject mysite`  

配置 MySQL，不用记，代码 settings 里面有网址，复制就行  

创建应用：`django-admin startapp polls`  

添加到 INSTALLED_APPS 中，就是源码中的 app_label    

项目是应用的容器  

BASE_DIR 就是项目文件夹  

STATIC_URL = '/static/' 当 html 前端 link 的 CSS 中有 static 的时候，就会去下面的 STATICFILES_DIRS 中去找 CSS 文件  

STATICFILES_DIRS 必须叫 STATICFILES_DIRS，这个名字是在 global_settings.py 中定义的  

MEDIA_ROOT 上传文件路径  

创建模型，继承自 models.Model，添加一些字段  

生成迁移表：`python manage.py makemigrations polls`  

查看 SQL 语句：`python manage.py sqlmigrate polls 0001`  

迁移到数据库：`python manage.py migrate`  


#### 模型操作  

模型是你的数据的唯一的，权威的信息源，包含所存储的必要字段，一个模型对应数据库中的一张表，一个字段对应于数据表中的一列  

Django ORM 可以用相同的接口操作不同的数据库，做了底层封装；更加安全；易读性更高；不用因为修改数据库而修改代码  

ORM 做的事情就是把 Python 类，拼接成 SQL 语句  

每个字段都是 Field 子类的实例，比如 username = models.CharField() username 就是 CharField 的实例；每个字段都是模型的类属性    

在 model.py 的模型类中，class Meta 的 verbose_name，是类显示的名字，是点进去之前显示的。  

def \_\_str__(self)，是点进去以后实例显示的内容  

字段的 verbos_name 是再点进去编辑的时候，左侧显示的名字  

DateField 日期、DateTimeField 时间、auto_now_add 创建时间、auto_now 修改时间   

修改属性：模型对象.属性 = 新值，然后 save()  

除了关联关系之外，一般第一个属性都是字段的自述名，就是 verbose_name  

max_length 是 CharField 的必填字段，在 \_\_init__方法中有一个 MaxLengthValidator 验证    

filter 内部有多个过滤条件的时候，是 AND，filter 不能实现 OR，如果想要实现，就要用 Q  

filter(类，子类), filter 内部是拼接 WHERE 语句，是与的关系  

关联关系：多对一、一对一、多对多  

ForeignKey，Comment 中的 ForeignKey 是 Blog，所以 Comment 直接就有 Blog 字段，所以取值的时候直接取，comment.blog.title  

Blog 中没有 Comment 字段，所以取的时候是反向查询，blog = Blog.objects.get(id=1)，blog.comment_set.all()，其中 comment_set 是自动添加的查询管理器  

大部分的展示信息，都是用的 `模型类.objects.all()`  

关联信息会用到反向查询和关联关系查询，对于 ForeignKey，ForeignKey 写在一对多的那个多的类中，比如 Topic 和 Comment，写在 Comment 类里，因为添加 Comment 必须要有 Topic，但是添加 Top 不用写 Comment。查询的时候，Topic 中没有 Comment 字段，所以用的是反向查询，自动添加了 comment_set 查询管理器，Topic.comment_set.all()。Comment 中有 Topic 字段，查询的时候直接查就可以，在前端可以通过 comment.topic.name 取值。  

比如通过标签查博客，先通过标签 id 取到特定标签，然后通过反向查询 Tags.blog_set.all() 取到所有有这个标签的 blog  

进入 shell 环境：`python manage.py shell`  

model 操作 API，创建一个实例，save()、filter()、get()、delete()、update()、  


#### 后台管理  

Django 相较于其他的框架的一个大的优势就是有一个功能完善的后台系统，不用从头搭建  

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
admin.site.site_title
admin.site.index_title
django/contrib/admin/templates/admin/base_site.html，在文件夹下面有很多 HTML 页面  


#### 视图  

先写 url，然后写视图函数  

浏览器找的时候是通过 url 找到 urls.py，从 urls.py 的配置中找到 views 函数，通过 views 函数返回响应  

路由列表必须叫 urlpatterns，因为源码里是 `getattr(urlconf_module, 'urlpatterns')`  

views 后面接函数名，不加括号是函数，加括号是函数的返回值；  

继承 View 类的时候，as_view() 加括号，加括号源码最后返回的是 as_view 内部定义的 view 函数，是 get 就走 get，是 post 就走 post，所以还是函数  

跳转到详细页面，移除硬编码，可以使用 `{% url 'detail' question.id %}`，这里单引号里的 detail 是 path 里面的 name  

在 View 函数中第一句做一个验证，`question = get_object_or_404(Question, pk=question_id)`  

`selected_choice = question.choice_set.get(pk=request.POST['choice'])` ['choice'] 中的 choice 是表单里的 name，前端代码是：`<input type="radio" name="choice">`  

request.POST 得到的就是一个 QueryDict，就是一个字典，[''] 就是字典取值，key 就是前端表单的名字，value 就是表单提交内容，一般用 get() 方法取值，这个 get 是 QueryDict 的父类 MultiValueDict 的方法，`get(self, key, default=None)`   

在走 POST 方法的时候，print(request.POST) 就全部看清楚了  

GET 获得请求头，请求体没有数据；POST 获取请求体内容，

request.GET 最重要的功能就是取 url 中的 query_string 的键比如 ?wd=python 中的 wd 和表单中的 name  

最后返回，`HttpResponseRedirect(reverse('result'))` 这里 result 也是 path 里面的 name，会根据 url 配置找到 result 视图函数  

HttpResponse(字符串)，HttpResponse 返回字符串，写的是内容；  
render 返回的才是模板，是模板路径，render 源码用的就是 HttpResponse。  
redirect 返回跳转地址  

所有的重定向都是浏览器完成的，Django 只是在响应头中加上一个 LOCATION 和要跳转到的地址  

HTTP 生命周期：请求头 --\> 提取 url --\> 路由关系匹配 --\> 视图函数(模板 + 数据进行渲染) --\> 返回给用户(响应头)  

类视图 TemplateView，使用非常简单  
```python 
class IndexView(TemplateView):
    template_name = 'hello.html'  
```


#### 模板  

要看是不是要有一个新的页面，如果是一个全新的页面，比如 vip 页面，就要添加一个 html 模板，然后要添加视图  

变量：{{ }}  
标签：{% if 或 for、url、block、extends、include %}  
过滤器：读源码最容易  

理解模板继承的时候，想象中应该是把 base.html 的内容拿到当前的模板文件中，然后结合 {% block %} 部分  

登录的视图函数中，写的是 `return render(request, 'login.html', {'error_msg':'用户名或密码错误！'})`  

前端 html 页面写的是 `<h3 style="color:red">{{error_msg}}</h3>` 所以就是一个简单的 {{ }} 变量替换  

`choice{{ forloop.counter }}` 拿到 choice1，choice2，choice3  

可以用数字索引查询，{{ item.0 }}、{{ item.1 }}  

删除功能 `<a href=/del/?nid={{ item.id }}>删除</a>`，在循环体中，点击哪个 id，就跳转到哪个页面  


#### 表单  

浏览器提交内容就要用到表单  

action 是表单内容提交的地址    

有三种方式：  
第一种是使用 HTML 的表单，视图函数中使用 request.POST.get('username') 取值    
第二种是 LoginForm(request.POST) 
第三种是使用 Django 的 form 表单系统。在 forms.py 中定义 form，然后在 views.py 中 import form 类，在视图函数的 get 方法中第一行先实例化，然后把 form 实例 render 到前端，在模板中使用 {{ form }}，最后生成的 form 不是 HTML 写的 form，是 Django forms.py 生成的 form，然后走 POST 方法的时候，再做验证。这种方法取值的使用用的是 clean_data 取值，关于 clean_data 读源码     
form 表单提交，页面就会刷新，刷新，提交表单就会消失，想要不刷新，就要用 ajax  

添加了 `{% csrf_token %}` 以后，提交表单，使用浏览器检查，就可以看到生成了一个 input 标签，type=hidden，name='csrfmiddlewaretoken'，value='一串随机数字'，后面就是根据这个取值验证。这部分内容是在请求体中，而不是请求头中   

ajax 绕过了表单  


#### 用户  

user 的方法和属性都在 django/contrib/auth/models.py 的 AbstractUser 和它的父类 AbstractBaseUser 中，比如 username、is_active，比如 is_authenticated  


#### 路由  

写路由配置，最后应该加上一个 /，因为不加会有一个重定向，会加上以后跳转    

路由就是给谁，路由本质上就是正则匹配  

一种是 http://127.0.0.1:8000/edit/?nid=fff 

path('edit', ...)

这种取值用的是 request.GET.get(nid)  

一种是 http://127.0.0.1:8000/edit/fff 

path('edit/<int:nid>', ...)  

这种在视图函数中要传入 id  

前端写的时候，比如 a 链接，也不加问号，而是 href='edit/{{nid}}'  


#### 中间件  

5 个方法  

权限  
用户登录验证  
黑名单/白名单  
csrf_token  

csrf_token 是在 process_view 中实现的，因为要走到视图函数，看有没有 csrf_exempt 装饰器  

AOP Aspect Oriented Programming 面向切面编程。AOP 的目的主要是针对业务处理过程的切面进行提取，它所面对的是处理过程中的某个步骤或阶段，以获得逻辑过程中各个部分之间低耦合的隔离效果。  

写 middleware 中间件，继承 MiddlewareMixin，在 settings 中注册  


#### 缓存  

统计功能：IP 统计、浏览器统计  

实现权重控制，返回的概率不一样，if random.randrange(100) > 20 或 > 80 实现  

黑名单/白名单  

实现反爬虫，实现频率控制，比如 10 秒之内只能访问一次  
```python 
if request.path == '/app/search/:
     result = cache.get(ip):
     if result:
         return response('请 10 秒后访问')
     cache.set(ip, ip, timeout=10)
```

将执行的操作数据存储下来，在一定时间内，再次获取数据的时候，直接从缓存中获取。从而提升服务器响应速度。  

比较理想的方案是使用内存缓存。速度快上万倍  

`python manage.py createcachetable`  

缓存配置和数据库配置格式差不多  

缓存在视图函数中使用最多   

@cache_page()  

视图函数先取缓存中查数据，如果缓存中没有才去数据库中查，去数据库中查到数据以后，还有存在缓存中  

不用装饰器  
cache.get() 取值  
cache.set() 存值  

可以使用 Redis 实现缓存功能  

黑名单，用 cookie 和 session，就是一个 if 判断，if ip == '黑名单 ip' 就 return HttpResponse('字符串')   


#### 分页

分页属于优化加载  

分页就是分批获取数据  

本质就是切片  
Blog.objects.all()[0:10]  
Blog.objects.all()[10:20]  

Django 自带分页，`from django.core.paginator import Paginator, Page`  

Paginator 是分页器，Page 是某一个页面  

`paginator = Paginator(blog_list, per_page=10)`  

paginator 自带一些方法，看源码，比如 count 对象总数，num_pages 总页数，page_range 页码列表    

比如 current_page_posts = paginator.page(第几页)，会显示一个页面  

current_page_posts 也自带一些方法  

因为 paginator.page() 调用了 \_get_page 方法，而 \_get_page 方法就是返回 Page()，所以就继承了 Page 的方法，比如 has_next、has_previous、object_list 等  

object_list 是当前页面的所有数据  

视图函数：
```python 
current_page = request.GET.get('page')  
current_page = int(current_page)  
blog_list = Blogs.objects.all()  
paginator = Paginator(blog_list, per_page=10)  
current_page_posts = paginator.page(1)   # paginator.page(显示第几页)  
ctx = {'posts':current_page_posts}
```

前端 html  
```html
<body>  
    <h1>用户列表</h1>
    <ul>
    {% for row in posts.object_list %}
	    <li>{{ row.name }}</li>
    {% endfor %}
    </ul>
    <div>
        {% if posts.has_previous %} 
	    <a href='/index.html?page={{ posts.previous_page_number }}'>下一页</a>
	{% endif %}
	{% for page_index in page_range %}  
	    <li><a href="{% url 'app:students_page' %}?page={{ page_index }}">{{ page_index }}</a></li>
	{% endfor %}    
	{% if posts.has_next %} 
	    <a href='/index.html?page={{ posts.next_page_number }}'>下一页</a>
	{% endif %}
    </div>
</body>	
```

用 Bootstrap 样式，先搜 Bootstrap cdn 和 jQuery cdn，导入，然后复制 Bootstrap 样式  

1: 0-10  
2: 10-20  
3: 20-30  
start = (current_page - 1) * per_page
end = current_page * per_page  


#### 验证码  

要用 Pillow 库  

自己绘制也很简单，一个坐标系，左上角开始，向右是 x 轴，向下是 y 轴，然后要有一块画布，一支画笔。  

Image 是画布，ImageDraw 是画笔，ImageFont 是字体  

```python 
def get_code(request):
    mode = 'RGB'  
    size = (200, 100) 
    color_bg = (255, 0, 0) 
    image = Image.new(mode=mode, size=size, color=color_bg) 
    image_draw = ImageDraw(image, mode=mode)  
    image_font = ImageFont.truetype(settings.FONT_PATH, 50(字号))
    image_draw.text(xy=(0, 0), text='Rock') 
    fp = ByteIO() 
    image.save(fp, 'png') 
    return HttpResponse(fp.getvalue(), content_type='image/png')
```
设置随机字符串，随机颜色，随机线条，随机噪点

找一份字体，配置路径  

用 session 存储生成的验证码，做验证  
```python 
receive_code = request.GET.get('verify_code') 
store_code = request.session.get('verify_code') 
if receive_code.lower() != store_code.lower():
    return redirect(reverse('app:login'))
return HttpResponse('登录成功')
```

用 jQuery 实现点击验证码刷新功能  
```js
$(function) {
    $("img").click(function ()) {
        $(this).attr("src", "app/getcode/?t=" + Math.random());   // 不加 random，浏览器就不会刷新  
    }
}
```


#### 富文本  

就写博客有用，干别的用不着  

富文本就是添加样式的文档，就是添加 HTML 标签  

`pip install tinymce`  

在 settings 中配置路径  

配置 url，配置函数，在 HTML 中引入 js，并且初始化  



## 留言板项目  

视图函数全部都是使用 View 创建的，读完就学会 View 类写视图了  
[models.py](https://github.com/yananma/python_web/blob/main/%E4%B8%8D%E5%B8%B8%E7%94%A8/Django%20%E9%A1%B9%E7%9B%AE/%E7%95%99%E8%A8%80%E6%9D%BF/models.py)、[forms.py](https://github.com/yananma/python_web/blob/main/%E4%B8%8D%E5%B8%B8%E7%94%A8/Django%20%E9%A1%B9%E7%9B%AE/%E7%95%99%E8%A8%80%E6%9D%BF/forms.md)、[views.py](https://github.com/yananma/python_web/blob/main/%E4%B8%8D%E5%B8%B8%E7%94%A8/Django%20%E9%A1%B9%E7%9B%AE/%E7%95%99%E8%A8%80%E6%9D%BF/views.py)  

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
先在 models.py 创建 Comment 模型  
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
<form name="comment-form" action="/comment/{{post.id}}/" method="POST">  # 核心是这里的 action  
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
		request.session['user_id'] = user.id    # 这里的 session 是为了保持登录状态，不至于每次都重新登录。  
		request.session['username'] = user.username		
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

使用函数实现  
```python 
def my_logout(request):
    logout(request) 
    return HttpResponseRedirect(reverse("index"))
```

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


#### 修改评论  

在 forms.py 中写验证表单  

```python 
class CommentForm(forms.Form):
    comment_text = forms.CharField(widget=forms.Textarea(attrs={'placeholder':'请输入评论',
                                                                'id':'comment_text',
								'class':'form-control form-input'}))
```
定义视图  

在 blog_detail 视图函数中实例化 form，并且共享到前端页面 `form = CommentForm()`  

前端没有实现 {{ form }}，还是用的 html 的表单，这种不用 Django 表单验证的方式不太好，不过这里主要是理解思路  
```python 
def comment_update(request, id, bid):
    form = CommentForm()
    comment = Comment.objects.get(id=id)
    blog = Blog.objects.get(id=bid)
    if request.method == 'GET':
        ctx = {
        'comment':comment,
        'form':form,
        'blog':blog,
        }
        return render(request, 'comment_update.html',ctx)

    if request.method == 'POST':
        comment.user = request.user
        comment.blog = Blog.objects.get(id=bid)
        comment.content = request.POST.get('comment_text')
        comment.pub_date = datetime.now()
        comment.save()
        return HttpResponseRedirect(reverse("blog-detail",kwargs={'bid':bid}))
```

#### 删除评论  

```python 
def comment_del(request, id, bid):
    comment = Comment.objects.get(id=id)
    comment.delete()
    return HttpResponseRedirect(reverse("blog-detail",kwargs={'bid':bid}))
```

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
部署的时候要改一下网址  
<a href="javascript:play_video('http://mayanan.top/{{video.video}}')">{{video.title}}</a>
```



### 首页

配置路由和视图   

移动端，最下面有 4 个选项，其实就是 4 个页面，配置 4 个路由，对应的视图函数，创建对应的模板和静态文件  

移动端和网页端的最大的区别就是 CSS 中宽高大小的值  

轮播图  
轮播图是用容器装图片，然后写 js 代码，让容器移动实现的  

页面布局  
前端传的数据，85% 都是 json 格式  

### 商品页面  
先设计表结构，然后创建模型  

分为类别和商品展示两大类  

实现通过类别查询商品  
先取商品类别，`category = Category.objects.get(pk=cid)`  
然后根据类别取得这个类别所包含的商品：`product_list = category.product_set.all()`  

子类查询，比如查询饮料分类中的汽水，用 filter(类，子类), filter 内部是拼接 WHERE 语句，是与的关系  

商品排序  
比如按照价格由高到低、由低到高、距离远近、评分高低等排序  
在商品字段中有一个 sort_id 字段，在视图函数中写判断：  
```python 
if sort_id == '1':
    product_list = Product.objects.order_by('price').all()  
if sort_id == '2':
    product_list = Product.objects.order_by('-price').all()  
...
```

点击加号，往购物车添加商品的时候，本质上就是把当前商品的 id 发给服务器。  



## 爱鲜蜂项目  

先设计表，表的字段，表的关系  

先完成主要功能，走通流程，再优化细节  

版本迭代，不要一次增加太多功能  

接口就是路由  

#### 设计分析  

主页面显示：最简单，数据查询显示  

商品数据展示：级联查询，排序  

用户系统：是业务的核心系统，只要有用户，别的都好说；腾讯做事容易做成，并不是产品做得好，而是用户来的快。  

购物车系统：商品和用户的关系；订单系统，购物车数据转换成订单；支付系统，很简单就是接口调用。  

扩展：地址管理系统，积分系统，会员级别系统，评价系统，优惠券系统，数据安全，过滤器，反爬，权限  

部署：动静分离部署  


#### 项目搭建 

开发流程：基本工程搭建，前端静态页面搭建，Model to DB，业务逻辑开发，前后端协同开发    

在应用中创建 urls.py 

创建静态文件夹 static，添加文件，css、js、fonts、img、uploads  

创建 base.html，title 设置变量，引入 CSS 和 JS，

前端配置，推荐百分比而不是固定尺寸，因为屏幕各种尺寸都有  

适配单位  
* px  
* em，默认相对于父级元素，默认大小 1em=16px  
* rem，默认相对于根元素，r 代表 root，默认大小 1rem=16px  

先创建 4 个 HTML 页面，配置 4 个路由  

切换页面的时候，底部不发生变化  

用 swiper 实现轮播图，用法看官网  

安装 django-debug-toolbar，按照官网教程说明配置  

django-debug-toolbar 拥有极强的调试功能，提供了各种信息的获取  

首页就是页面展示  


#### 闪购页面  

闪购，也就是 filter、exclude，还有 order_by  

商品应该有商品 id，数字排序更方便  

先创建表，迁移到数据库，插入数据  

要创建两个 model，一个是 category 表，一个是 product 表，product 表中添加 category_id 字段，设置 ForeignKey 关联 category  

然后在 views.py 中查询数据  

查询数据的时候，视图函数中传输 category 的 id  
```python
def product(request, cid):
    product_list = Product.objects.filter(category_id=cid)  
```    

前端在 a 链接中添加标签。  
`<a href="{% url 'axf:product' category_id=category.id %}"</a>`  

左侧是大类型，右侧上方为小类型，大类型和小类型之间是一对多的关系。   

二级查询的时候，先进行一级查询，然后再在一级查询的基础上进行一次查询。SQL 语句就是先根据一级分类 id 查询，然后再 AND 二级分类 id 查询。    

一级查询： `category_list = Category.objects.all()` `category = Category.get(category_id=cid)`  
二级查询：`second_category = category.second_category_names`，然后先按照 \# 进行 split，得到一个列表，再按照 : 进行 split，得到二级分类的名称和 id，然后把列表共享到前端，前端就可以取到二级分类的名字了。
而查询，则是因为在数据表中，有一个字段就是二级分类的 id，根据这个 id 就可以进行查询。  

函数参数要再传入一个二级查询 second_category 的 id，sid，前端的 a 链接查询的时候，后面也是要跟两个 id  
```python
def product(request, cid, sid):
    product_list = Product.objects.filter(category_id=cid).filter(second_category_id=sid)    
```    

上面这种做法，查询子类是可以的，但是在查询全部分类的时候，就会什么都查不到，所以还要进行一个判断，如果是全部分类的查询，就不进行二级查询。  

```python
def product(request, cid, sid):
    ALL_TYPE = '0'
    if sid == ALL_TYPE:
        product_list = Product.objects.filter(category_id=cid) 
    else:
        product_list = Product.objects.filter(category_id=cid).filter(second_category_id=sid)    
```    

前端查询的时候，点击全部分类，把向下的箭头改成向上的箭头，用 jQuery 实现。  
`$span.removeClass("glyphicon-chevron-down").addClass("glyphicon-chevron-up")`  

前端应该做一个判断，在全部分类点开以后，应该是选中的才是 active，没选中的就是平常的颜色，办法就是根据 id 判断，如果等于 id 就 active  

综合排序，里面是有多种选择条件的，办法就是在视图函数中做多次判断，视图函数中要传入一个 order_id，oid，然后把排序情况赋值为数字，如果 oid 等于某一个条件的 id，就按某一种方式 order_by。  


#### 用户页面  

先要设计表结构，用户包括 username、password、email、phone、thumbnail、is_active、is_deleted  

定义 AXFUser，直接继承自 models.Model  

在 bootstrap 上找登录注册的样式  

然后在视图函数中做判断，如果 method 是 POST 的时候，从前端拿到这些属性的值，然后实例化一个 user，属性赋值，最后 save()。  

用户名设置了 unque=True，如果输入了相同的用户名，提交以后就会报错。不过这种方案不好，因为这个不应该是后台判断的。因为想用户名想了半天，写了邮箱密码等很多其他的表单，最后报错，体验非常不好，应该再前端进行判断。  

应该是自动触发查询，应该是内容改变之后，而不是失去焦点之后更好。  

```js
$(function) {
    var username = $("$username_input").trim().val();  
    username.change(function(){
        if (username.length){
            $.getJSON(
                '/axf/check_user/', 
                {'username': username}, 
                function(data) {
                    var username_info = $('#username_info')
                    if(data['status] == 200){
                        username_info.html('用户名可用').css('color': 'green')
                    }else{
                        username_info.html('用户名已被占用').css('color': 'red')
                    }
            })
            
        }
    })
}
```

然后添加 check_user 的 url，写 check_user 函数。  
```python 
def check_user(request):
    username = request.GET.get('username')  
    user = AXFUser.objects.get(username=username)  
    data = {} 
    if user.exists:
        data['status'] = 自己创造一个号码，和前端协商好  
        data['msg'] = '用户名已被占用'  
    return JsonResponse(data=data)         
```

如果用户名已经存在，那么注册功能应该是不可用的。在 form 中添加 onsubmit 属性，`onsubmit="return check()"`  

然后再 js 文件中写 check 函数  
```js
function check() {
    var info_color = $('#username_info').css('color'); 
    // console.log(info_color)  
    if (info_color == 'rgb(255, 0, 0)'){
        return false 
    }
    return true 
}
```

没有输入用户名的时候，也不能注册，办法就是获取 username，如果为空，return false。输入两次密码，也是这么验证。  

密码要加密，如果不加密，后台是可以看见的，如果员工复制了密码跑了，就有大麻烦了  

用 Django 自带的 make_password  

验证密码  
```python 
user = AXFUser.objects.get(username=username)  
if user.exists():
    if check_password(password, user.password): 
        request.session['user_id'] = user.id 
        return redirect(reverse('index'))  
    else:
        return redirect(reverse('axf:login'))  
```

版本升级以后，密码策略不兼容问题。比如第一版是明文，第二版是哈希，第三版是哈希加时间戳。兼容办法就是加版本号，然后做判断。   

然后写一个个人中心页面的视图函数。  

`user_id = request.session.get['user_id']`  

注销的时候清空 session  

`request.session.flush()`  

用户激活认证，一般而言有三种方式，邮件激活、短信认证、人工审核。  

发送邮件，看官网教程。  

send_mail() 函数，有一个必填参数 message，是个占位参数，内容可以随便写，但是必须要有；使用 html_message 传递要发送的内容。  

send_mail() 函数在 `/django/core/mail/__init__.py` 中   

写一个激活 html 页面，把页面 render 以后，传到 html_message 中发送过去。  

链接中存在用户唯一标识，把 token 作为键放到缓存中，值为 user_id  

token 用 uuid 生成：`token = uuid.uuid4().hex`  

要在 settings 中配置 CACHE，格式和 MySQL 的配置差不多。  

设置缓存：`cache.set(token, user_id, timeout=60 * 60 * 24)`  

激活函数   
```python 
def active(request):
    token = request.GET.get('token') 
    user_id = cache.get(token)  
    if user_id:
        cache.delete(token)    # 验证链接，只能使用一次  
        user = AXFUser.objects.get(pk=user_id)  
        user.is_active = True 
        user.save() 
        return redirect(reverse('axf:login'))  
    return render(request, 'axf/active_fail.html')  
```

错误信息提示，因为有好几个错误都会 redirect 到 login 页面，如果没有错误提示，就不知道是那种错误造成的，用户体验非常不好。  

要把错误信息保存到 session 中  
要在错误显示页面获取错误信息  
保证错误信息只能出现一次  
获取数据后，删除 session 中的错误信息。`del request.session['error_message']`  


#### 购物车页面  

购物车页面比较复杂，如果这个可以弄明白，那么在工作中的很多业务都可以完成。  

要先设计表，把表结构理清了，后面就容易多了  

购物车中用户和商品是多对多关系  

多个已购商品最后变成一个订单，用的是 ForeignKey  

```python 
class Cart(models.Model):
    c_user = models.ForeignKey(AXFUser)  
    c_goods = models.ForeignKey(Goods) 
    c_goods_num = models.IntegerField(default=1) 
    c_is_selected = models.BooleanField(default=True) 
    
    class Meta:
        db_table = 'axf_cart'  
```

商品加入购物车，点击加减号，先写 JavaScript 代码，先获取元素，然后添加点击事件，先不写逻辑代码，而是先写 console.log()，验证 click 事件是否成功。  

添加商品，要获取用户，知道是哪个用户买的，然后获取商品，知道用户买的是哪个商品，把这两个结合起来就是一个购物车数据；还要判断是否还有库存。  

点击加号的时候，要获取商品 id，前端获取商品 id，在 add 和 sub 的属性中添加 goods_id 属性。`goods_id = {{ goods.id }}`，然后获取商品 id  
```js 
var add = $(this);  
add.attr('goods_id')    # jQuery 获取对象属性，attr 是可以获取所有属性  
// add.prop('goods_id')    # prop 只能获取内置属性  
```

在后台取值的时候，应该是两个过滤，先根据 user 进行 filter，后面再根据商品 id 就行 filter  

购物车页面设计  

添加到购物车的商品，点击减号的时候，要先根据 id 取到商品，然后数量减 1，如果没有了，就删除这个商品，把信息通过 JsonResponse 共享到前端，前端用 ajax 实现。  

```python 
def sub_shopping(request):
    cart_id = request.GET.get('cart_id')  
    cart_obj = Cart.objects.get(pk=cart_id)  
    data = {'status': 200, 'msg': 'ok'}  
    if cart_obj.c_goods_num > 1:
        cart_obj.c_goods_num -= 1 
        cart_obj.save() 
    else:
        cart_obj.delete()  
    return JsonResponse(data=data)  
```

购物车全选逻辑：  
默认状态：全选按钮是选中的，那么所有商品都是选中状态；全选按钮未选中，内部商品只要存在未选中的，全选就应该是未选中  
点击全选：原状态是选中的，全选和所有商品都变成未选中；原状态是未选中，全选和所有商品都变成选中。  
点击单个商品：商品由选中变成未选中，全选一定变成未选中；商品由未选中变成选中，则全选的默认状态是未选中，全选有可能变成选中  

价格，每一次添加或删除一个商品以后都要重新算一遍，计算价格是后端完成的。    

订单页面要创建一个订单的url 和 html 页面。  

会有 Python 的小数点的问题，比如 3 个 9 块，总价 price 会是 27.00000003  

办法：`'%.2f' %price` 或 `"{:.2f}".format(price)`  

支付就是调用接口  
读支付宝文档  

去 GitHub 搜 python-Alipay-sdk  


#### Nginx  

Nginx 可以直接访问静态文件，这时候就是 HTTP 服务器  

如果 Nginx 只是转发请求，那么就是反向代理服务器  

可以通过系统管理 systemctl 来开启 Nginx，但是不推荐这种方式，因为这种方式不会加载配置文件，会出很多奇怪的错误。  

Nginx 的核心就是配置文件  

Nginx 的配置文件非常简单  

Nginx 配置文件结构  

    main    全局设置  

    events {    工作模式，连接配置  
        ......
    }

    http {    http 配置  
        ......
        upstream xxx {    负载均衡配置  
            ......
        }
        server { 主机配置
            ...... 
            location xxx {    静态文件 url 配置  
                ...... 
            }
        }
    }


location 实现动静分离，其实就是 url  

    location /static {

    }

就是访问 url 包含 static 的时候，会访问内部的内容  

部署其实也很简单的，Nginx 和 uwsgi 的配置和命令都极其简单，没有任何难度  

通用的方向代理参数是 proxy_pass，对于 uwsgi 可以是用 uwsgi_pass，因为 uwsgi 和 Nginx 有合作，做了特定的优化  

gunicorn 的使用也非常简单，`gunicorn --help` 看参数  

阿里云：安装软件，配置环境，配置安全组  

可以使用 PyCharm 远程连接阿里云  

可以使用百度统计，友盟统计查看网站访问数据  

### RESTful  

REST Representational State Transfer 表现层状态转移，这里省略了主语，主语是资源 resource，资源的表现层状态转移  

PyCharm -> Tools -> HTTP Client -> Test RESTful Web Service 可以做简单测试     

主要的工具还是 Postman  

```python 
def index(request):
    data = {
        'status': 200,
        'msg': 'ok',
    }

    return JsonResponse(data=data)
```

大体上都是这种结构  

#### serialization

自己写，最麻烦的就是转换成 JSON 数据，数据多的时候，非常繁琐，所以要使用 Django REST framework，而且 serialization 是 Django REST framework 的核心    

Django REST framework 是基于 Django 的重量级框架，可以自己开发网站  

serialization 是 Django REST framework 的核心  

serialization 就是把模型数据编程 json 格式  

model 指定模型  

fields 指定字段   

有简洁的页面，可以点击 get、post、delete 等等，非常方便，自己写的话，要写视图函数，视图函数中要写各种方法  

写的顺序：model、serializer、views、urls  

serializer.Serializer 手动序列化，手动添加 serializers.CharField()，自己写 create()、update() 方法  

```python 
class SnippetSerializer(serializers.Serializer):
    id = serializers.IntegerField(read_only=True)
    title = serializers.CharField(required=False, allow_blank=True, max_length=100)
    code = serializers.CharField(style={'base_template': 'textarea.html'})
    linenos = serializers.BooleanField(required=False)
    language = serializers.ChoiceField(choices=LANGUAGE_CHOICES, default='python')
    style = serializers.ChoiceField(choices=STYLE_CHOICES, default='friendly')

    def create(self, validated_data):
        """
        Create and return a new `Snippet` instance, given the validated data.
        """
        return Snippet.objects.create(**validated_data)

    def update(self, instance, validated_data):
        """
        Update and return an existing `Snippet` instance, given the validated data.
        """
        instance.title = validated_data.get('title', instance.title)
        instance.code = validated_data.get('code', instance.code)
        instance.linenos = validated_data.get('linenos', instance.linenos)
        instance.language = validated_data.get('language', instance.language)
        instance.style = validated_data.get('style', instance.style)
        instance.save()
        return instance
```

serializers.ModelSerializer  
```python 
class SnippetSerializer(serializers.ModelSerializer):
    class Meta:
        model = Snippet
        fields = ['id', 'title', 'code', 'linenos', 'language', 'style']
```

JSONParser().parse() 源码中做的事情就是 json.load()  

serializer.data 是字典格式  

`content = JSONRenderer().render(serializer.data)` 把字典格式转化成二进制 bytes，源码是 `return bytes(ret.encode('utf-8'))`   

设置 `many=True` 可以序列化多个对象  


#### Requests 和 Responses  

Django REST framework 封装了 Django 的 request 对象，增加了功能，原来是 request.POST，现在使用 request.data 更好，同时兼容 POST、PUT、PATCH，request.data 方法的核心是 \_load_data_and_files 方法，这个方法的作用是 Parses the request content into self.data.     

APIView 弄明白了，Django REST framework 就理解的差不多了，把 APIView 源码流程给面试官讲一遍，工作基本上就有了。  

核心就是 dispatch() 方法  

默认配置在 rest_framework 的 settings.py 中，如果自己在 Django 的 settings 中设置了 REST_FRAMEWORK 那就会替换默认的 setting，读源码可以看到，在 reload 方法中    

APIView 的 dispatch 方法中，有一个 initialize_request()，在这个方法中，给 request 添加了一些特性  

dispatch 方法中还有一个 initial 方法，执行了认证、权限和限流操作  

其中认证函数 `perform_authentication()` 的内容就是 request.user，这个 user 就是 Django REST framework 的 user 方法，加了 @property 装饰器，内容就是验证，验证方法是 \_authenticate() 方法，这个方法的作用就是遍历认证器，认证成功返回一个元组，元组的第一个元素就是 user，第二个元素就是 auth，也就是 token。    

check_permissions() 方法会遍历权限检测器，只要有一个不满足，就调用 permission_denied() 函数，拒绝访问，

check_throttles() 方法和上面的道理是一样的，如果没有通过就 wait  

所以 Django REST framework 的 dispatch 方法比原来的 dispatch 方法要强大很多。  

as_view() 方法中最后返回 csrf_exempt(view)，所以 APIView 的所有子类都是 csrf_exempt 的  

response 也是封装的 Django 的 response  

状态码都在 rest_framework 的 status.py 中  

APIView 的子类都在 generic.py 中，有：GenericAPIView、CreateAPIView、ListAPIView、RetrieveAPIView、DestroyAPIView、UpdateAPIView 等等，这些的实现都很简单，读源码就可以理解，不过基本的都要再往深读一层，才能看到具体功能的实现。  

ModelViewSet 继承了所有的方法，是封装功能最多的  

#### celery  

读官方文档  

celery 消息队列：异步任务；定时任务  

RabbitMQ 是一个容器  

Redis 有三大功能：数据存储、缓存、消息队列  

耗时操作  

定时请求，比如证券行情，比如天气的温度  

celery，1) 把耗时任务放到 celery 中执行；2) 定时请求  

任务：就是一个 Python 函数  

队列：要执行的任务  

工人：执行任务  

代理：代理负责调度，部署环境中，一般使用 Redis  


创建任务  
```python 
from celery import Celery

app = Celery('tasks', broker='pyamqp://guest@localhost//')

@app.task
def add(x, y):
    return x + y
```    

运行：`celery -A tasks worker --loglevel=INFO`  

异步任务调用 delay 方法就可以了  

[在 Django 中使用 celery 文档](https://docs.celeryproject.org/en/stable/django/first-steps-with-django.html)  



 
