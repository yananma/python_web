
## Django REST framework 框架经典教程  

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

APIView 是 Django REST framework 中所有类视图的基类  

APIView 继承自 Django 的 View，不过传入的 request 和返回的 response 都是 Django REST framework 的 request 和 response  

而且 APIView 在 dispatch 方法中增加了身份认证、权限检查和流量控制  

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



