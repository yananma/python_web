
这本书是读懂源码的基础，是读懂源码的最强大的工具，源码是最好的技术文档技术书，可以读懂 Django、Flask、Python 库、深度学习框架等  

方法是先读源码，遇到不会的读一章，分而治之，各个击破  

元类(metaclass)、静态方法和类方法、字典推导式、迭代器和生成器、装饰器、\_\_new__ 和 \_\_init__、作用域、闭包、垃圾回收机制、

已完成：单下划线和双下划线、== 和 is、copy 和 deepcopy、  

### 第1章 Python数据模型  

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




### 第7章 函数装饰器和闭包  

装饰器是函数  




### 第8章 对象引用、可变性和垃圾回收  

为了理解 Python 中的赋值语句，应该始终先读右边。对象在右边创建或获取，然后为对象贴贴纸  

对象一旦建立，标识就不会再变，就是 id，就是内存地址，就是身份证  

is 比较的是地址；== 比较的是存储的内容  

元组如果有可变的元素，那么元组元素是可变的，元组不可变说的是元组的标识不会变  

浅复制，复制了最外层容器，副本中的元素是源容器中元素的引用  
```python
l1 = [3, [66, 55, 44], (7, 8, 9)] 
l2 = list(l1)   # 执行以后，l1 和 l2 指代不同的列表，但是两个列表引用的是相同的列表 [66, 55, 44] 和元组 (7, 8, 9)  
l1.append(100)  # l1 的列表增加了一个值为 100 的元素，l2 列表不变
l1[1].remove(55)   # 这里 remove 的是共同的引用，所以 l2 也 remove 了 55  
print('l1:', l1)   # l1: [3, [66, 44], (7, 8, 9), 100]
print('l2:', l2)   # l2: [3, [66, 44], (7, 8, 9)]
l2[1] += [33, 22]   # 改变的是共同引用部分，l1 和 l2 的引用内容都增加了 33 和 22  
l2[2] += (10, 11)   # l2 中的 tuple 不再引用，而是新建了一个元组
print('l1:', l1)   # l1: [3, [66, 44, 33, 22], (7, 8, 9), 100]
print('l2:', l2)   # l2: [3, [66, 44, 33, 22], (7, 8, 9, 10, 11)]  
```
在 [pythontutor](http://www.pythontutor.com/live.html#mode=edit) 上跑一遍就完全明白什么是深复制，什么是浅复制了  



### 第9章 符合 Python 风格的对象  

```python 
 class Vector2d:
     typecode = 'd'
     def __init__(self, x, y):
         print('init')
         self.x = float(x)
         self.y = float(y)
     def __iter__(self):
         print('iter')
         return (i for i in (self.x, self.y))
     def __repr__(self):
         print('repr')
         class_name = type(self).__name__
         return '{}({!r}, {!r})'.format(class_name, *self)
     def __str__(self):
         print('str')
         return str(tuple(self))
     def __bytes__(self):
         print('bytes')
         return (bytes([ord(self.typecode)])+
                 bytes(array(self.typecode, self)))
     def __eq__(self, other):
         print('eq')
         return tuple(self) == tuple(other)
     def __abs__(self):
         print('abs')
         return math.hypot(self.x, self.y)
     def __bool__(self):
         print('bool')
         return bool(abs(self))
```
敲一遍 9.2 节代码，可以看到程序都调用了哪个方法  

`v1 = Vector2d(3, 4)` 实例化，调用了 `__init__`  
`v1` 调用了 `__repr__`  
`print(v1)` 调用了 `__tr__`  
`x, y = v1` 拆包调用了 `__iter__`  
`v1 == v1_clone` 调用了 `__eq__`  
`bytes(v1)` 调用了 `__bytes__`  
`abs` 调用了 `__abs__`  
`bool(v1)` 调用了 `__bool__`  

所以可以自己重写这些方法，来改变行为  



Python 不像 Java 那样使用 private 来创建私有属性，但是 Python 也有自己的避免意外覆盖私有属性的方法。  

比如有人编写了一个名为 Dog 的类，这个类属性内部用到了 mood 实例属性，但是没有对外开放，后来另一个人创建了 Dog 的子类 Beagle，并且在毫不知情的情况下创建了 mood 实例属性，那么在继承中就会把 Dog 类中的 mood 属性覆盖掉，这是个很难 debug 的错误。  

如果以 \_\_mood 的形式命名实例属性，则 Python 会自动加上一个下划线和类名，于是两个实例属性就分别变成了 \_Dog\_\_mood 和 \_Beagle\_\_mood，这种特性叫做名称改写，可以避免意外访问造成的错误。  

有些人不喜欢这种方式，他们使用一个下划线来实现这种保护功能，很多程序员都遵守这种规定，他们不会在外部引用带有一个下划线的属性，Python 解释器也不会对这种格式的属性做特殊处理，所以就成了约定俗成的私有属性。(属于民间版本)  






## 其他  

python 自省就是运行时能够获得对象的类型。比如type()，dir()，getattr()，hasattr()，isinstance()  

字典推导式 
```python
d = {key: value for (key, value) in iterable}
```
GIL 对于 IO 密集型，python 多线程会提高速度，但是对于 CPU 密集型，很可能会降低速度  


