
[uwsgi 中文文档](https://uwsgi-docs-zh.readthedocs.io/zh_CN/latest/)  

[Django 文档，看 uwsgi 参数意义和配置](https://docs.djangoproject.com/zh-hans/3.1/howto/deployment/wsgi/uwsgi/)  


客户端发送请求时 Web 服务器(uwsgi)需要和 web 应用程序(Django)进行通信，但是 web 服务器有很多种，Python web 应用开发框架也对应多种，所以 WSGI 应运而生，定义了一套通信标准。如果不统一标准的话，就会存在 Web 框架和 Web 服务器数据无法匹配的情况，那么开发就会受到限制。  

web 服务器在将请求转交给 web 应用程序之前，需要先将 http 报文转换为 WSGI 规定的格式。  

WSGI 规定，Web 程序必须有一个可调用对象(比如函数)，且该可调用对象接收两个参数，返回一个可迭代对象：  
environ：字典，包含请求的所有信息  
start_response：在可调用对象中调用的函数，用来发起响应，参数包括状态码，headers 等  

wsgi 根据规则把请求封装成 environment，并把 environment 发送给 Django，Django 处理这些数据  

创建一个 hello.py  
```python 
import pysnooper

@pysnooper.snoop(max_variable_length=None)
def application(environ, start_response):
    start_response('200 OK', [('Content-Type', 'text/html')])
    body = '<h1>Hello, %s!<h1>' % (environ['PATH_INFO'][1:] or 'Web')
    return [body.encode('utf-8')]
```

创建一个 server.py  
```python 
from wsgiref.simple_server import make_server
from hello import application


httpd = make_server('', 8000, application)
print('serving port 8000...')
httpd.serve_forever()
```

确保以上两个文件在同一个目录下，然后在命令行输入 python server.py 来启动 WSGI 服务器  
注意：如果 8000 端口已被其他程序占用，启动将失败，就修改成其他端口。  

启动成功后，打开浏览器，输入http:\//localhost:8000/，就可以看到结果了  

    C:\Users\MI\Desktop\10programs\21March\WSGI>python server.py
    serving port 8000...
    Source path:... C:\Users\MI\Desktop\10programs\21March\WSGI\hello.py
    Starting var:.. environ = {'SERVER_NAME': 'DESKTOP-200GG65', 'GATEWAY_INTERFACE': 'CGI/1.1', 'SERVER_PORT': '8000', 'REMOTE_HOST': '', 'CONTENT_LENGTH': '', 'SCRIPT_NAME': '', 'SERVER_PROTOCOL': 'HTTP/1.1', 'SERVER_SOFTWARE': 'WSGIServer/0.2', 'REQUEST_METHOD': 'GET', 'PATH_INFO': '/', 'QUERY_STRING': '', 'REMOTE_ADDR': '127.0.0.1', 'CONTENT_TYPE': 'text/plain', 'HTTP_HOST': 'localhost:8000', 'HTTP_CONNECTION': 'keep-alive', 'HTTP_SEC_CH_UA': '" Not A;Brand";v="99", "Chromium";v="90", "Google Chrome";v="90"', 'HTTP_SEC_CH_UA_MOBILE': '?0', 'HTTP_UPGRADE_INSECURE_REQUESTS': '1', 'HTTP_USER_AGENT': 'Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/90.0.4430.85 Safari/537.36', 'HTTP_ACCEPT': 'text/html,application/xhtml+xml,application/xml;q=0.9,image/avif,image/webp,image/apng,*/*;q=0.8,application/signed-exchange;v=b3;q=0.9', 'HTTP_SEC_FETCH_SITE': 'none', 'HTTP_SEC_FETCH_MODE': 'navigate', 'HTTP_SEC_FETCH_USER': '?1', 'HTTP_SEC_FETCH_DEST': 'document', 'HTTP_ACCEPT_ENCODING': 'gzip, deflate, br', 'HTTP_ACCEPT_LANGUAGE': 'zh-CN,zh;q=0.9,en;q=0.8', 'wsgi.input': <_io.BufferedReader name=524>, 'wsgi.errors': <_io.TextIOWrapper name='<stderr>' mode='w' encoding='utf-8'>, 'wsgi.version': (1, 0), 'wsgi.run_once': False, 'wsgi.url_scheme': 'http', 'wsgi.multithread': True, 'wsgi.multiprocess': False, 'wsgi.file_wrapper': <class 'wsgiref.util.FileWrapper'>}
    Starting var:.. start_response = <bound method BaseHandler.start_response of <wsgiref.simple_server.ServerHandler object at 0x0000028330A4CDD8>>
    11:39:11.095888 call         5 def application(environ, start_response):
    11:39:11.102899 line         6     start_response('200 OK', [('Content-Type', 'text/html')])
    11:39:11.103867 line         7     body = '<h1>Hello, %s!<h1>' % (environ['PATH_INFO'][1:] or 'Web')
    New var:....... body = '<h1>Hello, Web!<h1>'
    11:39:11.103867 line         8     return [body.encode('utf-8')]
    11:39:11.104863 return       8     return [body.encode('utf-8')]
    Return value:.. [b'<h1>Hello, Web!<h1>']
    Elapsed time: 00:00:00.008975

无论多么复杂的 Web 应用程序，入口都是一个 WSGI 处理函数。HTTP 请求的所有输入信息都可以通过 environ 获得，HTTP 响应的输出都可以通过 start_response() 加上函数返回值作为 Body。  

