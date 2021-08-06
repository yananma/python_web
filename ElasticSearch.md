
#### 课程简介  

ElasticSearch 就是搜索用的，可以就把 ElasticSearch 当做一个数据库，具有搜索和存储功能。用传统数据库会非常慢。  

做大数据开发一定会用到  

RESTful 操作  

ES 就是重复的 CRUD  


#### Lucene 简介  

Lucene 是一个用于文本搜索的函数库，目的是为各种中小型应用软件加入全文检索功能。  

ElasticSearch 是基于 Lucene 做了一些封装和增强，上手十分简单，做和 ES 相关的工作非常轻松  

从接触到熟练，两天就行了  


#### ElasticSearch 概述  

ElasticSearch 是一个开源的高扩展的全文分布式搜索引擎，它可以近乎实时的存储和查询数据，查询效率非常高，本身扩展性很好，可以扩展到上百台服务器，处理 PB 级别的数据。  

设计的目的是通过简单的 RESTful API 封装 Lucene 的复杂性，从而让全文搜索变得简单。  

ElasticSearch 现在是排名第一的全文搜索类应用。  

使用的网站：维基百科、新闻网站、github、Stack Overflow、电商等等  

用于全文搜索、结构化搜索、分析以及将这三者混合使用  

ElasticSearch 适用于经常更新的数据，而且适合数据量非常大的使用场景。  

ElasticSearch 用的是自身的分布式协调管理功能  

ElasticSearch 仅支持 json 格式，只支持这一种就够了  


#### ElasticSearch 安装  

解压即用  

bin 启动文件  

config 配置文件  

lib 相关包  

modules 功能模块  

plugins 插件  

log 日志  

默认 9200 端口  


#### ES 核心概念  

ElasticSearch 是面向文档的  

ElasticSearch 中一切都是 json  

索引 indices 就是数据库 database  

type 就是表 table（慢慢会被弃用）  

document 是行 row  

fields 是字段 column  

ElasticSearch 在后台把每个索引划分成多个分片，每份分片都可以在集群中的不同服务器间迁移  

ElasticSearch 是面向文档的，意味着索引和搜索的最小单位就是文档，**可以把文档就当做是一条记录**  

ElasticSearch 索引是一个非常大的文档集合  

一个集群至少有一个节点，一个节点就是一个 ElasticSearch 进程，节点下面有分片  

Lucene  采用倒排索引，倒排就是根据关键词找文档  

ElasticSearch 用的就是 Lucene 的倒排索引，做了一个聚合  


#### IK 分词器  

搜索里面做的最重要的事情就是分词  

ik 分词用的  

ik_max_word 穷尽词库的可能  

可以自己配置分词  


#### 关于索引的基本操作  

RESTful 风格就是用不同的命令实现不同的操作。  

创建索引用 PUT  

PUT /索引名/类型名（可以不写）/id  

```json 
PUT /test1/type1/1  
{
    "name": "mayanan", 
    "age": 30, 
}
```

上面这种是文档，也可以只是添加库，添加规则  

```json 
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
```json 
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
```json 
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

```json 
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

```json 
PUT /vip/user/1
{
    "name": "mayanan", 
    "age": 30, 
    "desc": "very good", 
    "tags": ["运动", "读书"] 
}
```

```json 
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

```json 
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

这里的 q 就是 query  

分词器不会在 keyword 上发挥作用，所以 keyword 是精确匹配  

\_score 值就是匹配度，如果查询结果有多条，匹配度越高的分值越高。  

如果按照分值匹配，就可以把分值高的排在前面  

查询的常见结构就是下面这种形式  

```json 
GET /vip/_search  
{
    "query": {
        "match": {
            "name": "yananma"
        }
    }
}
```

其中，match 是模糊查询，就是 like % %  

返回的结果中，hits 包含索引和文档信息。查询总数在 total 里面。后面就是查询出来的具体的文档，就可以遍历文档。  

我们可以通过最后返回的 score 判断哪个更加符合  

通过 \_source 可以选择要的字段，`"_source": ["title", "desc"]`，就是一种结果的过滤，就好比是 MySQL 里面的 `select name, desc from user` 是一样的    

可以指定排序，排序是 sort，指定排序字段，和升序降序，指定了排序以后，分值 \_score 就是 null 了  

分页，指定 from 起始值，从第几个开始，下标默认从零开始；指定 size，返回多少条数据，就是一页的数量  

布尔查询，就是多条件查询，指定 bool，后面接 must（或其他），后面就可以做多条件匹配，must 里的条件都要符合，比如 match name，match age，name 和 age 都符合的才会返回，就是 and 查询，等价于 `where name=name and age=age`  

用 should 实现 or 查询。  




