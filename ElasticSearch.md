
### 查  
查看所有索引，得出结果以后 Ctrl + F 搜索索引名    
`GET _cat/indices?v`  

查看索引字段  
`GET kejisousou`  

查看所有别名  
`GET _alias`  

用通配符查看特定别名  
`GET kejisousou*/_alias`  

查看所有模板  
`GET _template`  

用通配符查看特定模板  
`GET _template/kejisousou*`


在所有索引中查询，就是不指定索引名查询  

```python 
GET _search
{}
```

查询 url 的时候，http 和 https 都试一试。有时候 http 查不出来，用 https 就能查出来。  

query_string 查询  

```python 
GET test-zky/_search
{
  "query": {
    "bool": {
      "should": [
        {
          "query_string": {
            "default_field": "text",
            "query":' OR '.join(f'"{data}"' for data in source_data)
          }
        }
      ]
    }
  },
  "_source": ["title","text","url","post_time"],
  "size": 1000
}
``` 

多条件查询（这里是 temp_titles 的精确查询，所以用了 term，查的是 title.keyword）  

must 是 and 查询  

should 是 or 查询  

```python 
query_dict = {
    "query": {
        "bool": {
            "must": [
                {
                    "bool": {
                        "should": [

                        ]
                    }
                },
                {
                    "range": {
                        "post_time": {
                            "gte": "2021-05-04 00:00:00",
                            "lt": "2021-08-05 00:00:00"
                        }
                    }
                }
            ]
        }
    },
}
for data in source_data:
    query_dict["query"]["bool"]['must'][0]['bool']['should'].extend([
        {"term": {
            "title.keyword": {
                "value": data
            }
        }
        }
    ])
```

用 sort 排序实现查询第一条和最后一条  
```python 
GET kejisousou-test/_search
{
  "size": 1,
  "_source": "post_time",
  "sort": [
    {
      "post_time": {
        "order": "asc"
      }
    }
  ]
}
```


反向过滤 must_not   

```python 
GET kejisousou-points-test/_search
{
  "query": {
    "bool": {
      "must": [
        {
          "query_string": {
            "fields": [
              "point_text"
            ],
            "query": "5G"
          }
        },
        {
          "bool": {
            "must_not": [
              {
                "prefix": {
                  "entry_name.keyword": {
                    "value": "知乎"
                  }
                }
              },
              {
                "prefix": {
                  "entry_name.keyword": {
                    "value": "微博"
                  }
                }
              }
            ]
          }
        }
      ]
    }
  },
  "size": 1000,
  "_source": [
    "entry_name"
  ]
}
```


### 增删改  

添加索引  
PUT /索引名/类型名（可以不写）/id  

```python 
PUT /test1/type1/1  
{
    "name": "mayanan", 
    "age": 30, 
}
```

删除索引
`DELETE kejisousou-test`  


#### 重建索引  

https://www.cnblogs.com/juncaoit/p/12815582.html  

新建一个索引，索引规则通过 GET 原索引名得到的结果获得。  

同步数据，不用文章里的异步的参数。  

删除旧索引。  


#### 新建模板  

比如照着 kejisousou-test 新建一个 kejisousou-testv2  

先 GET 原来的模板  
`GET /_template/kejisousou-test`  

然后从结果里去掉最外面一层，否则会报错 [Validation Failed: 1: template is missing](https://blog.csdn.net/congcong0808/article/details/52127611)  

然后改三个地方，一个是 PUT 命令后面那个模板名，一个是刚开始的 template 的值，`"template": "kejisousou-testv2-*"`，一个是最后的 aliases 的名字，`"kejisousou-testv2": {}`  

最后 `PUT /_template/kejisousou-testv2`  


## 工作 ES 相关  

ES 遇到问题自己用 kibana 写代码试   

提倡分多个索引，而不是一个索引里放很多东西  

es_bulk_module.py ES 增删改  

`GET test-zky/_count`  

query 是查询条件  

data_normalize.py  

zky-all 是备份  

5 种筛选数据的规则，满足任意一条就可以通过    
作者、域名、media 板块、child_map 域名后边带东西 比如 `finance.sina.com.cn/tech`，看 url 是否在目标的 url 里，在就返回 True，不在就返回 False，用 in 判断、site_name 和作者名都要符合的，用 and 关系    


一个 data 就是一条 kafka 数据  

helps 是 ES 的库，helpers.bulk 是批量操作，比如批量插入，如果数据重复就报错，一般忽略重复，不做重复判断    


flush_else() 把数据上传到 ES 以后删除内存里的数据    



## ElasticSearch 课程  

ElasticSearch 就是做文本搜索用的，可以就把 ElasticSearch 当做一个搜索和存储功能的数据库。用传统数据库做搜索会非常慢。  

RESTful 操作，上手非常简单，从接触到熟练，两天就行了。    

ES 就是重复的 CRUD，做和 ES 相关的工作非常轻松。    


#### ElasticSearch 概述  

ElasticSearch 是一个开源的高扩展的全文分布式搜索引擎，它可以近乎实时的存储和查询数据，查询效率非常高，本身扩展性很好，可以扩展到上百台服务器，处理 PB 级别的数据。  

Lucene 是一个用于文本搜索的函数库，目的是为各种中小型应用软件加入全文检索功能。  

ElasticSearch 是基于 Lucene 做了一些封装和增强  

设计的目的是通过简单的 RESTful API 封装 Lucene 的复杂性，从而让全文搜索变得简单。  

ElasticSearch 是排名第一的全文搜索类应用。使用的网站：维基百科、新闻网站、github、Stack Overflow、电商等等  

用于全文搜索、结构化搜索、分析以及将这三者混合使用  

ElasticSearch 适用于经常更新的数据，而且适合数据量非常大的使用场景。  

ElasticSearch 用的是自身的分布式协调管理功能  

ElasticSearch 仅支持 json 格式，只支持这一种就够了  

解压即用，默认 9200 端口    

bin 启动文件、config 配置文件、lib 相关包、modules 功能模块、plugins 插件、log 日志  


#### ES 核心概念  

ElasticSearch 是面向文档的，ElasticSearch 中一切都是 json  

索引 indices 就是数据库 database，type 就是表 table（慢慢会被弃用），document 是行 row，fields 是字段 column  

ElasticSearch 在后台把每个索引划分成多个分片，每份分片都可以在集群中的不同服务器间迁移  

ElasticSearch 是面向文档的，意味着索引和搜索的最小单位就是文档，**可以把文档就当做是一条记录**  

ElasticSearch 索引是一个非常大的文档集合  

一个集群至少有一个节点，一个节点就是一个 ElasticSearch 进程，节点下面有分片  

Lucene  采用倒排索引，倒排就是根据关键词找文档  

ElasticSearch 用的就是 Lucene 的倒排索引，做了一个聚合  


#### IK 分词器  

搜索里面做的最重要的事情就是分词  

ik 分词器就是分词用的  

ik_max_word 穷尽词库的可能  

可以自己配置分词  


#### 关于索引的基本操作  

RESTful 风格就是用不同的命令实现不同的操作。  

创建索引用 PUT  

PUT /索引名/类型名（可以不写）/id  

```python 
PUT /test1/type1/1  
{
    "name": "mayanan", 
    "age": 30, 
}
```

上面这种是文档，也可以只是添加库，添加规则  

```python 
PUT /test2  
{
    "mappings": {
        "properties": {
            "name": {
                "type": "text"
            }, 
            "age": {
                "type": "long"
            }, 
            "birthday": {
                "type": "date"
            }
        }
    }
}
```

这个和数据库建表是一样的  

或者使用 PUT /索引名/\_doc/1 默认类型就是 doc    
```python 
PUT /test3/_doc/1  
{
    "name": "mayanan", 
    "age": 30, 
    "birthday": "1991", 
}

GET /test3  
```

如果没有指定类型，ES 会自动指定字段类型  

可以使用 PUT 修改数据，其实这种方法就是覆盖  

比如  
```python 
PUT /test3/_doc/1  
{
    "name": "mayanan123", 
    "age": 30, 
    "birthday": "1991", 
}

GET /test3  
```
PUT 完以后，版本号 version 会增加  

PUT 方法不太好，比较好的方法是使用 POST 方法，后面接 update 更新  

```python 
POST /test3/_doc/1/_update  
{
    "doc": {
        "name": "yananma"  
    }
}
```

GET 索引名 获取索引的信息    

GET /索引名/表名/文档名 写到哪一层，就得到哪一层的信息  

GET \_cat 查看 ES 信息  

GET \_cat/indices?v  

DELETE 删除索引  

```json
DELETE test1  
```

#### 关于文档的基本操作   

先创建数据  

```python 
PUT /vip/user/1
{
    "name": "mayanan", 
    "age": 30, 
    "desc": "very good", 
    "tags": ["运动", "读书"] 
}
```

```python 
PUT /vip/user/2
{
    "name": "yananma", 
    "age": 30, 
    "desc": "very good", 
    "tags": ["运动", "读书"] 
}

GET /vip/user/1
```

如果再次 PUT 的 url 是已经存在的，就会是 update 操作，返回的数据，version 加 1，返回的 result 状态为 update  

不要用 PUT 更新，因为 PUT 更新，如果字段比原来的少，原来多的字段就没有了。用 POST /\_update 更新，update 更新以后，只是更新指定的字段，没有指定的字段保持不变。  

```python 
POST /vip/user/2/update  
{
    "doc": {
        "name": "nanyama"
    }
}

GET /vip/user/2
```

#### 查询（重点）

查询操作，最常见的就是根据 id 查询  

`GET /vip/user/1`  

这就是简单的条件查询，就是在查询的后面跟参数。  

`GET /vip/_search?q=name:yananma`   

q 就是 query  

分词器不会在 keyword 上发挥作用，所以 keyword 是精确匹配  

\_score 值就是匹配度，如果查询结果有多条，匹配度越高的分值越高。  

如果按照分值匹配，就可以把分值高的排在前面  

查询的常见结构就是下面这种形式  

```python 
GET /vip/_search  
{
    "query": {
        "match": {
            "name": "yananma"
        }
    }
}
```

match 是模糊查询，就是 like % %  

hits 包含索引和文档信息。前面是信息，后面是文档。拿到文档就可以遍历文档。  

total 查询结果总数。

score 可以判断判断哪个结果更加符合（用的是 TF/IDF）  

\_source 可以选择要的字段，`"_source": ["title", "desc"]`，就是一种结果的过滤，就好比是 MySQL 里面的 `select name, desc from user` 是一样的    

sort 可以指定排序字段和升序降序，指定了排序以后，分值 \_score 就是 null 了  

from 是分页起始值，从第几个开始，下标默认从零开始；

size 返回多少条数据，就是一页的数量  

bool 布尔查询，就是多条件查询，所有的查询条件都放到 bool 里面，后面接 must、must_not、should 等等，后面就可以做多条件匹配。  

must 里的条件都要符合，比如 match name，match age，name 和 age 都符合的才会返回，就是 and 查询，等价于 `where name=name and age=age`  

should 就是 or 查询  

must_not 就是 not 查询（就是 exclude）  

filter 过滤查询，指定 field，然后通过 gt 和 lt 指定查询区间    

term 精确查询，term 查询是直接通过倒排索引指定的词条进行精确查找的。    

（term 是直接倒排索引精确查询的，查询范围小，查找的词少，所以速度非常快。（可能对中文不是很好，没有空格，可以会把一句话就当成一个词了，试一试）
match 会使用分词器，满足其中一个就会被查出来）  

也可以用 term 精确查询多个值，查询办法就是使用 should 里面套多个 term  

text 类型会被分词器解析，keyword 类型不会被分词器解析  

highlight 指定高亮字段，可以自己指定前缀和后缀标签  

```python 
```

must_not 例子  

```python 
GET /vip/_search  
{
    "query": {
        "bool": {
            "must_not": [
                {
                    "match": {
                        "age": 30
                    }
                }
            ]
        }
    }
}
```

filter 例子  
```python 
GET /vip/_search  
{
    "query": {
        "bool": {
            "must": [
                {
                    "match": {
                        "name": "ma"
                    }
                }
            ], 
            "filter": {
                "range": {
                    "age": {
                        "gt": 10
                    }
                }
            }
        }
    }
}
```

多个词查询，查询条件之间用空格隔开，查询之间是 or 关系，只要满足其中一个就可以被查出，可以看到 score 值    
```python 
GET /vip/_search  
{
    "query": {
        "match": {
            "tags": "第一个词 第二个词"
        }
    }
}
```

高亮  
```python 
GET /vip/_search
{
    "query":{
        "match": {
            "name": "图书"
        }
    }, 
    "highlight": {
        "pre_tags": "<span class='key' style='color:red'>", 
        "post_tags": "</span>"  
        "fields": {
            "name": {}
        }
    }
}
```


## kibana 文档

`GET /_cat/indices?v`，查看所有 indices  

查看所有模板 `GET _template/*`   

`GET test_zky/` 不传参数返回的就是配置  

控制台插件提供一个用户界面来和 Elasticsearch 的 REST API 交互。控制台有两个主要部分： editor ，用来编写提交给 Elasticsearch 的请求； response 面板，用来展示请求结果的响应。  


可以一次选择多个请求，控制台会依次提交请求到 Elasticsearch ，并将 Elasticsearch 返回的结果显示在右边窗口。这在调试问题或在多个场景中尝试查询组合时会非常方便。  

小扳手里可以选择自动缩进格式化。  

Ctrl + Enter 提交请求  

Ctrl + Up/Down 跳转到上一个/下一个请求的开始或结束  

点击窗口右上角的 History 即可查看历史记录。会打开历史记录面板，可以在其中查看历史请求。也可以在这里选择一个请求，它将被添加到编辑器中当前光标所在的位置。  

在 Settings 里可以设置字符大小  




