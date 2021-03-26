
方法：视频看很多遍，代替读文档的文字，自己只敲代码，不再读文档  

视频 2 遍  




## Quickstart  

先找 url，其中 include(router.urls) 就包含了上面 register 的 users 和 groups；  
可以从这两个 url 找到各自的 view，view 中定义了 queryset，从数据库取值，定义了寻找的 serializer，可以关联到 serializer，定义了 permission；  
serializer 定义了绑定的 model 和要使用的 model 的 fields。  





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

继承 serializers.ModelSerializer 就非常简洁，指定 model 指定 fields 就可以了  


server can receive data from applications，可以是电脑端、iOS 和 Android  

前面是序列化一条数据，想要序列化所有的数据，要用 many=True  





## 文章  

URL 定位资源，用 HTTP 动词（GET,POST,DELETE,DETC）描述操作。  

REST 描述的是在网络中 client 和 server 的一种交互形式  

RESTful 可以通过一套统一的接口为 Web，iOS 和 Android 提供服务。另外对于广大平台来说，比如 Facebook platform，微博开放平台，微信公共平台等，它们不需要有显式的前端，只需要一套提供服务的接口，于是 RESTful 更是它们最好的选择。  






## 其他  

进入环境：`activate django_rest`  

添加虚拟环境：右下角 Interpreter Settings -> 点击齿轮 -> show all -> 点击加号 在环境中找 python.exe，参考已经有的环境的目录   


