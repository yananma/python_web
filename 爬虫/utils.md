
保存视频  

```python
def write_to_file(r):
    with open('a.mp4', 'ab+') as f:
        f.write(r.content)  
```

多线程，还要学一下怎么设置线程数量    

```python 
def multi_tread():
    threads = []
    for url in urls:
        thread = threading.Thread(target=blog_spider.craw, args=(url,))
        threads.append(thread)

    for thread in threads:
        thread.start()

    for thread in threads:
        thread.join()
```
