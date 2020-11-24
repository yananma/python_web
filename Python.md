
#### 变量和数据类型  

数据类型：数字(整数浮点数)、字符串 ''、列表 []，列表可以遍历、元组()、字典 {} 括起来的键值对、类的实例和函数等

type() 看类型  

#### 编码规范  

4 个空格缩进；顶级定义之间空两行，比如 class，类中的方法之间空一行；二元操作符前后空格，比如四则运算符号，用 = 指定参数默认值的时候，前后不要有空格。 

类名称大写，其他除全局变量外都是小写加下划线  


#### 注释  

单行注释井号，多行注释三引号  

文档字符串，类或函数的第一句话，可以用自带的 \_\_doc__ 函数访问  

多写注释，不用就忘。  

一个普通人加上记笔记的习惯就可以成为一个天才。  


#### 编程基础

占位符，name = 'mayanan' age = 30  print('%s, %d' % (name, age))  


#### 数字  

3.14e2 就是 314，科学计数法，表示 10 的 2 次方  

#### 运算

可变对象是说对象的值可以被修改，不可变对象是说对象的值不可以被修改  

可变对象：列表、字典、自定义类创建的对象  

不可变对象：数字、字符串、元组  
数字不可以被修改是说，赋值以后 id 会变，是重新创建了一个新的对象。
t = (1, 2, 3)  t[0] = 100 会报错，元组不可修改。  

#### 序列  

序列包括字符串、列表和元组  
切片  

序列操作函数：enumerate、len、reversed、sorted、zip、  

l = [(3, 'cat'), (1, 'bag'), (2, 'apple')]  

print(sorted(l, key=lambda x:x[0]))  
lambda 是 key 的 lambda，这个是按数字排序  

print(sorted(l, key=lambda x:x[1]))  
这个是按字母排序  

#### 字符串

r 就是 raw，按照原始的字符串输出，读路径的时候常用  

#### 列表  

列表方法：append、insert、remove、pop、clear、count、sort、reverse、  

列表推导式：[x\*\*2 for x in range(5)]  


#### 集合
 {} 或 set()，去重  

#### 字典

键值对  

#### range 函数

range(start, stop, step)  

#### break 和 continue  

break 就是不跑了，回宿舍，continue 就是这一圈没跑完，后面剩下的不跑了，回到出发点跑下一圈  

#### 迭代器

迭代器主要是在函数内部使用，有 iter() 和 next()  

iter(序列)， next(迭代器)  

l = ['享学', 'Python', 'mayanan']  

it = iter(l)  这个就是迭代器  

print(next(it))    享学
print(next(it))    Python
print(next(it))    mayanan    
就是有一个指针一样  


#### 生成器

有 yield 关键字，就是一个生成器，就是断点续传；读书读到一半夹一个书签；电影视频暂停  

#### 函数

关键字参数说的是调用的时候指定，可以不用管定义的时候的顺序。比如 def about(name, course, site): print(name, course, site)  调用的时候可以指定，about(site='网址', name='名字', course='课程') 可以打乱顺序  

默认参数是说定义的时候指定的  

不定长参数，就是加 *  
def loop(\*args):   
&emsp;    for x in args:  
&emsp;&emsp;        print(x)  

loop(1, 2, 3)  
loop(1, 3, 5, 7, 9)  

#### 递归函数  

1、函数自己调用自己  
2、有终止条件  


#### 变量的作用域

局部的和全局的  
def f(x):  
&emsp;    laocal_var = 200  

print(local_var) 就会报错，因为局部变量只能在函数内部使用  
如果是在函数外面定义，就是全局变量，在哪里都可以调用  

闭包就是，内部函数引用了外部函数的变量(不是全局变量)，那么内部函数就是闭包  
def outer():  
&emsp;    num = 100  
&emsp;    def inner():  
&emsp;&emsp;        print(num)  
&emsp;    inner()  

outer()  

在这里 inner 可以调用 num 变量  
查找顺序：局部 闭包 全局 内建  

局部不能修改全局变量，如果要修改，就要加上 global 关键字  
nonlocal 就是闭包里修改外部函数的变量  

函数的参数就是局部变量  

#### 模块  

如果使用命令行，关闭以后程序就没有了，所以要存储到文件中。模块可以实现代码重用  

搜索路径，默认是在环境变量中去寻找；运行期间是在 sys.path 中去寻找，sys.path 是一个列表，可以通过 append 添加  

模块在导入的时候就会被执行，为了避免这种情况，办法就是写 if name == \_\_main__  

#### 包

当模块非常多的时候，可以加上一定的逻辑，可以用包来组织模块，包就是文件夹，模块就是文件   

包要有 \_\_init__ 文件  

#### 文件  

最重要的就是 open 函数，有了 open 函数就可以做其他的操作。open(filename, acess_mode='r', encoding='utf-8')  

def open_file():
&emsp;    f = open('test.txt', 'r', encoding='utf-8')  
&emsp;    print(f.read())  

def write_file():
&emsp;    f = open('test.txt', 'w', encoding='utf-8')  
&emsp;    f.write('mayanan')  覆盖写入  

最好是用 with，这样不用再 close  

def open_file():
&emsp;    with open('test.txt','r',encoding='utf-8') as f:
&emsp;        print(f.read())


#### 异常和错误  

错误是在编译期间出现的，比如语法错误，逻辑错误，  

异常是在运行期间出现的，比如算法错误，内存不够。  

如果报了错，下面就不再执行了  

处理异常 try except，原因就是一部分出错，不能影响另一部分工作。比如汽车雨刷坏了不能影响刹车  

程序也是这样，不能因为一个小毛病就崩溃了  

def loop(l):  
&emsp;    try:  
&emsp;&emsp;        print(l[3])  
&emsp;    except Exception as e:  
&emsp;&emsp;        print('error')  

loop([1, 2])
















