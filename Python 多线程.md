


## [2小时玩转python多线程编程](https://www.bilibili.com/video/BV1fz4y1D7tU?from=search&seid=15504173216158754497)  

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


## [Python 并发编程实战，用多线程、多进程、多协程](https://www.bilibili.com/video/BV1bK411A7tV?p=13&spm_id_from=pageDriver)  

比如爬虫，顺序执行可能要 1 个小时，并发只需要 10 分钟  
比如请求网页，优化每次打开页面需要 3 秒，并发只需要 500 毫秒  

提高执行速度  

本质上是因为 IO 和 CPU 之间是可以并行执行的，IO 读取写入磁盘是不需要 CPU 的参与的  

单线程、**多线程并发 threading**、**多 CPU 并行 multiprocessing**、多机器并行(handoop/spark/hive)  

asyncio，异步 IO，在单线程中利用 CPU 和 IO 同时执行的原理，实现异步执行  


CPU 密集型计算(CPU bound)，也叫计算密集型，就是 CPU 限制了整体，IO 耗时很短，CPU 需要大量的计算和处理，特点是 CPU 使用率很高；比如加密解密、比如压缩解压  

IO 密集型(IO bound) 是说 CPU 大部分时间都在等待 IO 读取写入磁盘，CPU 使用率很低；比如数据库处理、爬虫下载、文件处理程序     

一个进程中可以包含多个线程，一个线程中可以启动多个协程，比如几万个  


1. 多进程 process  
利用多 CPU 并行计算  
占用资源多，可启动数目受 CPU 数限制，比较少  
适用于 CPU 密集型计算  

2. 多线程 thread  
相比多进程，可用数目多，占用资源少  
在 python 中，多线程执行并发执行，不能利用多 CPU 执行(GIL)  
适用于 IO 密集型计算，且启用数目不太多  

3. 多协程 Coroutine(asyncio)  
内存开销最少，启动数目最多  
很多库不支持，代码实现比较复杂  
适用于 IO 密集型计算，需要超多任务执行，有库支持  

根据任务特点，选择使用的技术  


全局解释器锁 (Global Interpreter Lock GIL)  
GIL 导致 python 无法利用多 CPU 并行执行  

GIL 是计算机编程语言解释器用于同步线程的一种机制，它使得任何时刻只有一个线程在执行，即使是在多核设备上，同一时间也只允许执行一个线程  

When a thread is running, it holds the GIL  

GIL 是设计之初是为了规避并发的数据同步问题而引入的，它简化了对共享资源的管理问题  

因为在 IO 期间，线程会释放 GIL，所以对于 IO 密集型计算，依然会大幅提升速度，但是对于 CPU 密集型计算，则会大幅降低速度  

为了应对 GIL 问题，python 引入了 multiprocessing 模块  

代码下载练习，写上，第 4 课  


线程池，不用创建释放线程，而是复用线程  



多进程和多线程的语法几乎一样，就是为了方便迁移而设计的  








