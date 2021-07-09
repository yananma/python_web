
DRF 在 Django 的基础上，去掉了模板的部分，提供了一个 REST 接口  

models -> serializers -> views -> urls 的模式去分析  

方法：写项目，读源码

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







## 视频课程  

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



<br>  

*** 

server can receive data from applications，可以是电脑端、iOS 和 Android，allows one software talk to another    

前面是序列化一条数据，想要序列化所有的数据，要用 many=True  

REST API pretty works like web does  





## Quickstart，不再写 quickstart 的代码    

url -> views -> models 数据库取值 -> serializer 序列化成 json 格式 -> 返回响应到浏览器  

先找 url，其中 include(router.urls) 就包含了上面 register 的 users 和 groups；  
可以从这两个 url 找到各自的 view，view 中定义了 queryset，从数据库取值，定义了寻找的 serializer，可以关联到 serializer，定义了 permission；  
serializer 定义了绑定的 model 和要使用的 model 的 fields。  


## 文章  

URL 定位资源，用 HTTP 动词（GET,POST,DELETE,DETC）描述操作。  

REST 描述的是在网络中 client 和 server 的一种交互形式  

RESTful 可以通过一套统一的接口为 Web，iOS 和 Android 提供服务。另外对于广大平台来说，比如 Facebook platform，微博开放平台，微信公共平台等，它们不需要有显式的前端，只需要一套提供服务的接口，于是 RESTful 更是它们最好的选择。  




## 其他  

进入环境：`activate django_rest`  

添加虚拟环境：右下角 Interpreter Settings -> 点击齿轮 -> show all -> 点击加号 在环境中找 python.exe，参考已经有的环境的目录   


