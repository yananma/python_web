
题目描述  
定义栈的数据结构，请在该类型中实现一个能够得到栈中所含最小元素的min函数（时间复杂度应为O（1））。  


思想就是用空间换时间，开一个新栈，此栈与数值栈一一对应，在元素入栈时，就记录处于每一个位置时的当前最小值，这样不论什么情况，不论之前如何出栈入栈，都能立即获取到最小值。  

```python 
# -*- coding:utf-8 -*-
class Solution:
    def __init__(self):
        self.stack = []
        self.min_stack = []

    def push(self, node):
        self.stack.append(node)
        if self.min_stack and self.min_stack[-1] < node:
            self.min_stack.append(self.min_stack[-1])    # 开辟的新栈不是和原来的栈一样，而是记录该位置时的最小值；元素个数是一样的，记录的是有这个元素的时候的最小值    
        else:
            self.min_stack.append(node)

    def pop(self):
        if self.stack:
            self.min_stack.pop()
            return self.stack.pop()
        return None 

    def top(self):
        if self.stack:
            return self.stack[-1]
        return None 
    
    def min(self):
        if self.min_stack:
            return self.min_stack[-1]
        return None  
```

