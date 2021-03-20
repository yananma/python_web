
## Quickstart  

先找 url，其中 include(router.urls) 就包含了上面 register 的 users 和 groups；  
可以从这两个 url 找到各自的 view，view 中定义了 queryset，从数据库取值，定义了寻找的 serializer，可以关联到 serializer，定义了 permission；  
serializer 定义了绑定的 model 和要使用的 model 的 fields。  







进入环境：`activate django_rest`  

添加虚拟环境：右下角 Interpreter Settings -> 点击齿轮 -> show all -> 点击加号 在环境中找 python.exe，参考已经有的环境的目录   


