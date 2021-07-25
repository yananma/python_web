
## [Django REST framework 框架经典教程](https://www.bilibili.com/video/BV1Sz4y1o7E8?p=1)  

这门课是讲的最好的，过几个月有时间还要再看一遍。  

serializer 主要有两种：Serializer 和 ModelSerializer  

视图主要有四种：APIView、GenericAPIView 结合 Mixin、ViewSet、GenericViewSet  


#### RESTful 规范  

前后端分离，后端只写一套代码即可，可以服务于各种前端场景  

Django REST framework 封装度特别高，自己手写一个符合 RESTful 风格的程序需要 100 多行代码，使用 Django REST framework 只要 4 行就能完成。  

但是封装度高的框架，还用不好理解，所以还是应该能够自己手写。  

学习 Django REST framework 的目的就是快速开发前后端分离的程序，使得开发效率大大提升。  

自己写代码，不同的人会有各种偏好，前端刚适应一种风格，换了人就又换了另一种风格，会非常痛苦。  

RESTful 统一规范，可以极大地减少沟通成本。  

RESTful 只有两种视图，列表视图和详情视图，详情视图是多了一个 pk    

通过 GET、POST、PUT、DELETE 方法实现增删改查  

代码，自己手写 5 遍  

```python 
# views.py

from datetime import datetime

class BooksAPIVIew(View):
    """
    查询所有图书、增加图书
    """
    def get(self, request):
        """
        查询所有图书
        路由：GET /books/
        """
        queryset = BookInfo.objects.all()
        book_list = []
        for book in queryset:
            book_list.append({
                'id': book.id,
                'btitle': book.btitle,
                'bpub_date': book.bpub_date,
                'bread': book.bread,
                'bcomment': book.bcomment,
                'image': book.image.url if book.image else ''
            })
        return JsonResponse(book_list, safe=False)

    def post(self, request):
        """
        新增图书
        路由：POST /books/ 
        """
        json_bytes = request.body
        json_str = json_bytes.decode()
        book_dict = json.loads(json_str)

        # 此处详细的校验参数省略

        book = BookInfo.objects.create(
            btitle=book_dict.get('btitle'),
            bpub_date=datetime.strptime(book_dict.get('bpub_date'), '%Y-%m-%d').date()
        )

        return JsonResponse({
            'id': book.id,
            'btitle': book.btitle,
            'bpub_date': book.bpub_date,
            'bread': book.bread,
            'bcomment': book.bcomment,
            'image': book.image.url if book.image else ''
        }, status=201)


class BookAPIView(View):
    def get(self, request, pk):
        """
        获取单个图书信息
        路由： GET  /books/<pk>/
        """
        try:
            book = BookInfo.objects.get(pk=pk)
        except BookInfo.DoesNotExist:
            return HttpResponse(status=404)

        return JsonResponse({
            'id': book.id,
            'btitle': book.btitle,
            'bpub_date': book.bpub_date,
            'bread': book.bread,
            'bcomment': book.bcomment,
            'image': book.image.url if book.image else ''
        })

    def put(self, request, pk):
        """
        修改图书信息
        路由： PUT  /books/<pk>
        """
        try:
            book = BookInfo.objects.get(pk=pk)
        except BookInfo.DoesNotExist:
            return HttpResponse(status=404)

        json_bytes = request.body
        json_str = json_bytes.decode()
        book_dict = json.loads(json_str)

        # 此处详细的校验参数省略

        book.btitle = book_dict.get('btitle')
        book.bpub_date = datetime.strptime(book_dict.get('bpub_date'), '%Y-%m-%d').date()
        book.save()

        return JsonResponse({
            'id': book.id,
            'btitle': book.btitle,
            'bpub_date': book.bpub_date,
            'bread': book.bread,
            'bcomment': book.bcomment,
            'image': book.image.url if book.image else ''
        })

    def delete(self, request, pk):
        """
        删除图书
        路由： DELETE /books/<pk>/
        """
        try:
            book = BookInfo.objects.get(pk=pk)
        except BookInfo.DoesNotExist:
            return HttpResponse(status=404)

        book.delete()

        return HttpResponse(status=204)
```        

```python 
# urls.py

urlpatterns = [
    url(r'^books/$', views.BooksAPIVIew.as_view()),
    url(r'^books/(?P<pk>\d+)/$', views.BookAPIView.as_view())
]
```

#### Django REST framework 框架简介  

Django REST framework 内部就遵守了 RESTful 设计风格  

序列化就是把从数据库查询的结果，编程 json 格式输出到前端；反序列化就是把前端输入的 json 格式数据，转换成一般格式，存入到数据库中。  

Django REST framework 的主要功能就是将序列化和反序列化进行了封装。写程序的时候只需要把数据传给 Django REST framework 即可。  

Django REST framework 提供了序列化和反序列化方法；丰富的类视图，简化视图的编写；丰富的定制层级函数视图、类视图、视图集合，满足不同的应用场景；多种身份认证和权限认证方式；限流系统；直观的 API web 页面；课扩展性，有很多插件。  

学习 Django REST framework 主要学的就是 serializer 和视图，还有一点辅助功能。  

要使用 Django REST framework 就要先添加到 INSTALLED_APPS 中，所以 Django REST framework 是对 Django 的一个拓展，不添加找不到模板文件。  

用 Django REST framework 实现上面的程序，非常简洁。  

serializers.py  
```python 
class BookInfoSerializer(serializer.ModelSerializer):
    """实现模型的序列化与反序列化"""
    class Meta:
        model = BookInfo  
        fields = '__all__'
```
model 指明该序列化器处理的数据字段的模型类  
fields 指明该序列化器包含模型类中的哪些字段  

views.py  
```python 
from rest_framework.viewsets import ModelViewSet
from .serializers import BookInfoSerializer
from .models import BookInfo

class BookInfoViewSet(ModelViewSet):
    """指定查询集"""
    queryset = BookInfo.objects.all()  
    """指定序列化器"""
    serializer_class = BookInfoSerializer  
```
queryset 指明查询数据时使用的数据  
serializer_class 指明该视图在进行序列化或反序列化时使用的序列化器  

urls.py  
```python 
from . import views
from rest_framework.routers import DefaultRouter

urlpatterns = [
    ...
]

router = DefaultRouter()  # 创建路由器
router.register(r'books', views.BookInfoViewSet)  # 向路由器中注册视图集

urlpatterns += router.urls  # 将路由器中的所以路由信息追到到django的路由列表中
```

#### 序列化  

在开发 REST API 的时候，主要是做了 3 件事：将 json 数据进行反序列化；操作数据库；序列化成 json 格式返回给前端。  

所以 Django REST framework 把用的最多的第一步和第三步进行了封装，大大简化了开发流程。  

序列化器不仅可以进行数据转行，还会进行数据校验。  

数据校验主要是用在反序列化中，用于验证前端传入的数据是否合法。  

序列化器就是一个 Python 类  

serializer 就是比照着 model 的字段写的（可以用 Django 的分屏功能），而且要保证 serializer 的字段名字和 model 的字段名字完全一样，因为 serializer 就是按照字段名去 model 里取值的  

只是要求名称一样，数量并没有说一定要完全一样，可以选择只使用部分字段。  

read_only 只读，只能序列化，不能反序列化，也就是只能输出。比如 id 字段。  

write_only 只能反序列化。  

serializer 类主要接受两个参数，序列化时接受的 instance 和反序列化时接受的 data  

`serializer = BookSerializer(instance=book)`  
然后 `serializer.data` 就可以直接获取序列化后的字典数据  

序列化多个对象，要使用参数 many=True  

ModelSerializer 更简洁，自己默认用 ModelSerializer  

不是自己写字段，而是引入 Model，可以自动生成字段  

ModelSerializer 中定义了 create 和 update 方法。  

在 ModelSerializer 中也可以像在 Serializer 中一样定义字段，因为 ModelSerializer 是继承自 Serializer，所以肯定是可以的。  

使用 extra_kwargs 可以修改选项参数。  


#### 反序列化  

serializer(data=data)  

is_valid() 用于数据验证  

errors 属性包含了错误信息  

反序列化通过 validated_data 属性拿到数据  

```python 
data = {
    'title': '三国', 
    'pub_data': '1985-01-01'
}

serializer = BookSerializer(data=data)  
serializer.is_valid()  
serializer.errors  
serializer.validated_data 
```

可以自己在 serializer 函数中定义校验规则  

校验规则以 validate_ 开头，后面接字段名，因为验证的时候是去掉前面的 validate_，以后面的字段名为 key 去取值。  

验证通过以后要保存，调用 serializer 的 save 方法（不是 ORM 的 save 方法），save 有两个功能 update 和 create，如果原来的 instance 存在，就 update，如果不存在就 create。在源码的最后一段有判断  

可以自己实现 create 和 update 方法，使用 ORM 的 create 和 update  

create 方法  
`book = Book.objects.create(**validated_data)`  

update 方法  
`instance.title = validated_data.get('title')`  


#### Django REST framework 中的 request 和 response  

Request 和 Response 都对 Django 中自带的进行了封装，增加了功能。  

在 Request 中增加了 parser 解析器，可以根据请求头中 content-type 自动进行类型转换  

request.data 包含了原来的 POST 和 FILES 属性，包含了 POST、PUT、PATCH 请求方式解析后的数据  

request.query_params 和 Django 中的 request.GET 一样，就是换了一个名字，源码就是 `self._request.GET`  

response.data 是已经序列化但是还没有 render 的数据（这里的 render 不是渲染，而是进一步的数据处理） 

response.status_code 状态码数字  

response.content 经过 render 处理后的数据  


#### APIView  

视图函数非常简单：主要就是数据和序列化器  

APIView 是 Django REST framework 中所有类视图的基类  

APIView 继承自 Django 的 View，不过传入的 request 和返回的 response 都是 Django REST framework 的 request 和 response  

而且 APIView 在 dispatch 方法中增加了身份认证、权限检查和流量控制  

authentication_classes 身份认证类  
permissoin_classes 权限检查类  
throttle_classes 流量控制类  

```python 
class SnippetList(APIView):
    """
    List all snippets, or create a new snippet.
    """
    def get(self, request, format=None):
        snippets = Snippet.objects.all()
        serializer = SnippetSerializer(snippets, many=True)
        return Response(serializer.data)

    def post(self, request, format=None):
        serializer = SnippetSerializer(data=request.data)    # 反序列化
        if serializer.is_valid():
            serializer.save()
            return Response(serializer.data, status=status.HTTP_201_CREATED)
        return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)
```


#### GenericAPIView  

继承自 APIVIew，主要增加了操作序列化器和数据库查询的方法，作用是为下面 Mixin 扩展类的执行提供方法支持。通常在使用时，可搭配一个或多个 Mixin 扩展类。  

关于序列化器使用的属性与方法  

serializer_class 指明视图使用的序列化器  

get_serializer_class(self) 返回序列化器类，默认返回serializer_class，可以重写。  

get_serializer(self, args, \*kwargs) 返回序列化器对象，主要用来提供给Mixin扩展类使用，如果我们在视图中想要获取序列化器对象，也可以直接调用此方法。  

关于数据库查询的属性与方法  

queryset 指明使用的数据查询集  

get_queryset(self) 返回视图使用的查询集，主要用来提供给Mixin扩展类使用，是列表视图与详情视图获取数据的基础，默认返回queryset属性，可以重写。  

get_object(self) 返回详情视图所需的模型类数据对象（获取单一模型对象），主要用来提供给Mixin扩展类使用。  

GenericAPIView 结合 Mixin 可以极大地减少代码量  
```python 
class SnippetList(mixins.ListModelMixin,
                  mixins.CreateModelMixin,
                  generics.GenericAPIView):
    queryset = Snippet.objects.all()
    serializer_class = SnippetSerializer

    def get(self, request, *args, **kwargs):
        return self.list(request, *args, **kwargs)

    def post(self, request, *args, **kwargs):
        return self.create(request, *args, **kwargs)
```

#### ViewSet  

ViewSet 源码主要就是重写了 as_view() 方法，目的就是可以把增删改查所有的接口都可以写在一个类视图里面  

list() 提供一组数据  
retrieve() 提供单个数据  
create() 创建数据  
update() 保存数据  
destory() 删除数据  

ViewSet 视图集类不再实现 get()、post() 等方法，而是实现动作 action 如 list() 、create() 等。  

视图集只在使用 as_view() 方法的时候，才会将 action 动作与具体请求方式对应上。  

也就是把请求方法写在 as_view() 里，把请求方法和视图方法绑定在一起 as_view({'get': 'list'}) 获取列表，as_view({'get': 'retrieve'}) 获取详细（视图类中定义了 list 和 retrieve 方法）  

```python 
class BookInfoViewSet(viewsets.ViewSet):

    def list(self, request):
        books = BookInfo.objects.all()
        serializer = BookInfoSerializer(books, many=True)
        return Response(serializer.data)

    def retrieve(self, request, pk=None):
        try:
            books = BookInfo.objects.get(id=pk)
        except BookInfo.DoesNotExist:
            return Response(status=status.HTTP_404_NOT_FOUND)
        serializer = BookInfoSerializer(books)
        return Response(serializer.data)
```

路由  
```python 
urlpatterns = [
    url(r'^books/$', BookInfoViewSet.as_view({'get':'list'}),
    url(r'^books/(?P<pk>\d+)/$', BookInfoViewSet.as_view({'get': 'retrieve'})
]
```

ViewSet 继承自 APIView，GenericViewSet 继承自 GenericAPIView  


使用ViewSet通常并不方便，因为list、retrieve、create、update、destory等方法都需要自己编写，而这些方法与前面讲过的Mixin扩展类提供的方法同名，所以我们可以通过继承Mixin扩展类来复用这些方法而无需自己编写。但是Mixin扩展类依赖与GenericAPIView，所以还需要继承GenericAPIView。

GenericViewSet 就帮助我们完成了这样的继承工作，继承自 GenericAPIView 与 ViewSetMixin，在实现了调用 as_view() 时传入字典（如 {'get':'list'}）的映射处理工作的同时，还提供了GenericAPIView 提供的基础方法，可以直接搭配 Mixin 扩展类使用。  

```python 
class BookInfoViewSet(mixins.ListModelMixin, mixins.RetrieveModelMixin, GenericViewSet):
    queryset = BookInfo.objects.all()
    serializer_class = BookInfoSerializer
```

可以直接使用 ModelViewSet，就不用再写 Mixin 了。ModelViewSet 继承自 GenericViewSet，同时包括了ListModelMixin、RetrieveModelMixin、CreateModelMixin、UpdateModelMixin、DestoryModelMixin。  


#### 路由器

路由器只能结合视图集一起使用，其他情况还是用 Django 的 path 配置路由  

可以不指定 base_name 属性，读源码就可以看到，Django REST framework 会自己去找 model 的 name  


### 其他功能  

作为了解  

#### 认证   

Authentication  

就是状态保持，如果认证通过就是还会保持登录状态。  

就是判断是登录用户还是匿名用户。  

要进行认证的核心原因是 HTTP 协议是无状态的，但是有些页面却是要登录以后才可以访问。  

认证要配合权限才能看出效果。  

写在 settings 中就是全局变量，所有的视图中都可以用。写在视图中 authentication_classes 是局部变量，只有访问这个视图的时候才可以用。  

认证一般写在全局中。  

认证失败会有两种可能的返回值：  
401 Unauthorized 未认证  
403 Permission Denied 权限被禁止  


#### 权限   

权限和认证一样，可以写在 settings 里面，作为全局变量，也可以写在类视图的 permission_classes 中。  

权限一般写在局部视图中。因为写在 settings 里，很多功能都不能用了。  

默认权限是 AllowAny 允许所有用户。  

permission_classes = (IsAuthenticated, ) IsAuthenticated 仅通过认证的用户。意思就是已经登录的用户。  

可以自定义权限。比如 VIP 用户不用看广告。  

自定义权限，需继承rest_framework.permissions.BasePermission父类，并实现以下两个任何一个方法或全部  

.has_permission(self, request, view)  
是否可以访问视图， view表示当前视图对象  

.has_object_permission(self, request, view, obj)  
是否可以访问数据对象， view表示当前视图， obj 为单一数据对象  

```python 
class MyPermission(BasePermission):
    def has_object_permission(self, request, view, obj):
        """控制对 obj 对象的访问权限，此案例拒绝所有对对象的访问"""
        return False

class BookInfoViewSet(ModelViewSet):
    queryset = BookInfo.objects.all()
    serializer_class = BookInfoSerializer
    permission_classes = [IsAuthenticated, MyPermission]
```


#### 限流   

对接口访问的频次进行限制，以减轻服务器压力。买服务器很贵；访问量过大会服务器死机。  

也是可以配置全局和局部。   


#### 过滤   

过滤就是得到自己想要的，排除自己不想要的。  

过滤用在查询所有的时候，对应的是列表视图。  

restful 建议，过滤信息都应该通过查询字符串实现。   

不加查询字符串的时候，是查询所有，加了查询字符串，就是过滤。  


#### 排序   

排序也是一种过滤，按照自己想要的方式展示出来。  

很简单，指定过滤后端，指定排序字段。  


#### 分页   

分页也是对应于增删改查中的查，而且是对应于查询所有。  

分页继承自 PageNumberPagination。  

页数不需要控制，需要控制的是每页显示多少条数据。  

page_size 每页数目  
page_query_param 前端发送的页数关键字名，默认为 "page"  
page_size_query_param 前端发送的每页数目关键字名，默认为 None  
max_page_size 前端最多能设置的每页数量  

还有一种方式是 limit 和 offset。和分页效果是一样的，不过用的不太多。  


#### 异常处理  

REST framework定义的异常  
APIException 所有异常的父类  
ParseError 解析错误  
AuthenticationFailed 认证失败  
NotAuthenticated 尚未认证  
PermissionDenied 权限决绝  
NotFound 未找到  
MethodNotAllowed 请求方式不支持  
NotAcceptable 要获取的数据格式不支持  
Throttled 超过限流次数  
ValidationError 校验失败  


#### 自动生成接口文档   

安装 coreapi  

大部分还是手写。  






