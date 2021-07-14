
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

第2章 Python中的整数对象  

Python 中的整数是通过 PyIntObject 对象来实现的。PyIntObject 的对象是一个不变(immutable)对象，也就是说，在创建了一个 PyIntObject 的对象之后，我们就再也不能改变该对象的值了。  

```c
[intobject.h]
typedef struct {
    PyObject_HEAD
    long ob_ival; 
} PyIntObject;
``` 

可以看到，Python 中的 PyIntObject 实际上就是对 C 中 long 的一个简单包装。  


## 第4章 Python 中的 List 对象  

元素的一个群是一个非常重要的抽象概念，我们可以将符合某一特性的一堆元素聚集为一个群，当然，还要可以向群中添加或删除元素。这样的群的概念对于编程语言十分重要，C 语言就内建了数组的概念，随着编程语言的发展，现在所有的编程语言都会在语言中或标准库中实现这样的群的概念。而且群的概念还进一步地细分为多种实现方式，比如 map，vector 等。每一种实现都为某种目的的元素聚集或元素访问提供了极大的方便。  

PyListObject 对象可以有效地支持插入，添加，删除等操作，在 Python 的列表中，无一例外地存放的都是 PyObject 的指针。  

很显然，PyListObject 一定是一个变长对象，因为不同的 list 中存储的元素的个数会是不同的。但是，PyListObject 对象还支持插入删除等操作，可以在运行时动态地调整其所维护的内存，所以，它还是一个可变对象。  

```c
[listobject.h] 
typedef struct {
    PyObject_VAR_HEAD
    /* Vector of pointers to list elements. list[0] is ob_item[0], 
    etc. */
    PyObject **ob_item;    # 这里是指针的指针，也就是说有两层
    int allocated;     # 内存
} PyListObject;
``` 

PyListObject 并不是存了多少东西就申请对应大小的内存，这样的申请策略显然是低效的，因为用户选用列表正是为了频繁地插入删除元素。因此，PyListObject 在每一次需要申请内存的时候，会申请一大块内存，这是申请的总内存的大小记录在allocated 中，而这些内存中实际被有效的 PyObject\*占用的内存大小被记录在了 ob_size 中。  

PyObject_VAR_HEAD 中的 ob_size 就是列表元素的个数，和 len(list) 是相等的。  


#### 创建  

Python 中只提供了唯一一种创建 PyListObject 对象的方法—PyList_New：
```c
[listobject.c] 
PyObject* PyList_New(int size) 
{
    PyListObject *op;
    size_t nbytes;
    
    nbytes = size * sizeof(PyObject *);
    /* Check for overflow */
    if (nbytes / sizeof(PyObject *) != (size_t)size)
        return PyErr_NoMemory();
        
    //为 PyListObject 申请空间
    if (num_free_lists) { 
        //使用缓冲池
        num_free_lists--;
    op = free_lists[num_free_lists];
    _Py_NewReference((PyObject *)op);
   } else { 
        //缓冲池中没有可用的对象，创建对象
        op = PyObject_GC_New(PyListObject, &PyList_Type);
   } 
   //为 PyListObject 对象中维护的元素列表申请空间
    if (size <= 0)
        op->ob_item = NULL;
    else {
        op->ob_item = (PyObject **) PyMem_MALLOC(nbytes);
        memset(op->ob_item, 0, nbytes);
    }
    op->ob_size = size;
    op->allocated = size;
    _PyObject_GC_TRACK(op);
    return (PyObject *) op; 
}
```

首先进行一些例行检查；然后为 PyListObject 申请内存空间，创建 PyListObject 对象。再成功创建 PyListObject 对象之后，就需要为这个对象申请存储PyObject\*的内存空间，内存空间的大小由传入的参确定，传入的参数决定了新创建的 PyListObject 可以容纳多少个 PyObject*。最后将 PyListObject 对象的存储区域清空，并将 ob_size 和 allocated 都设置为 size，为内存管理做好准备。  

我们看到，在 list 的实现中，同样用到了缓冲池的技术，创建 PyListObject 的时候会首先检查 free_lists 中是否还有没有使用的 PyListObject，如果有就直接使用，只有在 free_lists中的 PyListObject 全部用完之后才会通过 malloc 在堆上创建新的 PyListObjec。free_lists 的默认大小为 80，对于一般的小程序而言，基本上只会使用到 PyListObject 缓冲池。  

```c
/* Empty list reuse scheme to save calls to malloc and free */
#define MAXFREELISTS 80 
static PyListObject *free_lists[MAXFREELISTS]; 
static int num_free_lists = 0;
```

```
[listobject.c] 
int PyList_SetItem(register PyObject *op, register int i, register PyObject *newitem) 
{
    register PyObject *olditem;
    register PyObject **p;
    if (!PyList_Check(op)) {
        ……
    }
    if (i < 0 || i >= ((PyListObject *)op) -> ob_size) {
        Py_XDECREF(newitem);
        PyErr_SetString(PyExc_IndexError,
            "list assignment index out of range");
        return -1;
    }
    p = ((PyListObject *)op) -> ob_item + i;
    olditem = *p;
    *p = newitem;
    Py_XDECREF(olditem);
    return 0; 
}
```

#### 添加  
```c
[listobject.c] 
int PyList_Insert(PyObject *op, int where, PyObject *newitem) {
    ......//类型检查
    return ins1((PyListObject *)op, where, newitem);
}

static int ins1(PyListObject *self, int where, PyObject *v) {
    int i, n = self->ob_size;
    PyObject **items;
    ......
    if (list_resize(self, n+1) == -1)
        return -1;
        
    if (where < 0) {
    where += n;
    if (where < 0)
        where = 0;
    }
    if (where > n)
        where = n;
    items = self->ob_item;
    for (i = n; --i >= where; )
        items[i+1] = items[i];
    Py_INCREF(v);
    items[where] = v;
    return 0; 
}
```

我们看到，调用了一个 list_resize 函数，从函数名我们可以想象，这个函数改变了 PyListObject 所维护的 PyObject\* 列表的大小：  
```c
[listobject.c]
static int list_resize(PyListObject *self, int newsize) {
    PyObject **items;
    size_t new_allocated;
    int allocated = self->allocated;

    /* Bypass realloc() when a previous overallocation is large enough
    to accommodate the newsize. If the newsize falls lower than half
    the allocated size, then proceed with the realloc() to shrink 
    the list.
    */
    if (allocated >= newsize && newsize >= (allocated >> 1)) {
        assert(self->ob_item != NULL || newsize == 0);
        self->ob_size = newsize;
        return 0;
    }

    /* This over-allocates proportional to the list size, making room
    * for additional growth. The over-allocation is mild, but is
    * enough to give linear-time amortized behavior over a long
    * sequence of appends() in the presence of a poorly-performing
    * system realloc().
    * The growth pattern is: 0, 4, 8, 16, 25, 35, 46, 58, 72, 88, ...
    */

    new_allocated = (newsize >> 3) + (newsize < 9 ? 3 : 6) + newsize;
    if (newsize == 0)
        new_allocated = 0;
    items = self->ob_item;
    if (new_allocated <= ((~(size_t)0) / sizeof(PyObject *)))
        PyMem_RESIZE(items, PyObject *, new_allocated);
    else
        items = NULL;
    if (items == NULL) {
        PyErr_NoMemory();
        return -1;
    }
    self->ob_item = items;
    self->ob_size = newsize;
    self->allocated = new_allocated;
    return 0; 
}
```

PyListObject 的空间调整之后，接着就应该搬动元素了，挪出一个位置，插入我们想要插入的元素。  

```c
static int ins1(PyListObject *self, int where, PyObject *v) 
{
    ......
    if (where < 0) {
        where += n;
        if (where < 0)
            where = 0;
    }
    if (where > n)
        where = n;
    items = self->ob_item;
    for (i = n; --i >= where; )
        items[i+1] = items[i];
    Py_INCREF(v);
    items[where] = v;
    return 0; 
}
```

可以看到，不管你插入在什么位置，对于 Python 来说，都是合法的，它会自己调整插入的位置。在确定了插入的位置之后，会将插入点之后的所有元素向下挪动一个位置，这样，在插入点就能空出一个位置来。  

Python 中，list 有一个被广泛使用的操作 append。append 与上面的插入操作非常相似。  

```c
[listobject.c]
int PyList_Append(PyObject *op, PyObject *newitem) {
    if (PyList_Check(op) && (newitem != NULL))
        return app1((PyListObject *)op, newitem);
    PyErr_BadInternalCall();
    return -1; 
}
``` 

```c
static PyObject* listappend(PyListObject *self, PyObject *v) {
    if (app1(self, v) == 0)
        Py_RETURN_NONE;
    return NULL; 
}
```

```c
static int app1(PyListObject *self, PyObject *v) {
    int n = PyList_GET_SIZE(self);
    ......
    if (list_resize(self, n+1) == -1)
        return -1;
    Py_INCREF(v);
    PyList_SET_ITEM(self, n, v);
    return 0; 
}    
``` 

#### 删除  

当执行 l.remove() 时，PyListObject 中的 listremove 操作会被激活：  
```c
[listobject.c] 
static PyObject * listremove(PyListObject *self, PyObject *v) {
    int i;
    for (i = 0; i < self->ob_size; i++) {
        int cmp = PyObject_RichCompareBool(self->ob_item[i], v, Py_EQ);
        if (cmp > 0) {
            if (list_ass_slice(self, i, i+1,(PyObject *)NULL) == 0) Py_RETURN_NONE;
            return NULL;
        }
        else if (cmp < 0)
            return NULL;
    }
    PyErr_SetString(PyExc_ValueError, "list.remove(x): x not in list");
    return NULL;
```

在遍历 PyListObject 中所有元素的过程中，将待删除的元素与 PyListObject 中的每个元素一一进行比较，比较操作是通过 PyObject_RichCompareBool 完成的。如果发现了匹配，则调用 list_ass_slice 进行删除操作：  
```c
[listobject.c]
static int list_ass_slice(PyListObject *a, int ilow, int ihigh, PyObject *v) 
{ 
    PyObject *recycle_on_stack[8];
    PyObject **recycle = recycle_on_stack; /* will allocate more if needed */
    PyObject **item;
    int n; /* # of elements in replacement list */
    int norig; /* # of elements in list getting replaced */
    int d; /* Change in size */
#define b ((PyListObject *)v)
    if (v == NULL)
    n = 0;
    else { 
    ……
    }

    norig = ihigh - ilow;
    d = n - norig;
    item = a->ob_item;
    //[1] 
    s = norig * sizeof(PyObject *);
    if (s > sizeof(recycle_on_stack)) {
        recycle = (PyObject **)PyMem_MALLOC(s);
        if (recycle == NULL) {
            PyErr_NoMemory();
            goto Error;
        }
    }
    memcpy(recycle, &item[ilow], s); 
    
    //[2] 
    if (d < 0) { /* Delete -d items */
        memmove(&item[ihigh+d], &item[ihigh], (a->ob_size - ihigh)*sizeof(PyObject *));
        list_resize(a, a->ob_size + d);
        item = a->ob_item;
    }
    ……
    //[3] 
    for (k = norig - 1; k >= 0; --k)
        Py_XDECREF(recycle[k]);
#undef b
}
```

当传入的 v 是 NULL 时，就会进行删除的动作，可以看到，这正是 listremove 期望的动作。首先会获得需要删除的元素个数，这是通过 ihigh-ilow 得到的，在删除元素这种情况下，这个值显然是 1。在获得了需要删除的元素个数之后，在代码的[2]处，list_ass_slice 通过 memmove 来达到删除元素的目的。  



