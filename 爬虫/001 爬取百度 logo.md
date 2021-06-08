
可以替换成任意图片地址链接，视频也是同样的代码    

```python 
import requests 

r = requests.get("https://www.baidu.com/favicon.ico")  

with open("favicon.ico", "wb") as f:
    f.write(r.content) 
```
