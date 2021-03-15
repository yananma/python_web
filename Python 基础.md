
Python 里 . 就是的，views.banner 就是 views 里面的 banner 函数   

#### 变量和数据类型  

数据类型：数字(整数浮点数)、字符串 ''、列表 []，列表可以遍历、元组()、字典 {} 括起来的键值对、类的实例和函数等

type() 看类型  

#### 编码规范  

4 个空格缩进；顶级定义之间空两行，比如 class，类中的方法之间空一行；二元操作符前后空格，比如四则运算符号，用 = 指定参数默认值的时候，前后不要有空格。 

类名称首字母大写，其他除全局变量外都是小写加下划线  


#### 注释  

单行注释井号，多行注释三引号  

文档字符串，类或函数的第一句话，可以用自带的 \_\_doc__ 函数访问  

多写注释，不用就忘。  

一个普通人加上记笔记的习惯就可以成为一个天才。  


#### 编程基础

占位符，

    name = 'mayanan' 
    age = 30  
    print('%s, %d' % (name, age))  

占位符的读法是，读到哪一个就把后面的名字提到前面来读  

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

r 就是 raw，按照原始的字符串输出，读路径的时候常用  

#### 列表  

列表方法：append、insert、remove、pop、clear、count、sort、reverse、  

列表推导式：`[x**2 for x in range(5)]`  


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

`l = ['享学', 'Python', 'mayanan']`  

`it = iter(l)`  这个就是迭代器  

`print(next(it))`    享学  
`print(next(it))`    Python  
`print(next(it))`    mayanan    
就是有一个指针一样  


#### 生成器

有 yield 关键字，就是一个生成器，就是断点续传；读书读到一半夹一个书签；电影视频暂停  

#### 函数

关键字参数说的是调用的时候指定，可以不用管定义的时候的顺序。比如 

    def about(name, course, site): 
        print(name, course, site)  
    
调用的时候可以指定，`about(site='网址', name='名字', course='课程')` 可以打乱顺序  

默认参数是说定义的时候指定的  

不定长参数，就是加 *  

    def loop(*args):   
        for x in args:  
            print(x)  

    loop(1, 2, 3)  
    loop(1, 3, 5, 7, 9)  
    

#### 递归函数  

1、函数自己调用自己  
2、有终止条件  


#### 变量的作用域

局部的和全局的  

    def f(x):  
        lacal_var = 200  

print(local_var) 就会报错，因为局部变量只能在函数内部使用  
如果是在函数外面定义，就是全局变量，在哪里都可以调用  

闭包就是，内部函数引用了外部函数的变量(不是全局变量)，那么内部函数就是闭包  

    def outer():  
        num = 100  
        def inner():  
            print(num)  
        inner()  

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
        f = open('test.txt', 'r', encoding='utf-8')  
        print(f.read())  

    def write_file():  
        f = open('test.txt', 'w', encoding='utf-8')  
        f.write('mayanan')  覆盖写入  


最好是用 with，这样不用再 close  

    def open_file():  
        with open('test.txt','r',encoding='utf-8') as f:  
            print(f.read())  


    def write_file():
        with open('test.py', 'w', encoding='utf-8') as f:
            f.write('Hello World!')

    write_file()


#### 异常和错误  

错误是在编译期间出现的，比如语法错误，逻辑错误，  

异常是在运行期间出现的，比如算法错误，内存不够。  

如果报了错，下面就不再执行了  

处理异常 try except，原因就是一部分出错，不能影响另一部分工作。比如汽车雨刷坏了不能影响刹车  

程序也是这样，不能因为一个小毛病就崩溃了  

    def loop(l):  
        try:  
            print(l[3])  
        except Exception as e:  
            print('error')  

    loop([1, 2])

try except 的时候一般会 print 错误信息，否则不知道错在什么地方  

finally 不管有没有异常都会执行，比如 close 文件，关闭数据库等等  

#### raise 和 assert  

raise 是主动抛出异常，assert 是断言，满足条件才往下执行  

#### 自定义异常

类要继承 Exception 类，要重写 \_\_init__ 和 \_\_str__ 方法，可以用 raise 抛出异常  

#### 面向对象  

抽象、封装、继承、多态  
封装，比如汽车，最后留给我们的只有几个方向盘，刹车等几个接口，发动机、变速箱等都封装了起来  

类是抽象的，是一个模板；对象是具体的，是类的一个实例  

函数放到类里就叫做方法，其实就是函数  

构造方法就是 \_\_init__，作用就是初始化实例变量，当实例化对象时，一定会调用构造方法  

self 关键字，self 翻译过来就是我自己，指当前对象本身，谁调用该方法，当前对象就是谁；在类里面的方法的第一个关键字必须是 self；self 就是 this，翻译成这个实例的  

验证 self 就是实例本身代码  

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

id 相同，所以就验证了 self 就是这个实例本身  

最开始初始化的时候，写 self.name = name 就是要区分参数和实例变量，否则分不清  

#### 类方法静态方法和实例方法  

实例方法必须实例化才能调用，就是最常用的那种方法  

静态方法不需要实例化，通过名称就可以直接访问，静态方法不加 self  

    class Site(object):  
        @staticmethod  
        def get_name():  
            return 'mayanan'  

    name = Site.get_name()  
    print(name)  

不用实例化  

类方法用的不多，用的是 @classmethod，第一个参数必须是 cls 类本身  

#### 类属性和实例属性(属性就是变量)  

实例属性就是实例变量，self.name = name，前面的 self.name 就是实例属性  

下面这样的就是类属性，实例方法可以访问类属性  

    class Site(object):  
        name = 'mayanan'     
        course = 'Python'  


#### 继承  

可以继承父类里面所有的属性和方法，不用再从头构建    

多重继承，可以继承多个类  

非常清楚的一个例子  

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
    

#### 方法覆盖  

必须是继承关系；子类覆盖(重写)父类里面的同名方法  

既可以复用，又可以保证灵活性，可以根据实际情况修改定制  

    class Animal(object):  
        def run(self):  
            print('Animal run...')  
            
        def sleep(self):  
            print('Animal sleep...')  


    class Dog(Animal):  
        def run(self):  
            print('dog run...')  


    hua = Dog()  

    hua.run()  
    hua.sleep()  


#### super 关键字 

调用父类的初始化方法 super().\_\_init__()  
调用父类的其他属性和方法  

    class Person(object):  
        def __init__(self, name, age):  
            self.name = name  
            self.age = age  
        
        def display(self):  
            print(self.name, self.age)  

    class Manager(Person):  
        def __init__(self):  
            super().__init__('mayanan', 26)  
    
        def m_display(self):  
            super().display()  

    m = Manager()  
    m.m_display()  


#### isinstance 

isinstance(obj, cls)  

判断一个实例是不是一个类的实例  

#### 属性操作  

hasattr()、getattr()、setattr()、delattr()  

    class Person(object):  
        def __init__(self, name):  
            self.name = name  

    p = Person('mayanan')  
    print(hasattr(p, 'name')) True  
    print(getattr(p, 'name')) 就是 p.name  
    setattr(p, 'name', 'mayanan')  
    print(p.name)  
    delattr(p, 'name')  
    print(hasattr(p, 'name')) False   


#### 序列化和反序列化  

对象序列化就是把对象保存成文件格式，用 pickle.dumps()  
反序列化就是把对象从文件转化为对象，用 pickle.load()  

因为一般情况下，结束以后内容就消失了，所以有了序列化    

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
    

#### 多线程  

多进程是系统中的多个应用程序，比如同时打开 WPS、QQ、音乐、浏览器等等；打开任务管理器，看到开的应用就是进程  
线程是一个应用程序的多个执行线路，这样就不会产生阻塞，用户不用等待；比如 web 服务器针对不同用户的请求，启动不同的线程来相应，不用排队；  

如果没有多线程，就会顺序执行，不管第一个函数执行多长时间，后面的函数都会等待  

不使用线程代码，就是先打印 5 个 i，i 打印完了以后再打印 j    

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

使用线程交替执行，不是顺序执行的，而是并行执行的  

相当于买票的时候，原来只有一个窗口，只能这一队人排完以后，才能开始另一队；多线程就是有多个窗口买票  

使用线程代码，这个 thread 模块，只能在 python2 版本中才能运行，但是可以便于理解多线程  

    import thread  
    from time import ctime, sleep  

    def func1():  
        for i in range(5):  
            print('i=:', i)  
            sleep(1)  

    def func2():  
        for j in range(5):  
            print('j=:', j)  
            sleep(1)  

    def main():  
        print('start:', ctime())  
        thread.start_new_thread(func1, ())  
        thread.start_new_thread(func2, ())  
        sleep(5)  
        print('end:', ctime)  

    if __name__ == '__main__':  
        main()  

现实中不使用 sleep 函数，因为不知道运行多长时间，现实中使用 lock  

python3 中使用的是 threading 模块，有 3 种方法，第一种是创建 Thread 实例，为 target 函数传递一个参数；第二种是创建 Thread 实例，传递给一个可调用的类实例，需要复写 \_\_call__ 函数；第三种是继承 Thread，并创建子类的实例  

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


#### 线程同步  

多个用户同时操作一个共享资源，要对共享资源进行保护，方法就是使用 lock。  

比如现实中火车站，4 个窗口卖 100 张票，就要用 lock 线程，否则会卖重复  

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
        

如果把程序中的 lock 去掉，就会有卖重复的现象  

queue 模块使得共享数据更加方便，不用再用 lock，不用再自己控制，queue 自己内部就实现了这些功能  

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


#### 网络编程  

客户端服务器，客户端发送请求，服务器返回响应  

socket 就是插座，4 个部分连接上以后才是一个 socket，ip 端口 ip 端口。互联网上有成千上万台机器，一台机器如何找到另一台机器呢？办法就是 IP 地址，每一台机器都有唯一的 IP 地址。另一个问题是，一台电脑有几百个应用，怎么区分应用呢？答案就是端口号。socket 由 IP 地址和端口号组成，想要请求应用程序的服务，就必须要知道 IP 地址和端口号，有了 IP 地址和端口号以后就能定位到这个应用，就能实现连接，连接以后就可以实现数据的收发。有点儿像访问阿里云的 docker  

服务器先绑定一个端口号，然后 listen 监听，客户端再根据 IP 地址和端口号连接服务器，如果服务器接受了连接，就可以实现读写，数据传输  

网络连接一般分为两种，一种是面向连接的 TCP，必须要先建立连接才能实现，分片段传输，传输是可靠的，使用的协议是 TCP 协议，SOCKET_STREAM；另一种是无连接的 UDP，不需要连接，整体发送，不能保证可靠性，SOCKET_DGRAM  


#### TCP  

TCP 客户端  

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


TCP 服务器  

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


UDP 客户端  

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


UDP 服务器 

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




### Python 多进程和多线程  

多任务，比如百度网盘同时下载多部电影  
好处：提高 CPU 资源利用率，降低时间  

多任务是指在**同一时间**执行**多个任务**  

并发：交替执行，比如一个 CPU 执行多个任务  
并行：任务量小于或等于 CPU 核数  

不使用多进程和多线程的时候，就是顺序执行，先执行完 sing 函数，再执行 dance 函数  

#### 进程  

进程是资源分配的最小单位，它是操作系统进行资源分配和调度运行的基本单位。通俗地说，一个正在运行的程序就是一个进程；Windows 任务管理器  

使用 pysnooper 可以看到这两个函数是同时执行的  

    import time
    import multiprocessing

    def sing(num):
        for i in range(num):
            print('唱歌......')
            time.sleep(0.5)

    def dance(num):
        for i in range(num):
            print('跳舞......')
            time.sleep(0.5)


    if __name__ == "__main__":
        # 通过进程类，创建进程对象
        sing_process = multiprocessing.Process(target=sing, args=(3, ))
        dance_process = multiprocessing.Process(target=dance, kwargs={'num': 3})

        sing_process.start()
        dance_process.start()  
        
        
主进程会等待子进程执行结束以后才结束，可以设置 daemon=True 守护主进程，使得主进程执行结束以后，子进程自动销毁，程序结束  


#### 线程  
为什么要使用线程？  
进程是分配资源的最小单位，一旦创建一个进程就会分配一定的资源，有时是比较浪费资源  

线程是程序执行的最小单位，实际上进程只负责分配资源，而利用这些资源执行程序的是线程。进程是线程的容器，一个进程中最少有一个线程来负责执行程序。同时线程自己不拥有系统资源，只需要一点必不可少的资源，它可以和同属一个进程的其他线程共享进程所拥有的全部资源。  

    import time
    import threading


    def sing(num):
        for i in range(num):
            print("唱歌......")
            time.sleep(0.5)


    def dance(num):
        for i in range(num):
            print("跳舞......")
            time.sleep(0.5)


    if __name__ == "__main__":
        sing_thread = threading.Thread(target=sing, args=(3, ))
        dance_thread = threading.Thread(target=dance, kwargs={'num': 3})

        sing_thread.start()
        dance_thread.start()

线程之间的执行是无序的，是由 CPU 调度决定的  

进程可以使用多核，线程不可以使用多核  







