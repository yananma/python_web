

### 一般情况下，手写查询，不再复制  

查询 text 类型，使用 query_string 或 match_phrase，完全匹配关键字类型，用 term.  

查看索引字段  
`GET kejisousou`  

在所有索引中查询，就是不指定索引名查询  
`GET _search`  

查看数量  
`GET /kejisousou-testv5/_count`  

多用 filter，会大幅提高查询速度，因为不用评分   
```python 
query_dict = {
    "query": {
        "bool": {
            "filter": {
                "bool": {
                    "must": [
                        # {
                        #     "match_phrase": {
                        #         "talent_text": query_word
                        #     }
                        # },
                        {
                            "query_string": {
                                "default_field": "talent_text",
                                "query": ' AND '.join(f'"{word}"' for word in query_word.split())
                            }
                        },
                        {
                            "term": {
                                "author_type": {
                                    "value": 1
                                }
                            }
                        }
                    ]
                }
            }
        }
    }
}
```

query_string 查询  

最常用的是这个  
```python 
GET test-zky/_search
{
  "query": {
    "bool": {
      "must": [
        {
          "query_string": {
            "default_field": "url",
            "query": "\"http://kuaibao.qq.com/s/93560f119f336852\" 
            or \"https://finance.sina.com.cn/tech/2021-07-16/doc-ikqcfnca7213437.shtml\""
          }
        }
      ]
    }
  }
}
```

query_string 查多个 id，最开始和结束都有斜杠  
```python 
GET kejisousou-en-formal/_search
{
  "query": {
    "query_string": {
      "default_field": "entry_id",
      "query": "\"647520\" OR \"647521\" OR \"647522\" OR \"647542\""
    }
  }
}
```

拼接用 print，不过前后要手动加上引号  
```python 
print(('\\" OR \\"').join(li)) 
```

```python 
GET kejisousou-en-testv3/_search
{
  "query": {
    "bool": {
      "should": [
        {
          "query_string": {
            "fields": ["title", "text"],
            "query": "math"
          }
        }
      ]
    }
  }
}
```

```python 
GET /kejisousou-en-testv3/_search
{
  "query": {
    "query_string": {
      "fields": ["title", "text"],
      "query": "math"
    }
  }
}
```

多条件查询  

```python 
GET kejisousou-en-yuce-formal-v2/_search
{
  "query": {
    "bool": {
      "should": [
        {
          "terms": {
            "url.raw": [
              "https://news.mit.edu/2021/automated-machine-learning-veeramachaneni-1006", 
              "https://oraclesinvestmentgroup.medium.com/oig-ama-with-darenft-50be70784ef4", 
              "https://www.nsf.gov/discoveries/disc_summ.jsp?cntn_id=303606&org=NSF&from=news",
              "https://news.mit.edu/2021/does-artificial-intelligence-play-well-others-1004"
            ]
          }
        }
      ]
    }
  }
}
```


在多个字段中查询  

```python 
GET test-zky/_search
{
  "query": {
    "bool": {
      "should": [
        {
          "query_string": {
            "fields": ["title", "text"],
            "query": "\"拉曼研究所\""
          }
        }
      ]
    }
  },
  "_source": ["title", "url", "post_time", "text"]
}
```

title.keyword  
```python 
GET test-zky/_search 
{
  "query": {
    "term": {
      "title.keyword": {
        "value": "落户合肥"
      }
    }
  }, 
  "_source": ["title", "text"]
}
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

按字段是否存在查询  
```python 
GET kejisousou-yuce-formal-v4/_search 
{
  "query": {
    "bool": {
      "must_not": [
        {
          "exists": {
            "field": "include_time"
          }
        }
      ]
    }
  }
}
```


#### 聚合  

按月份聚合  
```python 
GET /kejisousou-en-test/_search
{
  "size": 0,
  "aggs": {
    "time_aggs": {
      "date_histogram": {
        "field": "post_time",
        "time_zone": "+08:00",
        "interval": "month",
        "format": "yyyy-MM"
      }
    }
  }
}
```

按分类聚合  
```python 
GET /kejisousou-en-test/_search
{
  "size": 0,
  "aggs": {
    "category_aggs": {
      "terms": {
        "field": "category.keyword"
      }
    }
  }
}
```

先按月份聚合，然后每个月按分类聚合  
```python 
GET /kejisousou-en-test/_search
{
  "size": 0,
  "aggs": {
    "time_aggs": {
      "date_histogram": {
        "field": "post_time",
        "time_zone": "+08:00",
        "interval": "month",
        "format": "yyyy-MM"
      },
      "aggs": {
        "category_aggs": {
          "terms": {
            "field": "category.keyword"
          }
        }
      }
    }
  }
}
```

限定日期范围聚合查询  

```python 
GET /kejisousou-en-test/_search
{
  "query": {
    "bool": {
      "must": [
        {
          "range": {
            "post_time": {
              "gte": "2020-01-01 00:00:00",
              "lte": "2021-09-09 00:00:00"
            }
          }
        }
      ]
    }
  },
  "size": 0,
  "aggs": {
    "time_aggs": {
      "date_histogram": {
        "field": "post_time",
        "interval": "month"
      }
    }
  }
}
```

聚合后根据聚合结果的数量排序  

```python 
GET page/_search
{
  "query": {
    "bool": {
      "must": [
        {
          "range": {
            "include_time": {
              "gte": "2021-10-01 00:00:00",
              "lte": "2021-10-25 00:00:00"
            }
          }
        }
      ]
    }
  },
  "aggs": {
    "NAME": {
      "date_histogram": {
        "field": "include_time",
        "interval": "day",
        "order": {
          "_count": "asc"
        }
      }
    }
  },
  "size": 0
}
```

按 entry_id 聚合，这样可以看到都有哪些 entry_id。    

```python 
GET /kejisousou-en-testv1/_search
{
  "size": 0,
  "aggs": {
    "category_aggs": {
      "terms": {
        "field": "entry_id",
        "size": 1000    # 这个 size 是 agg 的类别条数，不是具体内容的条数
      }
    }
  },
  "size": 0
}
```

按照 id 筛选，再按照时间排序，就可以看到这个 id 下的按顺序排列的结果  

```python 
GET kejisousou-en-test/_search
{
  "query": {
    "match_phrase": {
      "entry_id": "647232"
    }
  }, 
  "size": 161,
  "_source": "post_time",
  "sort": [
    {
      "post_time": {
        "order": "desc"
      }
    }
  ]
}
```


### script  

```python 
GET kejisousou-yuce-formal-v3/_search
{
  "query": {
    "bool": {
      "should": [
        {
          "script": {
            "script": "doc[\"point_text.raw\"].value.length()==0"
          }
        }
      ]
    }
  }
}
```

### 正则  

不用 raw，会分词，分词以后就不是正则了，就成了单个字和符号的匹配了  

```python 
GET kejisousou-zhili-formal-v3/_search
{
  "query": {
    "regexp": {
      "point_text.raw": ".*只是因为.*"
    }
  }
}
```



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
```python 
PUT mayanan
{
  "mappings": {
    "zky_doc": {
      "properties": {
        "author_id": {
          "type": "integer",
          "copy_to": ["author_id_str"]
        },
        "author_id_str": {
          "type": "keyword",
          "store": true
        }
      }
    }
  }
}
```

直接添加数据  
PUT /索引名/类型名（可以不写）/id  

```python 
PUT /test1/type1/1  
{
    "name": "mayanan", 
    "age": 30, 
}
```

添加字段  
```python 
PUT 索引名/_mapping/类型名  
{
  "properties": {
    "include_time": {
      "type": "date",
      "format": "yyyy-MM-dd HH:mm:ss"
    }
  }
}
```



删除索引
`DELETE kejisousou-test`  


删除查询的结果  
```python 
POST suoyinming/_delete_by_query
{
  "query": { 
    "match": {
      "num": "39"
    }
  }
}
```

update 一条数据  

```python 
GET kejisousou-yuce-formal-v3/_update_by_query
{
  "script": {
    "inline": "ctx._source['yuce_text']='充电桩的盈利'"
  },
  "query": {
    "bool": {
      "should": [
        {
          "query_string": {
            "default_field": "url",
            "query": "\"https://www.toutiao.com/i7000203772555166244/\""
          }
        }
      ]
    }
  }
}
```

### 新建索引  

先找一个参考索引 `GET kejisousou-zhili-formal-v3/`  
PUT 新索引名，比如 `PUT zjgdk-v1`  
复制查询结果里的 mappings，修改 \_doc   
添加、删除、修改字段    
执行 PUT 命令   


## 工作 ES 相关  

keyword 类型，直接简历反向索引  
text 类型，先分词，再建立反向索引  

反向索引是根据内容的关键词建立索引  

搜索引擎的原理就是建立反向索引   




ES 遇到问题自己用 kibana 写代码试   



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

```python
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

#### 新建索引  

[新建 index 的例子](https://github.com/yananma/python_web/blob/main/%E4%B8%8D%E5%B8%B8%E7%94%A8/%E5%85%B6%E4%BB%96/elasticsearch_index.md)   


#### 新建模板  

比如照着 kejisousou-test 新建一个 kejisousou-testv2  

先 GET 原来的模板  
`GET /_template/kejisousou-test`  

然后从结果里去掉最外面一层，这里说的最外面一层包括最外层的两个花括号和 "kejisousou-en-test":。否则会报错 [Validation Failed: 1: template is missing](https://blog.csdn.net/congcong0808/article/details/52127611)  

然后改三个地方：
1. PUT 命令后面那个模板名，`PUT /_template/kejisousou-testv2`  
2. 刚开始的 template 的值，改成 `"template": "kejisousou-testv2-*"`  
3. 最后的 aliases 的名字，改成 `"kejisousou-testv2": {}`  

[新建 \_template 的例子](https://github.com/yananma/python_web/blob/main/%E4%B8%8D%E5%B8%B8%E7%94%A8/%E5%85%B6%E4%BB%96/elasticsearch_template.md)   



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




