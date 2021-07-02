
Guido van Rossum: **Programming languages are how programmers express themselves and communicate ideas**。  


编程就是给你原材料(数据结构)、工具(if语句、for循环、函数、类)和说明书(算法)，自己生产自己想要的产品。想一想自己想去除 Chrome 的 doodle 费了多少周折还是做不成，想定制新建标签页面是何其艰难，这就可以看出编程是有多么广阔的自由度   

Python 可以在 PyCharm 中看源码，虽然没有代码，但是有 doc，doc 里面有例子，是最权威的解释，是最好的参考；  
比如 setattr  
```python 
def setattr(x, y, v):
    """
    Sets the named attribute on the given object to the specified value.
    
    setattr(x, 'y', v) is equivalent to ``x.y = v''
    """
    pass
```

或者使用 help，效果是一样的。比如 help(setattr)  

```python
a = [1, 2, 3]  
isinstance(a, list)    # True
```


Python 里 . 就是的，views.banner 就是 views 里面的 banner 函数   

重载就是同名函数不同参数  
比如 round(1.567) 结果是 2，round(1.567, 2) 保留两位小数，结果是 1.57   

#### 变量和数据类型  

数据类型：数字(整数浮点数)、字符串 ''、列表 []，列表可以遍历、元组()、字典 {} 括起来的键值对、类的实例和函数等

type() 看类型   

字面量就是最简单的表达式，所以又叫简单值，比如 42，"hello" 都是字面量，对字面量求值会得到自己，而 age 不加引号，就是变量，求值要看赋给它的值是什么      

#### 编码规范  

PyCharm 快捷键 Ctrl + Alt + l  

被困惑是很好的事情，如果不是自己在编码规范上苦苦思索挣扎过，看到这个快捷键就不会这么高兴。由于人越渴，喝到水时，乐趣就越大。——但丁《神曲》  

编码规范是为了好读，不要吹毛求疵，因小失大。最重要的，最核心的还是编程思想，是程序实现的功能。  

4 个空格缩进；顶级定义之间空两行，比如 class，类中的方法之间空一行；二元操作符前后空格，比如四则运算符号，用 = 指定参数默认值的时候，前后不要有空格。 

类名称首字母大写，其他除全局变量外都是小写加下划线  


#### 注释  

单行注释井号，多行注释三引号  

文档字符串，类或函数的第一句话，可以用自带的 \_\_doc__ 函数访问  
```python
from collections import OrderedDict  
OrderedDict.__doc__  
'Dictionary that remembers insertion order'  
```
多写注释，不用就忘。  

一个普通人加上记笔记的习惯就可以成为一个天才。  

Python 中的 -> 就是函数标注，为函数添加元数据，本质上就是注释，方便阅读，通常用于类型提示：例如以下函数预期接受两个 int 参数并预期返回一个 int 值:  

```python 
def sum_two_numbers(a: int, b: int) -> int:
    return a + b
```

PEP 是 Python Enhancement Proposal 的缩写，通常翻译为“Python增强提案”。每个 PEP 都是一份为 Python 社区提供的指导 Python 往更好的方向发展的技术文档，其中的第 8 号增强提案（PEP 8）是针对 Python 语言编订的代码风格指南。  

#### 占位符

```python 
name = 'mayanan' 
age = 30  
print('%s, %d' % (name, age))  
```

[% 和 format](https://mp.weixin.qq.com/s?__biz=MzA5NzgzODI5NA==&mid=2454037457&idx=4&sn=232076a78028e1cf7b3496ead5ab465e&chksm=872bb668b05c3f7e958f5e9bb8306e2bf743472adbe9d42a5f8db5b3be8077e02a8af104f6da&scene=21#wechat_redirect)  

占位符的读法是，读到哪一个就把后面的名字提到前面来读  

前端 `{% extends 'base.html' %}` 也是这样，把 base.html 的内容替换到当前的 HTML 文件中，就很清楚了  

`super().__init__(*args, **kwargs)` 也是这个意思，把父类中的 \_\_init__ 方法中的内容放到当前 \_\_init__ 中  

#### Python 数据类型  

Python 的六种标准数据类型：数字、字符串、列表、元组、字典、集合。  

不可变数据（3个）：Number（数字）、String（字符串）、Tuple（元组）。
可变数据（3个）：List（列表）、Dictionary（字典）、Set（集合）。  

[可变数据类型和不可变数据类型，这一篇说的最清楚](https://mp.weixin.qq.com/s?__biz=MzA5NzgzODI5NA==&mid=2454037174&idx=3&sn=e44a0b1fcf6e374119c5a970f38cba87&chksm=872bb70fb05c3e194d3daaffc7033bab02fab9ae88908ff488638dd7c8d3fa8c9eb0d315e437&scene=21#wechat_redirect)  


#### 数字  

3.14e2 就是 314，科学计数法，表示 10 的 2 次方  

#### 运算

可变对象是说对象的值可以被修改，不可变对象是说对象的值不可以被修改  

可变对象：列表、字典、自定义类创建的对象  

不可变对象：数字、字符串、元组  
数字不可以被修改是说，赋值以后 id 会变，是重新创建了一个新的对象。  
`t = (1, 2, 3)  
t[0] = 100`
会报错，元组不可修改。  

#### 序列  

序列包括字符串、列表和元组  
切片  

序列操作函数：enumerate、len、reversed、sorted、zip、  

`l = [(3, 'cat'), (1, 'bag'), (2, 'apple')]`  

`print(sorted(l, key=lambda x:x[0]))`  
lambda 是 key 的 lambda，这个是按数字排序  

`print(sorted(l, key=lambda x:x[1]))`  
这个是按字母排序  

#### 字符串

字符串统一使用单引号    

r 就是 raw，按照原始的字符串输出，读路径的时候常用  

#### 列表  

列表方法：append、insert、remove、pop、clear、count、sort、reverse、  
列表方法可以在 PyCharm 中看，`a = list()` 看 list  

append() 函数就是在栈顶添加元素  
```python
a = [1, 2, 3]  
a.append(4)  # 结果 a = [1, 2, 3, 4]
```

pop() 函数就是在栈顶弹出元素  
```python
a = [1, 2, 3]  
a.pop()    # 弹出 3  
a.pop(0)   # 弹出 1  
```

列表推导式：`[x**2 for x in range(5)]`  

#### 列表和元组的区别  

最核心的一点就是，列表是动态数组，列表是可变的;元组是静态数组，不可变，且其内部数据一旦创建便无法改变。我们可以修改列表的值，但是不修改元组的值。    

列表是用来保存多个相互独立对象的数据集合  
元组设计的初衷就是为了描述一个不会改变的事物的多个属性  

[列表存储空间分配](https://github.com/yananma/python_web/blob/main/%E4%B8%8D%E5%B8%B8%E7%94%A8/Python%20%E5%9F%BA%E7%A1%80/%E5%88%97%E8%A1%A8%E5%92%8C%E5%85%83%E7%BB%84%E7%9A%84%E5%8C%BA%E5%88%AB.md)

#### 集合
 {} 或 set()，去重  

#### 字典

字典其实就是字典，键是目录的一条，值是具体的详细内容。特点就是关联关系和哈希存储  

字典是 Python 提供的一种常用的数据结构，主要用于存放具有映射关系的数据 。比如保存某班同学的成绩单数据，张三：95分，李四：70分，王五：100分 ... ，因为姓名和成绩是有关联的，所以不能单独用两个列表来分别保存，这时候用字典来存储，再合适不过了。  

字典是一种可变的容器模型，它是通过一组键（key）值（value）对组成，这种结构类型通常也被称为映射，或者叫关联数组，也有叫哈希表的。每个key-value之间用“:”隔开，每组用“,”分割，整个字典用“{}”括起来。  

JSON(JavaScript Object Notation) 是一种数据格式，是一种 Notation，和 CSV 一个级别。  

字典是一种数据结构。  

可以把 JSON 转化成字典  

####  OrderedDict  
Dictionary that remembers insertion order  

字典存储用的是 hash，是无序的，OrderedDict 可以按字典中元素的插入顺序来输出。  

OrderedDict 是使用双向链表存储，插入的时候在链表表尾插入  

#### range 函数

range(start, stop, step)    # 是非常合理的，step 可有可无，放到最后面，start 开头，stop 结尾  

#### break 和 continue  

break 就是不跑了，回宿舍，continue 就是这一圈没跑完，后面剩下的不跑了，回到出发点跑下一圈  

#### 迭代器

迭代器主要是在函数内部使用，有 iter() 和 next()  

iter(序列)， next(迭代器)  

`l = ['享学', 'Python', 'mayanan']`  

`it = iter(l)`  这个就是迭代器  

`print(next(it))`    享学  
`print(next(it))`    Python  
`print(next(it))`    mayanan    
就是有一个指针一样  


#### 生成器

有 yield 关键字，就是一个生成器。  

生成器的本质：遵守迭代器协议，**逐个产出元素**，而不是先建一个完整的列表，再把这个列表传入到某个构造函数里。优点是可以节省内存。  

语法：把列表推导的方括号换成圆括号即可。   


#### if 语句，条件判断  

if 语句就是在分叉路口做判断，根据判断结果选择走哪一条路  

把 if 和 else 下的内容当做两条路上的内容  

#### 函数

关键字参数说的是调用的时候指定，可以不用管定义的时候的顺序。比如 
```python
def about(name, course, site): 
    print(name, course, site)  
```

调用的时候可以指定，`about(site='网址', name='名字', course='课程')` 可以打乱顺序  

site 就是形参，'网址'就是实参  

默认参数是说定义的时候指定的  

不定长参数，就是加 *  
```python
def loop(*args):   
    for x in args:  
        print(x)  

loop(1, 2, 3)  
loop(1, 3, 5, 7, 9)  
```    

#### \*args 和 \*\*kwargs  

灵活的参数处理机制，是 Python 最好的特性之一  

可变参数(Variable Argument)，就是不定量，不定长的参数，\*args 是可变的 positional arguments，kwargs 是可变的 keyword arguments  

这里的核心是 \* 和 \*\*，后面的名词可以随便取，比如 \*var \*\*vars；     

\* 和 \*\* 的作用是展开可迭代对象，映射到单个参数  

这一个程序就能说明所有问题了  
```python 
def para_test(arg, *args, **kwargs):
    print(arg, type(args), args, type(kwargs), kwargs)
    
para_test(1, 3, 4, 5, a=7, b=8, c=9)  
1 <class 'tuple'> (3, 4, 5) <class 'dict'> {'a': 7, 'b': 8, 'c': 9}
```

[详细例子](https://github.com/yananma/python_web/blob/main/%E4%B8%8D%E5%B8%B8%E7%94%A8/Python%20%E5%9F%BA%E7%A1%80/args%20%E5%92%8C%20kwargs%20%E8%AF%A6%E7%BB%86.md) 


#### 递归函数  

1、函数自己调用自己  
2、有终止条件  


#### 变量的作用域和闭包

局部的和全局的  
```python
def f(x):  
    lacal_var = 200  
```

在外面 print(local_var) 就会报错，因为局部变量只能在函数内部使用  
如果是在函数外面定义，就是全局变量，在哪里都可以调用  

闭包就是，内部函数引用了外部函数的变量(不是全局变量)，那么内部函数就是闭包  

闭包
* 必须有一个内嵌函数
* 内嵌函数必须引用外部函数中的变量
* 外部函数的返回值必须是内嵌函数

```python
def outer():  
    num = 100  
    def inner():  
        print(num)  
    inner()  

outer()  
```
这个例子中，num 可以读，但是不能改，比如 num = num + 1 就报错  

[pysnooper 文件：闭包](https://github.com/yananma/python_web/blob/main/%E4%B8%8D%E5%B8%B8%E7%94%A8/pysnooper%20%E6%96%87%E4%BB%B6/%E9%97%AD%E5%8C%85.md)

闭包的特殊之处在于在这里 inner 可以调用 num 变量，一般是不可以的  
查找顺序：局部 闭包 全局 内建  

局部不能修改全局变量，如果要修改，就要加上 global 关键字 [global 例子](https://github.com/yananma/python_web/blob/main/%E4%B8%8D%E5%B8%B8%E7%94%A8/pysnooper%20%E6%96%87%E4%BB%B6/%E9%97%AD%E5%8C%85.md#global)  
nonlocal 就是闭包里修改外部函数的变量 [nonlocal 例子](https://github.com/yananma/python_web/blob/main/%E4%B8%8D%E5%B8%B8%E7%94%A8/pysnooper%20%E6%96%87%E4%BB%B6/%E9%97%AD%E5%8C%85.md#nonlocal)  


函数的参数就是局部变量  

#### 模块  

如果使用命令行，关闭以后程序就没有了，所以要存储到文件中。模块可以实现代码重用  

搜索路径，默认是在环境变量中去寻找；运行期间是在 sys.path 中去寻找，sys.path 是一个列表，可以通过 append 添加  

模块在导入的时候就会被执行，为了避免这种情况，办法就是写 if name == \_\_main__  

#### 包

当模块非常多的时候，可以加上一定的逻辑，可以用包来组织模块，包就是文件夹，模块就是文件   

包要有 \_\_init__ 文件，有一个 \_\_init__ 文件是为了和普通文件夹做区分，有这个文件，就是一个 Python 包，就可以 import     

#### 文件  

f 就是 file  

```python
def open_file():  
    with open('test.txt','r',encoding='utf-8') as f:  
        print(f.read())  


def write_file():
    with open('test.py', 'w', encoding='utf-8') as f:
        f.write('Hello World!')

write_file()
```

#### 异常和错误  

**好程序和差程序之间的区别往往在于处理意外情况的能力**  

所以源码中有非常多的 try except 语句和 if 判断  

错误是在编译期间出现的，比如语法错误，逻辑错误，  

异常是在运行期间出现的，比如算法错误，内存不够。  

如果报了错，下面就不再执行了  

处理异常 try except，原因就是一部分出错，不能影响另一部分工作。比如汽车雨刷坏了不能影响刹车  

程序也是这样，不能因为一个小毛病就崩溃了  
```python
def loop(l):  
    try:  
        print(l[3])  
    except Exception as e:  
        print('error')  

loop([1, 2])
```

try except 的时候一般会 print 错误信息，否则不知道错在什么地方  

finally 不管有没有异常都会执行，比如 close 文件，关闭数据库等等  

[异常](https://mp.weixin.qq.com/s?__biz=MzA5NzgzODI5NA==&mid=2454038018&idx=4&sn=cacc75f7858e5b66949a5e85f54e36ac&chksm=872bb3bbb05c3aad0d07d352f0b8ae10ce6351490f19b44b232999fc0560d85f8843d7d22d6c&scene=21#wechat_redirect)

#### raise 和 assert  

raise 是主动抛出异常，assert 是断言，满足条件才往下执行  

#### 自定义异常

类要继承 Exception 类，要重写 \_\_init__ 和 \_\_str__ 方法，可以用 raise 抛出异常  

#### 面向对象  

[封装、继承、多态](https://mp.weixin.qq.com/s?__biz=MzA5NzgzODI5NA==&mid=2454037085&idx=2&sn=6f898ae80004ed081648b761f271c63a&chksm=872bb7e4b05c3ef25f205f55fdf50189e66b03b48dcac5f6b2089a7dab4ef94d164ba567d337&scene=21#wechat_redirect)    
封装，比如汽车，最后留给我们的只有几个方向盘，刹车等几个接口，发动机、变速箱等都封装了起来  

隐藏对象的属性和实现细节，仅对外提供公共访问方式。  
好处：1. 将变化隔离；2. 便于使用；3. 提高复用性；4. 提高安全性。  
在python中用双下划线开头的方式将属性设置成私有的。  

多态是一种事物的多种体现形式，函数的重写其实就是多态的一种体现。  
多态的好处：（1）增加了程序的灵活性；（2）增加了程序可扩展性  

类是抽象的，是一个模板；对象是具体的，是类的一个实例  

函数放到类里就叫做方法，其实就是函数  

构造方法就是 \_\_init__，作用就是初始化实例变量，当实例化对象时，一定会调用构造方法  

方法重载，方法名称相同，参数的个数或类型不同  

self 关键字，self 翻译过来就是我自己，指当前对象本身，谁调用该方法，当前对象就是谁；在类里面的方法的第一个关键字必须是 self；self 就是 this，翻译成这个实例的  

验证 self 就是实例本身代码  

```python
class Person(object):  
    def __init__(self):  
        print(id(self))  

# 方法里的 self 的 id 和实例也是相同的  
    def say_hello(self, name):
        print(id(self))
        print('hello,', name)


p = Person()  
print(id(p))  

p = Person()  
print(id(p))  
p.say_hello('mayanan')  
```

id 相同，所以就验证了 self 就是这个实例本身  

最开始初始化的时候，写 self.name = name 就是要区分参数和实例变量，否则分不清  

#### 类方法静态方法和实例方法  

实例方法必须实例化才能调用，就是最常用的那种方法  
```python
class Site(object):
    def get_name(self):
        return 'baidu'
    def get_address(self):
        return 'http://www.baidu.com'

s = Site()
name = s.get_name()
address = s.get_address()
print(name, address)
```

静态方法不需要实例化，通过名称就可以直接访问，静态方法不加 self，因为不用实例化，所以不加 self  
```python
class Site(object):  
    @staticmethod  
    def get_name():  
        return 'mayanan'  

name = Site.get_name()  
print(name)  
```
静态方法不能访问实例变量（因为没有实例化），也不能访问类变量。（静态方法用的不多）  

类方法用的是 @classmethod，第一个参数必须是 cls 类本身  
```python
class Site(object):
    name = 'mayanan'
    @classmethod
    def get_name(cls):
        return cls.name

name = Site.get_name()
print(name)
```

#### 类属性和实例属性(属性就是变量)  

类变量：是可在类的所有实例之间共享的值  
实例变量：实例化之后，每个实例单独拥有的变量  

实例属性就是实例变量，self.name = name，前面的 self.name 就是实例属性  

下面这样的就是类属性，实例方法可以访问类属性  
```python
class Site(object):  
    name = 'mayanan'     
    course = 'Python'  
    
Site().course   # 类属性可以直接被类调用
site = Site()
site.name    # 也可以通过实例调用  
```

#### 继承  

可以继承父类里面所有的属性和方法，不用再从头构建    

多重继承，可以继承多个类  

非常清楚的一个例子  

```python
class Bird(object):  
    def fly(self):  
        print('fly...')  

class Fish(object):  
    def swim(self):  
        print('swim...')  

class FlyFish(Bird, Fish):  
    pass  

ff = FlyFish()  
ff.fly()  
ff.swim()  
```

#### 方法覆盖  

必须是继承关系；子类覆盖(重写)父类里面的同名方法  

如果子类重新实现了父类中的同名方法，调用的时候，会使用子类的方法，也就是子类的优先级更高  

源码是使用了 update 方法，如果有同名方法，就 update，覆盖原来的方法    

既可以复用，又可以保证灵活性，可以根据实际情况修改定制  

```python
class Animal(object):  
    def run(self):  
        print('Animal run...')  

    def sleep(self):  
        print('Animal sleep...')  


class Dog(Animal):  
    # 这个例子很好地展示了方法覆盖的含义  
    def run(self):  
        super.run()   # 这里调用的就是父类的 run 方法，覆盖，但是用的时候还可以用，这就是 super 的作用  
        print('dog run...')  


hua = Dog()  
hua.run()  
hua.sleep()  
```

#### super 关键字 

上面的例子更好，说明了 super 的作用就是调用父类的方法  

调用父类的初始化方法 super().\_\_init__()  
调用父类的其他属性和方法  

```python
class Person(object):  
    def __init__(self, name, age):  
        self.name = name  
        self.age = age  

    def display(self):  
        print(self.name, self.age)  

class Manager(Person):  
    def __init__(self):  
        super().__init__('mayanan', 26)   # 理解 super().__init__() 的很好的例子

    def m_display(self):  
        super().display()  

m = Manager()  
m.m_display()  
```


#### issubclass  

判断前面一个类是不是后面类的子类  

```python 
class Animal(object):
    pass 
    
class Dog(Animal):
    pass  
    
print(issubclass(Dog, Animal))    # True   

```

#### isinstance 

isinstance(obj, cls)  

判断一个实例是不是后面这个类的实例  

```python
a = [1, 2, 3]  
isinstance(a, list)    # True
```


#### 属性操作  

hasattr()、getattr()、setattr()、delattr()  
```python
class Person(object):  
    def __init__(self, name):  
        self.name = name  

p = Person('mayanan')  
print(hasattr(p, 'name')) True  
print(getattr(p, 'name'))   # 就是 p.name  
setattr(p, 'name', 'mayanan')    # 等价于 p.name = 'mayanan'，想一想是非常合理的，因为要 set  
print(p.name)  
delattr(p, 'name')  
print(hasattr(p, 'name')) False   
```

#### Python 组合关系  

Python 类之间有继承关系，也有组合关系，组合有一对一，一对多，多对一，多对多  

人骑车  
```python 
class Person(object):
    def ride(self, b):
        b.run()


class Bicycle(object):
    def run(self):
        print('run...')


b = Bicycle()
p = Person()
p.ride(a, b)
```


最好的一个例子  
```python
class Author(object):
    def __init__(self, name, age):
        self.name = name
        self.age = age

class Course(object):
    def __init__(self, name, runtime, author):
        self.name = name
        self.runtime = runtime
        self.author = author

class Site(object):
    def __init__(self, name, address, courses):
        self.name = name
        self.address = address
        self.courses = courses

a = Author('马亚南', 26)
py = Course('Python 基础', 100, a)
dj = Course('Django 项目', 120, a)

xxkt = Site('享学课堂', '2xkt.com', [py, dj])

print(xxkt.name)
print(xxkt.address)
courses = xxkt.courses

for c in courses:
    print(c.name, c.runtime, c.author.name)
# print(xxkt.courses)
```


#### 序列化和反序列化  

作用就是持久保存  

对象序列化就是把对象保存成文件格式，从 Python 转成 Windows，用 pickle.dumps()  
反序列化就是把对象从文件转化为对象，从 Windows 转成 Python，用 pickle.load()  

因为一般情况下，结束以后内容就消失了，所以有了序列化    
```python
try:  
    import cPickle as pickle  
except ImportError:
    import pickle  


class Person(object):  
    def __init__(self, name, age):   
        self.name = name  
        self.age = age  

p = Person('mayanan', 26)  

def write():  
    with open('test.data', 'wb') as f:  
        b = pickle.dumps(p)  
        f.write(b)  

def read():  
    with open('test.data', 'rb') as f1:  
        p = pickle.load(f1)  
        print(p.name, p.age)  

# write()  
read()  
```    

#### Python 访问控制  

主要就控制是变量和方法的调用  

一个下划线，意思是受保护的，但只是一种口头约定，用的时候和一般的完全一样，丝毫不会影响。  
前面两个下划线，意思是私有的，调用的时候会报错，说没有这个变量或方法  

#### 多线程  

多进程是系统中的多个应用程序，比如同时打开 WPS、QQ、音乐、浏览器等等；打开任务管理器，看到开的应用就是进程  
线程是一个应用程序的多个执行线路，这样就不会产生阻塞，用户不用等待；比如 web 服务器针对不同用户的请求，启动不同的线程来相应，不用排队；  

如果没有多线程，就会顺序执行，不管第一个函数执行多长时间，后面的函数都会等待  

不使用线程代码，就是先打印 5 个 i，i 打印完了以后再打印 j    
```python
from time import ctime, sleep  

def func1():  
    for i in range(5):  
        print('i=', i)  
        sleep(0.1)  

def func2():  
    for j in range(5):  
        print('j=', j)  
        sleep(0.1)  

def main():  
    print('start:', ctime)  
    func1()  
    func2()  
    print('end:', ctime)  

if __name__ == '__main__':  
    main()  
```

使用线程交替执行，不是顺序执行的，而是并行执行的  

相当于买票的时候，原来只有一个窗口，只能这一队人排完以后，才能开始另一队；多线程就是有多个窗口买票  

现实中不使用 sleep 函数，因为不知道运行多长时间，现实中使用 lock  

python3 中使用的是 threading 模块，有 3 种方法，第一种是创建 Thread 实例，为 target 函数传递一个参数；第二种是创建 Thread 实例，传递给一个可调用的类实例，需要复写 \_\_call__ 函数；第三种是继承 Thread，并创建子类的实例  

```python
import threading
from time import ctime, sleep

def func1():
    for i in range(5):
        print('i=%d \n' % i)
        sleep(0.1)

def func2():
    for j in range(5):
        print('j=%d \n' % j)
        sleep(0.1)

def main():
    print('start:', ctime())
    t1 = threading.Thread(target=func1)
    t2 = threading.Thread(target=func2)
    t1.start()
    t2.start()
    t1.join()
    t2.join()
    print('end:', ctime())

if __name__ == '__main__':
    main()
```

#### 线程同步  

多个用户同时操作一个共享资源，要对共享资源进行保护，方法就是使用 lock。  

比如现实中火车站，4 个窗口卖 100 张票，就要用 lock 线程，否则会卖重复  
```python
class Window(threading.Thread):  
    def __init__(self, n, lock):  
        self.lock = lock  
        threading.Thread.__init__(self, name=n)  

    def take(self):  
        global tickets  
        while tickets >= 1:  
            self.lock.acquire()  
            print('%s :%d' % (threading.currentThread().name, tickets))  
            tickets -= 1  
            self.lock.release()  
            sleep(0.1)  

    def run(self):  
        self.take()  

def main():  
    lock = threading.Lock()  
    for i in range(1, 5):  
        name = '窗口' + str(i)  
        w = Window(name, lock)  
        w.start()  

if __name__ == '__main__':  
    main()  
```        

如果把程序中的 lock 去掉，就会有卖重复的现象  

queue 模块使得共享数据更加方便，不用再用 lock，不用再自己控制，queue 自己内部就实现了这些功能  
```python
from queue import Queue
from time import sleep
from random import randint
from threading import Thread


class Producer(object):
    def __init__(self, q):
        self.q = q

    def put(self):
        print('为 Q 添加对象...')
        self.q.put('xxx', 1)
        print('当前 Q 大小：%d' % self.q.qsize())

    def produce(self):
        for i in range(5):
            self.put()
            sleep(randint(1, 2))

    def __call__(self):
        self.produce()

class Consumer(object):
    def __init__(self, q):
        self.q = q

    def get(self):
        val = self.q.get(1)
        print('从 Q 取对象...')
        print('当前 Q 大小：%d' % self.q.qsize())

    def consume(self):
        for i in range(5):
            self.get()
            sleep(randint(2, 5))

    def __call__(self):
            self.consume()


def main():
    q = Queue(32)
    p = Producer(q)
    c = Consumer(q)

    t1 = Thread(target=p)
    t1.start()

    t2 = Thread(target=c)
    t2.start()

    t1.join()
    t2.join()

if __name__ == '__main__':
    main()
```

#### 网络编程  

客户端服务器，客户端发送请求，服务器返回响应  

socket 就是插座，5 个部分连接上以后才是一个 socket，协议 ip 端口 ip 端口。互联网上有成千上万台机器，一台机器如何找到另一台机器呢？办法就是 IP 地址，每一台机器都有唯一的 IP 地址。另一个问题是，一台电脑有几百个应用，怎么区分应用呢？答案就是端口号。socket 由 IP 地址和端口号组成，想要请求应用程序的服务，就必须要知道 IP 地址和端口号，有了 IP 地址和端口号以后就能定位到这个应用，就能实现连接，连接以后就可以实现数据的收发。有点儿像访问阿里云的 docker  

服务器先绑定一个端口号，然后 listen 监听，客户端再根据 IP 地址和端口号连接服务器，如果服务器接受了连接，就可以实现读写，数据传输  

网络连接一般分为两种，一种是面向连接的 TCP，必须要先建立连接才能实现，分片段传输，传输是可靠的，使用的协议是 TCP 协议，SOCKET_STREAM；另一种是无连接的 UDP，不需要连接，整体发送，不能保证可靠性，SOCKET_DGRAM  


#### TCP  

要先运行服务器，先 listen，再运行客户端  
要打开端口  

TCP 服务器  
```python
from socket import *  
from time import ctime  

HOST = 'localhost'  
PORT = 10001  
BUFFER = 1024  
ADDRESS = (HOST, PORT)  

serverSocket = socket(AF_INET, SOCK_STREAM)  
serverSocket.bind(ADDRESS)  

serverSocket.listen(5)  

while True:  
    print('等待连接...')  
    clientSocket, add = serverSocket.accept()  
    print('连接来自：', add)  
    while True:  
        data = clientSocket.recv(BUFFER).decode()  
        print('来自客户端的信息：', data)  
        if not data:  
            break  
        clientSocket.send(('[%s] %s' %(ctime(), data)).encode())  
    clientSocket.close()  

serverSocket.close()  
```

TCP 客户端  

```python
from socket import *  

HOST = 'localhost'  
PORT = 10001  
BUFFER = 1024  
ADDRESS = (HOST, PORT)  

clientSocket = socket(AF_INET, SOCK_STREAM)  
clientSocket.connect(ADDRESS)  
while True:  
    data = input('>')  
    if not data:  
        break  
    clientSocket.send(data.encode())  
    data = clientSocket.recv(BUFFER).decode()  
    if not data:  
        break  
    print(data)  

clientSocket.close()  
```

UDP 服务器 

```python
from socket import *
from time import ctime

HOST = 'localhost'
PORT = 10001
BUFFER = 1024
ADDRESS = (HOST, PORT)

udpSocket = socket(AF_INET, SOCK_DGRAM)
udpSocket.bind(ADDRESS)

while True:
    print('等待信息...')
    data, addr = udpSocket.recvfrom(BUFFER)
    if not data:
        break
    print(data.decode())
    udpSocket.sendto(('[%s] %s' %(ctime(), data.decode())).encode(), addr)
    print('返回给：', addr)

udpSocket.close()
```


UDP 客户端  

```python
from socket import *

HOST = 'localhost'
PORT = 10001
BUFFER = 1024
ADDRESS = (HOST, PORT)

udpClient = socket(AF_INET, SOCK_DGRAM)

while True:
    data = input('>')
    if not data:
        break
    udpClient.sendto(data.encode(), ADDRESS)
    data, ADDRESS = udpClient.recvfrom(BUFFER)
    if not data:
        break
    print(data.decode())
    print(ADDRESS)

udpClient.close()
```

#### 服务器  

```python
import socket

sock = socket.socket()
sock.bind(('127.0.0.1', 80))
sock.listen(5)

while True:
  conn, addr = sock.accept()
  data = conn.recv(8096)
  conn.send(b'HTTP/1.1 200 OK\r\n\r\n')
  conn.send(b'123')
  conn.close()
```

可以在阿里云服务器上跑，把 IP 改成 0.0.0.0，端口自己指定，阿里云打开安全组端口  

#### url 访问  

复制代码，用 ipython 运行  
浏览器输入 `http://127.0.0.1:10001/index` 访问  


```python
import socket

def index():
    # return b'index page!'
    # return b'<html><h1>H1</h1></html>'
    return b'<html><form action="" method="POST"><input type="text" class="form-control" name="telephone" placeholder="phone number"> <button type="submit" class="btn btn-primary btn-block btn-flat">login</button></form></html>'   # 最后在命令行中国看到了一个 telephone=18888888888，证明数据从浏览器传到了服务器 

urls = [
    ('/index', index)
]

sock = socket.socket()
sock.bind(('127.0.0.1', 10001))
sock.listen(5)

while True:
    conn, addr = sock.accept()
    data = conn.recv(8096).decode()
    print('这里是浏览器发送的所有的 data：\n', data)  # 浏览器就是客户端，可以清楚地看到，客户端发送了什么内容到服务器，彻底理解了客户端和服务器是怎么交互的；彻底理解了 cookie 和 session 是如何发挥作用的  
    print('这里是 data[4:10]：', data[4:10])
    url = data[4:10]
    conn.send(b'HTTP/1.1 200 OK\r\n\r\n')

    page_content = None
    for u in urls:
        print('这里是 u[0]', u[0])
        # print('这里是 u[1]', u[1])
        if u[0] == url:  # 可以清楚地看到，是 url 是怎么发挥作用的，就是匹配  
            page_content = u[1]
            break

    if page_content:
        response = page_content()
        print("这里是 response：\n", response)
    else:
        response = b'404 page not found!'

    conn.send(response)
    conn.close()
```

改变 index 返回的内容，比如改成 HTML 表单，就可以看到表单是如何提交数据的  

退出的时候，先在命令行中 Ctrl + C，然后刷新浏览器，就可以退出  

再次运行，可以换端口，比如 10002，或者等一会儿  



https://www.nowcoder.com/tutorial/10005/dc2c82d6557548beb0e2252869be13d8
