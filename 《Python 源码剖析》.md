
# 第1部分 Python内建对象

## 第1章 Python对象初探

在 Python 中，一切皆对象  

通常的说法是，对象是数据以及基于这些数据的操作的集合。在计算机上，一个对象实际上就是一片被分配的内存空间，这些内存可能是连续的，也有可能是离散的，这都不重要，重要的是这片内存在更高的层次上可以作为一个整体来考虑，这个整体就是一个对象。  

在 Python 中，一个对象一旦被创建，它在内存中的大小就是不变的了。这就意味着那些需要容纳可变长度数据的对象只能在对象内维护一个指向一个可变大小的内存区域的指针。  

在 Python 中，所有的东西都是对象，而所有的对象都拥有一些相同的内容，这些内容在 PyObject 中定义，PyObject 是整个 Python 对象机制的核心。  

```c
[object.h]
typedef struct _object {
    PyObject_HEAD
} PyObject;
```

实际上，PyObject 是 Python 中不包含可变长度数据的对象的基石，而对于包含可变长度数据的对象，它的基石是 PyVarObject：  
```c
[object.h]
typedef struct {
    PyObject_VAR_HEAD
} PyVarObject;
```

这两个结构体构成了 Python 对象机制的核心基石。  

在 Python 中，每一个对象都拥有相同的对象头部。这就使得在 Python 中，对对象的引用变得非常的统一。  

```c
#define PyObject_HEAD \
    _PyObject_HEAD_EXTRA \
    int ob_refcnt; \
    struct _typeobject *ob_type;
``` 

```c
#define PyObject_VAR_HEAD \
    PyObject_HEAD \
    int ob_size; /* Number of items in variable part */
```

在 PyObject_HEAD 的定义中，我们注意到有一个 ob_refcnt 的整形变量，这个变量的作用是实现引用计数机制。对于某一个对象 A，当有一个新的 PyObject\*引用该对象时，A 的引用计数应该增加；而当这个 PyObject \*被删除时，A 的引用计数应该减少。当 A 的引用计数减少到 0 时，A 就可以从堆上被删除，以释放出内存供别的对象使用。  

在 PyObject_HEAD 中，我们注意到 ob_type 是一个指向_typeobject 结构体的指针，那么这个结构体是一个什么东西呢？实际上这个结构体也是一个对象，它是用来指定一个对象类型的类型对象。  

在 Python 中实际上对象机制的核心非常的简单，一个是引用计数，一个就是类型。  

而对于拥有可变长度数据的对象，这样的对象通常都是容器，我们可以在 PyObject_VAR_HEAD 中看到 ob_size 这个变量，这个变量实际上就是指明了该对象中一共包含了多少个元素。  

#### 引用计数  

在 C 或 C++中，程序员被赋予了极大的自由，可以任意地申请内存。但是权利的另一面则对应着责任，程序员必须自己负责将申请的内存释放，并释放无效指针。可以说，这一点正是万恶之源，大量的内存泄露和悬空指针的 bug 由此而生，如黄河泛滥一发不可收拾

现代的开发语言中一般都选择由语言本身负责内存的管理和维护，即采用了垃圾收集机制，比如 Java 和 C#。垃圾收集机制使开发人员从维护内存分配和清理的繁重工作中解放出来，这样做的好处是提高了开发效率，并降低了 bug 发生的机率。Python 同样也内建了垃圾收集机制，代替程序员进行繁重的内存管理工作，而引用计数正式 Python 垃圾收集机制的一部分。  

Python 通过对一个对象的引用计数的管理来维护对象在内存中的生存。我们知道在 Python 中每一个东西都是一个对象，都有一个 ob_refcnt 变量，正是这个变量维护着该对象的引用计数，从而也最终决定着该对象的生生灭灭。  

在 Python 中，主要是通过 Py_INCREF(op)和 Py_DECREF(op)两个宏来增加和减少一个对象的引用计数。当一个对象的引用计数减少到 0 之后，Py_DECREF 将调用该对象的析构函数（deallocator function）来释放该对象所占有的内存和系统资源。  

## 第2章 Python中的整数对象  



