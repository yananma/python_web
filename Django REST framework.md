
不同设备，不同的前端样式，共用一套后端  

Django REST framework 在 Django 的基础上，去掉了模板的部分，提供了一个 REST 接口  

url -> views -> models 数据库取值 -> serializer 序列化成 json 格式 -> 返回响应到浏览器  

REST API pretty works like web does，是在网络中 client 和 server 的一种交互形式，server can receive data from applications，可以是电脑端、iOS 和 Android，allows one software talk to another  

方法：写项目，读源码  


## Django REST framework 使用与源码分析  


#### RESTful 规范  

REST 全称是 Representational State Transfer，中文意思是表述性状态转移。  

遵守统一的 RESTful API 规范，对于前端和后端都会非常方便，在 url 中就包含了操作信息  

要实现增删改查，就要有 4 个分别对应的 url  
RESTful 规范建议使用 1 个 url，通过方法实现增删改查的功能，比如 if request.method == 'GET' 等判断  

API 与用户的通信协议，总是使用 HTTPs 协议。  

域名  
`https://api.example.com`                         尽量将 API 部署在专用域名 （会存在跨域问题）  
`https://example.org/api/`                        API 很简单  

版本  
URL，如：`https://api.example.com/v1/`  
请求头                                                  跨域时，引发发送多次请求  

路径，视网络上任何东西都是资源，均使用名词表示（可复数）  
`https://api.example.com/v1/zoos`    
`https://api.example.com/v1/animals`    
`https://api.example.com/v1/employees`    

method  
GET      ：从服务器取出资源（一项或多项）  
POST    ：在服务器新建一个资源  
PUT      ：在服务器更新资源（客户端提供改变后的完整资源）  
PATCH  ：在服务器更新资源（客户端提供改变的属性）  
DELETE ：从服务器删除资源  

过滤，通过在url上传参的形式传递搜索条件  
`https://api.example.com/v1/zoos?limit=10`：指定返回记录的数量  
`https://api.example.com/v1/zoos?offset=10`：指定返回记录的开始位置  
`https://api.example.com/v1/zoos?page=2&per_page=100`：指定第几页，以及每页的记录数  
`https://api.example.com/v1/zoos?sortby=name&order=asc`：指定返回结果按照哪个属性排序，以及排序顺序  
`https://api.example.com/v1/zoos?animal_type_id=1`：指定筛选条件  

状态码  
 常用状态码列表  
错误处理，状态码是4xx时，应返回错误信息，error当做key。  

    {  
        error: "Invalid API key"  
    }  

返回结果，针对不同操作，服务器向用户返回的结果应该符合以下规范。  

GET /collection：返回资源对象的列表（数组）  
GET /collection/resource：返回单个资源对象  
POST /collection：返回新生成的资源对象  
PUT /collection/resource：返回完整的资源对象  
PATCH /collection/resource：返回完整的资源对象  
DELETE /collection/resource：返回一个空文档  
Hypermedia API，RESTful API最好做到Hypermedia，即返回结果中提供链接，连向其他API方法，使得用户不查文档，也知道下一步应该做什么。  

    {"link": {
      "rel":   "collection https://www.example.com/zoos",
      "href":  "https://api.example.com/zoos",
      "title": "List of zoos",
      "type":  "application/vnd.yourformat+json"
    }}

#### 认证

APIView 继承自 Django 的 View，但是又定义了很多方法，实现了很多功能  

越往下继承，包含的功能越多，ModelViewSet 继承了 6 个类，这六个类中还有父类，所以功能非常多。   

源码从 dispatch 入手  

APIView 自己实现了 dispatch 方法，在 dispatch 方法中  
```python
request = self.initialize_request(request, *args, **kwargs)
self.request = request
```
已经不是 Django 原始的 request 了，是 Django REST framework 处理过的 request，丰富了一些功能  

比如在里面就做了用户认证  

用 Django REST framework 提供了 API 接口，这个接口要控制，有人能访问，有人访问不了，怎么控制？就是要用户认证  

先走 APIView 的 dispatch 方法，在方法中对 request 进行了封装，用户认证系统，先看 views.py 中是不是自己定义了认证方法，如果没有就用 Django REST framework 自己在 settings 里配置的方法认证。然后执行 Django REST framework 自己的 initial 方法，进行认证。然后在 initial 方法中执行 perform_authentication，在 perform_authentication 方法中，调用了 request.user，然后要去 Request 类中找 user 方法，在 user 方法中调用了 self.\_authencate()，在 \_authencate() 方法中循环 authencator，循环认证类的所有对象，在这里调用了 authenticate 方法进行验证。这里返回的是 user_auth_tuple，所以必须是 tuple。如果一个返回了 None，就进行下一次循环，交给下一个循环来处理。       

可以自己配置路径  

没有登录，默认设置的是 AnonymousUser  

内置认证在 rest_framework 的 authentication.py 中  

自己写认证，必须继承 BasicAuthentication 类  

#### 权限  

比如设置 user_type 为普通用户、VIP，设置对应的 id 为 1、2，所谓权限就是判断如果 user_type_id == 2，有权访问，如果不等于 2，就返回无权访问。  

方法就是写一个权限类，然后在视图函数中使用就可以了  

流程和用户认证前半部分差不多，要更简单  

内置权限  


#### 访问频率控制  

访问记录通过拿到用户 IP 地址实现  

实现方法非常巧妙，用列表存储访问记录，比如限制 60 秒之内访问 10 次，用 while 循环，如果最后一条，在 60 之外就 pop，直到所有的都在 60 秒之内，然后判断列表中的元素个数是否大于 10.  

用缓存实现的  


#### 版本  

这个不重要，一次配置，以后不用  

可以通过 url 的 query string 传参，通过 get 拿到，不推荐使用   

最好还是使用 /v1/ 的方式传，用 URLPathVersioning 取到  

源码，还是先走 dispath 方法，在 initial 方法里有 self.determine_version，返回的两个值赋值给 request，在 determin_version 中又调用了 self.version_class，self.version_class 调用的是设置中的 version。  


#### 解析器  

不重要  

Django 自带的 request.POST / request.body  
当请求头中有 Content-Type: application/x-www-form-urlencoded 时，post 中才有值   

Django REST framework 的解析器  
解析器就是对请求体中的数据进行解析  
Django REST framework 的解析器，比 Django 自己的解析器要强大很多  
parser_classes = [JSONParser]，看 JSONParser 源码  
JSON 格式是最常用的  


#### 序列化  

最重要，每个都要用  

序列化有两大功能：对请求验证，对 query_set 进行序列化  

serializers.Serializer  

serializers.ModelSerializer，字段多的时候用    


#### 分页  

PagerSerializer   

PageNumberPagination  


#### 视图  


#### 路由  


#### 渲染  






## 文档  

### Tutorial 1: Serialization  

先创建模型，然后迁移到数据库，然后要使用 Web API 第一件要做的事就是 serializing 导入的 model 实例为 json 格式，在 app 目录下创建 serializer.py 文件，继承 serializers.Serializer，内容和 Django forms 差不多  

第一节的这个 serializer 看似是最麻烦的，但是却是根基，可以看到内部是怎么实现的  

validate_data.get() 是要先验证数据的正确性，比如 python 第一个字母大写就通不过，这一步应该是从数据库取数据，浏览器展示数据之前的验证        

后面的 shell 部分可以看到，serializer 是怎么把数据编程 json 格式的  

`snippet = Snippet(code='foo = "bar"\n')` 就是实例化一个类，指定一个属性 code 的值  

继承 serializers.ModelSerializer，指定 model 和 fields 就行了，而且自动包含了 create() 和 update() 方法  

views 这里用的是函数  

从 snippet_list 和 snippet_detail 两个函数的内部实现可以看出，serializer 可以接受前端页面传来的数据，就是 request，进行序列化，然后保存到数据库，也可以从数据库取数据  

可以从实现中看到 GET 方法就是从数据库中取数据，POST 是存数据  


### Tutorial 2: Requests and Responses  

request.data 和 request.POST 意思差不多，但是功能更强大  

views 使用 api_view 装饰器  

urls.py 添加 suffixes  

浏览器的显示内容的样式会发生改变  

使用浏览器查看内容是一种极大的优势，自己可以很方便地查看和使用，也可以让别人更容易接触  


### Tutorial 3: Class-based Views  

views 使用的是 APIView  

从 SnippetList 这个 class 的 get 方法中可以看到 get 是从数据库中取数据，展示到浏览器中，post 方法是将前面的 request 中包含的数据，save 到数据库中  

可以使用 mixin   

可以使用 generic class-based views，这个最简洁  


### Tutorial 4: Authentication & Permissions  

删除 db.sqlite 的时候，要先停止服务器  

创建用户，关联用户  

可以添加权限，没有登录的用户，没有权限添加数据  


### Tutorial 5: Relationships & Hyperlinked APIs  

这里的 serializer 用的是 HyperlinkedModelSerializer，自动添加超链接  


### Tutorial 6: ViewSets & Routers  

这一节用的 ViewSets 是最简单的  



## Django REST framework 入门  

URL 非常简洁，非常规范  

API 由来已久，在有程序之前就有了 API，我们写一个类库或模块，对外提供几个方法，这几个方法说明要完成什么功能，并且方法有什么参数，以及返回值是什么。你调用了以后，它就完成一些功能，返回一些值  

常见的 Web API 有 create、edit、delete  

REST 请求是 HTTP 请求  

除了 GET 请求外，其他请求的 body 都是 json 格式  

rest 里面最重要的一个就是 serializer，就是把格式转化成 json 格式  

在 serializer.py 里指定 model，指定用 model 的哪些 fields  

看文档里面的 shell 交互代码，就可以很清楚地看到 serializer 是在干什么：拿到数据，转化成 json 格式  

exempt 免除，豁免  

继承 serializers.Serializer，要自己定义各个 field，和 model 的形式差不多  

继承 serializers.ModelSerializer 就非常简洁，指定 model 和 fields 就可以了  

继承 serializers.HyperlinkedModelSerializer 可以实现使用超链接点击跳转  




## 其他  

进入环境：`activate django_rest`  

添加虚拟环境：右下角 Interpreter Settings -> 点击齿轮 -> show all -> 点击加号 在环境中找 python.exe，参考已经有的环境的目录   


