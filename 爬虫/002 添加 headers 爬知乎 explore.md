
```python
import requests

headers = {
'user-agent':'Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/90.0.4430.212 Safari/537.36'
}

r = requests.get("https://www.zhihu.com/explore", headers=headers)
print(r.text)
```
