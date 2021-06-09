
不再使用这个版本  

```python 
import requests
from bs4 import BeautifulSoup
import pprint
import json


def download_all_htmls():
    urls = [f'http://www.crazyant.net/page/{page}' for page in range(1, 35)]
    htmls = []
    for url in urls:
        r = requests.get(url)
        print(url)
        if r.status_code != 200:
            raise Exception('exception')
        htmls.append(r.text)
    return htmls


def parse_single_html(html):
    soup = BeautifulSoup(html, 'html.parser')
    articles =soup.find_all('article')
    datas = []
    for article in articles:
        title_node = (
            article
            .find('h2', class_='entry-title')
            .find('a')
        )
        title = title_node.get_text()
        link = title_node["href"]

        datas.append({'title': title, 'link': link})
    return datas


def write_to_file(content):
    with open('result.json', 'a') as f:
        f.write(json.dumps(content, ensure_ascii=False) + '\n')


if __name__ == '__main__':
    htmls = download_all_htmls()
    all_datas = []
    for html in htmls:
        all_datas.extend(parse_single_html(html))
    for data in all_datas:
        write_to_file(data)
    print('程序执行完毕')
```
