

文档：https://docs.dify.ai/en/introduction     


### 对 python 代码的返回格式有要求  

文档位置：https://docs.dify.ai/en/guides/workflow/node/code    

```python
defmain(arg1:int,arg2:int)->dict:
    return{
        "result": arg1 + arg2
    }
```

#### array   

array[string]: ['a', 'b', 'c']   

array[object]: [{'0': [], '1': []}]  # object 是字典，用的前端的概念   


#### 飞书表格  

插入列的时候，是在最后添加的列，不是在自己数据的后面的列，而是整个 sheet 的列   



#### 开始  

开始，选择插入变量，变量选择 string 类型，可以传飞书 url    

