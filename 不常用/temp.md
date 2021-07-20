
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

