
这本书是读懂源码的基础，是读懂源码的最强大的工具，源码是最好的技术文档技术书，可以读懂 Django、DjangoRESTFramework、Flask、Python 库、深度学习框架等  

方法是先读源码，遇到不会的读一章，分而治之，各个击破  

已完成：单下划线和双下划线、== 和 is、copy 和 deepcopy、迭代器和生成器、垃圾回收机制、\_\_new__ 和 \_\_init__、静态方法和类方法、字典推导式、装饰器、作用域、闭包、    

以这一篇为标准，[《流畅的python》阅读笔记](https://segmentfault.com/a/1190000011568813) [备份链接](https://zhuanlan.zhihu.com/p/30754843)，自己写的笔记就是一些补充    

层次结构图片中，箭头是从子类指向父类   

#### 第1章 Python数据模型  

访问属性，调用方法的时候，就会调用 \_\_getitem__ ,   

for 循环背后调用的是 iter(), 背后是 \_\_iter__    

\_\_repr__ 的作用是实现字符串现实形式  
```python 
class Dog:
    pass 

my_dog = Dog()
print(my_dog)
```
结果是 `<__main__.Dog object at 0x00000283CAAD5FD0>`，这样的输出对我们理解程序没什么帮助  

可以改写 \_\_repr__，来实现输出自己想要了解得内容。  
```python 
class Dog:
     def __init__(self):
         self.name = '旺财'
         self.age = 3
     def __repr__(self):
         return "名字："+ self.name +"，年龄：" + str(self.age) + " 岁"

my_dog = Dog()
print(my_dog)
``` 
结果是 `名字：旺财，年龄：3 岁`  

占位符 % 和 .format() 背后用的就是 \_\_repr__  

使用 if while and or 这些的时候，会调用 bool() 进行判断  


#### 第5章 一等函数   

```python 
def tag(name, *content, cls=None, **attrs):
    """生成一个或多个HTML标签"""
    if cls is not None:
        attrs['class'] = cls
    if attrs:
        attr_str = ''.join('%s="%s" ' % (attr, value) for attr, value in sorted(attrs.items()))
    else:
        attr_str = ''
    if content:
        return '\n'.join('<%s %s>%s</%s>' % (name, attr_str, c, name) for c in content)
    else:
        return '<%s %s/>' % (name, attr_str)


print(tag("br"))
print(tag("p", "hello"))
print(tag("p", "hello", "world"))
print(tag("p", "hello", id=33))
print(tag("p", "hello", "word", cls='sidebar'))
print(tag(content="testing", name='img'))
my_tag = {'name': "img", "title": "Sunset Boulevard", "src": "sunset.jpg", "cls": "framed"}
print(tag(**my_tag))
```  


#### 第7章 函数装饰器和闭包  

装饰器执行顺序   

```python 
registry = []  # 第一个断点


def register(func):
    print('running register(%s)' % func)  # 第二个断点
    registry.append(func)
    return func


@register
def f1():
    print('running f1()')


@register
def f2():
    print('running f2()')


def f3():
    print('running f3()')


def main():
    print('running main()')
    print('registry->', registry)
    f1()  # 步入
    f2()  # 步入
    f3()  # 步入


if __name__ == '__main__':
    main()  # 第三个断点，步入
```  


[装饰器](https://www.bilibili.com/video/BV1Vv411x7hj?p=1)非常重要  

装饰器实现原理：基于 @ 语法和函数闭包，将原函数封装在闭包中，然后将函数赋值为一个新的函数（内层函数），执行函数时再在内层函数中执行闭包中的原函数    
装饰器实现效果：可以在不改变原函数内部代码和调用方法的前提下，实现在函数执行和执行扩展功能  
装饰器适用场景：多个函数系统统一在执行前后自定义一些功能  

背下来这段代码  
```python
def outer(origin):
    def inner(*args, **kwargs):
        # 执行前  
        result = origin(*args, **kwargs)  
        # 执行后  
        return result 
    return inner
    
@outer
def func():
    pass 
    
func()
```

可以在不改变原有函数结构的情况的，为函数增加功能；大量简化重复代码，只写一个 @ 就行；如果修改，只修改一处就行，维护极其方便  

用的多的时候，很多地方都要增加功能的时候，用装饰器  





#### 第8章 对象引用、可变性和垃圾回收  

为了理解 Python 中的赋值语句，应该始终先读右边。对象在右边创建或获取，然后为对象贴贴纸  

对象一旦建立，标识就不会再变，就是 id，就是内存地址，就是身份证  

is 比较的是id；== 比较的是 value    

元组如果有可变的元素，那么元组元素是可变的，元组不可变说的是元组的标识不会变  

浅复制，复制了最外层容器，副本中的元素是源容器中元素的引用  

#### 第9章 符合 Python 风格的对象  

所以可以自己重写内置方法，来改变行为  

一般方法不实例化直接使用类调用是会报错的，

@classmothed 改变了调用方法的方式，一般是实例调用，而类方法是类调用，所以调用的时候不用实例化，所以第一个参数是 cls，而不是 self。好处是不用改变原来的类的结构，增加功能，有点像插件。  

不需要实例化是因为想在类实例化之前增加某些功能，先和类进行交互    



受保护的和私有属性的意思是，这个方法只能在当前这个类中使用，不要在外面使用  

变量前面添加两个下划线和一个下划线的主要目的是避免意外覆盖。  

Python 不像 Java 那样使用 private 来创建私有属性，但是 Python 也有自己的避免意外覆盖私有属性的方法。  

比如有人编写了一个名为 Dog 的类，这个类属性内部用到了 mood 实例属性，但是没有对外开放，后来另一个人创建了 Dog 的子类 Beagle，并且在毫不知情的情况下创建了 mood 实例属性，那么在继承中就会把 Dog 类中的 mood 属性覆盖掉，这是个很难 debug 的错误。  

如果以 \_\_mood 的形式命名实例属性，则 Python 会自动加上一个下划线和类名，于是两个实例属性就分别变成了 \_Dog\_\_mood 和 \_Beagle\_\_mood，这种特性叫做名称改写，可以避免意外访问造成的错误。  

有些人不喜欢这种方式，他们使用一个下划线来实现这种保护功能，很多程序员都遵守这种规定，他们不会在外部引用带有一个下划线的属性，Python 解释器也不会对这种格式的属性做特殊处理，所以就成了约定俗成的私有属性。(属于民间版本)  

`__dict__` 存储会消耗大量内存，通过 `__slots__` 属性，可以让解释器在元组中存储实例属性，而不是字典，从而节省大量内存。  



有了 @property 装饰器，调用的时候，就直接当一个属性来调用，不用加括号了   


#### 第14章 可迭代的对象、迭代器和生成器  

可迭代对象就是有 \_\_iter__ 方法的类的实例  

迭代器类型有 \_\_iter__ 方法和 \_\_next__ 方法的类，迭代器对象就是类的实例对象  

生成器对象是生成器类 generator 的对象，generator 类内部实现了 \_\_iter__ 方法和 \_\_next__ 方法，所以可以说 generator 就是一种特殊的迭代器  


#### 第21章 类元编程  

元类就是读源码用的  

Python 中类可以创建对象，类创建对象分两步，第一步是用构造方法 \_\_new__ 创建一个对象，对象是空的，第二步是初始化方法 \_\_init__ 完成初始化  

类可以由 type 创建，元类是用来改变创建过程的  

元类用来指定类由谁创建  

metaclass=指定的类  

类加括号执行 \_\_new__ 方法和 \_\_init__ 方法  
实例加括号执行 \_\_call__ 方法  

类是元类的对象，类加括号的时候，其实调用的是元类的 \_\_call__ 方法  

之所以创建对象的时候先执行 \_\_new__ 方法后执行 \_\_init__ 方法，就是因为在元类中的 \_\_call __ 方法中有 \_\_new__ 方法和 \_\_init__ 方法，而且 \_\_new__ 方法在 \_\_init__ 方法之前执行  


### 其他  

python 自省就是运行时能够获得对象的类型。比如type()，dir()，getattr()，hasattr()，isinstance()  

[Python 自省方法](https://mp.weixin.qq.com/s?__biz=MzA5NzgzODI5NA==&mid=2454038123&idx=4&sn=e4f654549eca6d51344873c6f85568cb&chksm=872bb3d2b05c3ac4b0cffac332d71256a3e19813e0187ef77076e32f78423d37c9e71111e07a&scene=21#wechat_redirect)  
自省是一种自我检查行为。在计算机编程中，自省是指这种能力：检查某些事物以确定它是什么、它知道什么以及它能做什么。自省向程序员提供了极大的灵活性和控制力。  

说的更简单直白一点：自省就是面向对象的语言所写的程序在运行时，能够知道对象的类型。一句可以概况为：运行时能够获知对象的类型。  

字典推导式 
```python
d = {key: value for (key, value) in iterable}
```
GIL 对于 IO 密集型，python 多线程会提高速度，但是对于 CPU 密集型，很可能会降低速度  





