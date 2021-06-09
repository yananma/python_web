
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

下载  

```python
def download(url, name):
    global count
    count = count + 1
    r = requests.get(url, timeout=100)
    with open("F:/crawling/" + str(count) + '.' + str(name) + '.jpg', 'wb') as f:
        f.write(r.content)
    print('已打印第{}张图片'.format(count))
```
