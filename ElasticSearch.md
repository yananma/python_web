
#### 课程简介  

ElasticSearch 就是搜索用的，可以就把 ElasticSearch 当做一个数据库，具有搜索和存储功能  

用传统数据库会非常慢  

做大数据开发一定会用到  

RESTful 操作 search  

ES 就是重复的 CRUD  

库就是索引  


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


#### REST 操作  

RESTful 风格就是用不同的命令实现不同的操作。  

创建索引用 PUT  


