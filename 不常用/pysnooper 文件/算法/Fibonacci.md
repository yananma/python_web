
先算加号左边的，一路到底  
画成二叉树，就是先左子树一路走到头，再往上走  

```python 
Starting var:.. n = 4
06:56:38.167264 call         4 def Fibonacci(n):
06:56:38.168260 line         5     if n == 0 or n == 1:
06:56:38.168260 line         7     return Fibonacci(n - 1) + Fibonacci(n - 2)
    Starting var:.. n = 3
    06:56:38.168260 call         4 def Fibonacci(n):
    06:56:38.168260 line         5     if n == 0 or n == 1:
    06:56:38.168260 line         7     return Fibonacci(n - 1) + Fibonacci(n - 2)
        Starting var:.. n = 2
        06:56:38.168260 call         4 def Fibonacci(n):
        06:56:38.168260 line         5     if n == 0 or n == 1:
        06:56:38.168260 line         7     return Fibonacci(n - 1) + Fibonacci(n - 2)
            Starting var:.. n = 1
            06:56:38.168260 call         4 def Fibonacci(n):
            06:56:38.168260 line         5     if n == 0 or n == 1:
            06:56:38.168260 line         6         return n
            06:56:38.168260 return       6         return n
            Return value:.. 1
            Elapsed time: 00:00:00.000000
            Starting var:.. n = 0
            06:56:38.169257 call         4 def Fibonacci(n):
            06:56:38.169257 line         5     if n == 0 or n == 1:
            06:56:38.169257 line         6         return n
            06:56:38.169257 return       6         return n
            Return value:.. 0
            Elapsed time: 00:00:00.000000
        06:56:38.169257 return       7     return Fibonacci(n - 1) + Fibonacci(n - 2)
        Return value:.. 1
        Elapsed time: 00:00:00.000997
        Starting var:.. n = 1
        06:56:38.169257 call         4 def Fibonacci(n):
        06:56:38.169257 line         5     if n == 0 or n == 1:
        06:56:38.169257 line         6         return n
        06:56:38.169257 return       6         return n
        Return value:.. 1
        Elapsed time: 00:00:00.000000
    06:56:38.169257 return       7     return Fibonacci(n - 1) + Fibonacci(n - 2)
    Return value:.. 2
    Elapsed time: 00:00:00.000997
    Starting var:.. n = 2
    06:56:38.169257 call         4 def Fibonacci(n):
    06:56:38.169257 line         5     if n == 0 or n == 1:
    06:56:38.169257 line         7     return Fibonacci(n - 1) + Fibonacci(n - 2)
        Starting var:.. n = 1
        06:56:38.169257 call         4 def Fibonacci(n):
        06:56:38.169257 line         5     if n == 0 or n == 1:
        06:56:38.169257 line         6         return n
        06:56:38.169257 return       6         return n
        Return value:.. 1
        Elapsed time: 00:00:00.000000
        Starting var:.. n = 0
        06:56:38.169257 call         4 def Fibonacci(n):
        06:56:38.169257 line         5     if n == 0 or n == 1:
        06:56:38.170255 line         6         return n
        06:56:38.170255 return       6         return n
        Return value:.. 0
        Elapsed time: 00:00:00.000998
    06:56:38.170255 return       7     return Fibonacci(n - 1) + Fibonacci(n - 2)
    Return value:.. 1
    Elapsed time: 00:00:00.000998
06:56:38.170255 return       7     return Fibonacci(n - 1) + Fibonacci(n - 2)
Return value:.. 3
Elapsed time: 00:00:00.002991
```
