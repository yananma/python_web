
可以替换成任意图片地址链接  

```python 
import requests 

r = requests.get("https://www.baidu.com/favicon.ico")  

with open("favicon.ico", "wb") as f:
    f.write(r.content) 
```
