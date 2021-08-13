
### 前言  

每当我通过编写程序解决了一个问题时，都非常高兴  

编写函数，可以重用，用多少次都可以  


### 第1章 起步  



### 第2章 变量和简单的数据类型  

在程序中可随时修改变量的值，而 Python 讲始终记录变量的最新值。  

变量是标签。  

#### 字符串  

对数据进行分类大有裨益。  

字符串看似简单，但是能够以很多不同的方式使用。  

字符串就是一系列字符。在 Python 中，用引号括起来的都是字符串，其中引号可以是单引号，也可以是双引号。这种灵活性可以让我们能够在字符串中包含引号和撇号。  

字符串常用方法：title()、upper()、lower() 等等  

字符串方法看源码和注释。  

使用 f 字符串可以实现在字符串中使用变量的值。  

```python  
In [1]: first_name = "ada"

In [2]: last_name = "lovelace"

In [3]: full_name = f"{first_name} {last_name}"

In [4]: full_name
Out[4]: 'ada lovelace'
```

可以使用 f 字符串可以利用变量拼接出来完整的信息。   

```python 
In [6]: f"Hello {full_name.title()}"
Out[6]: 'Hello Ada Lovelace'
```



