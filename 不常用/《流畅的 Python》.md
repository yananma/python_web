
已完成：单下划线和双下划线、[== 和 is](https://mp.weixin.qq.com/s?__biz=MzA5NzgzODI5NA==&mid=2454038245&idx=4&sn=6c4f80bee2292ad74ec8466428bf4bdc&chksm=872bb35cb05c3a4a57955cd41f949c3608d5742b05298507004da975a3174b2b7425fbbbd6ec&scene=21#wechat_redirect)、[copy 和 deepcopy](https://mp.weixin.qq.com/s?__biz=MzA5NzgzODI5NA==&mid=2454037267&idx=4&sn=6c41c5e950dc057a0713cf7e683d3403&chksm=872bb6aab05c3fbc7874054dbab0df0771a6666e2d1799d7f04276a0cc4b998141fef4c60c44&scene=21#wechat_redirect)、[迭代器和生成器](https://mp.weixin.qq.com/s?__biz=MzA5NzgzODI5NA==&mid=2454037337&idx=5&sn=3c84b314c82f72abf2213b1982b70311&chksm=872bb6e0b05c3ff6c284aba96b1203c1335f1f256c2a7ad9513cecd835c5ee89c40789a09fc6&scene=21#wechat_redirect)、[垃圾回收机制](https://mp.weixin.qq.com/s?__biz=MzA5NzgzODI5NA==&mid=2454037551&idx=5&sn=63f15731506f43c134320f594ba1d2fb&chksm=872bb196b05c3880378e6bee135e9f03d3e72f08606f55790a69f7e92961c74c0ef6c37fc3a6&scene=21#wechat_redirect)、[\_\_new__ 和 \_\_init__](https://mp.weixin.qq.com/s?__biz=MzA5NzgzODI5NA==&mid=2454037869&idx=5&sn=1b101279e96bd18cdb2e88d135703f94&chksm=872bb0d4b05c39c2786ed93d90f1ef07bca0d624bc07d893c59b094aafbe98eaea1fdbdeaffa&scene=21#wechat_redirect)、元类(metaclass)、静态方法和类方法、字典推导式、装饰器、作用域、闭包、    


#### 深拷贝浅拷贝  

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




```python 
from array import array 
import math 

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

此时的 Vector2d 是不可散列的，因此不能放入 set() 中。`hash(v1)`和`set([v1])`会报错。如果要把 Vector2d 实例变成可散列的，必须要实现 `__hash__` 和 `__eq__` 方法。此外还要让变量不可变。变量不可变就是使用 @property 装饰器，。

