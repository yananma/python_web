


#### 第4章 Python面向对象程序设计   

这个例子不重要，主要就是记一下，不用再看。    

```python 
class Users(object):
    online_count = 0

    def __init__(self):
        Users.online_count += 1


a = Users()
a.online_count += 1
print(Users.online_count)
```  

这个例子是在说类变量和实例变量。    

Users() 在实例化的时候，会调用 init 方法，online_count 会加 1，就变成了 1.    

a.online_count 就是 1，再 += 1 以后，a.online_count 就是 2.    

最后打印 Users.online_count 还是 1.   




