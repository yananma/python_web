
搜工具集和 cyberin，看用法       


查看键中的值：`GET "键名"`  




## 列表   

#### 查看列表长度   

```python  
from hill.models.connections import lazy

lazy.rc.llen(u"crawlcomments:urls-info")
```


#### 清空列表  

```python  
lazy.rc.ltrim(u"crawl:comment:crawlcomments_weibo_com:urls", 0, 0)   
```

#### 添加元素    

```python
rpush     
```


#### 查数量  

```python  
lazy.rc.zcard("crawlcomments:urls-info-url-dedup")   
```


## 集合   

#### 添加元素   

```python
cache.sadd(u"urls-info-dedupe", trans_to_md5(d[u"url"]))
``` 


#### 判断元素在不在集合    

```python
cache.sismember(u"urls-info-dedupe", trans_to_md5(d[u"url"]))    
```


#### 查询数量   

```python
cache.scard("dazhong_author_set_mayanan:urls-dedup")
```


#### 清空集合   

```python
cache.delete("dazhong_author_set_mayanan:urls-dedup")  # 有时候键太大，删除以后不会立即生效，就重新换一个键      
```



## 有序集合  

#### 添加元素   

```python  
cache.zadd(redis_dedup_key, {md5_url: time.time()})
# 低版本 redis（比如 Cyberin）（应该是 3.0 以下）不支持上面这种写法，低版本要用下面这种写法
cache.zadd(redis_dedup_key, md5_url, time.time())
```

#### 只保留一个小时以内的元素   

```python  
# zremrangebyscore 移除给定的分数区间的所有成员
cache.zremrangebyscore(redis_dedup_key, 0, time.time() - 60 * 60)
```

#### 查询数量  

```python
from rediscluster import RedisCluster, StrictRedisCluster
from mx_config import mxconfig

startup_nodes = mxconfig('[redis_cluster_nodes]$/connection/redis$redis.servers')
cache = StrictRedisCluster(startup_nodes=startup_nodes, decode_responses=True)
redis_dedup_key = u"crawlinteraction:urls-info"

cache.zscan(redis_dedup_key)
```




#### 删除，量大的时候不要自己删，找树兵删     

```python  
cache.delete(key)  
```


#### redis 缓存   

```python  
def redis_cache(func):
    @functools.wraps(func)
    def wrapper(*args, **kwargs):
        request = args[0]
        oid = request.GET.get(u"objectid")
        start_date = request.GET.get(u'start_date')
        end_date = request.GET.get(u'end_date')
        key = u"cyberin_tongyong_dashboard::" + oid + u'_' + start_date + u"_" + end_date + u"_" + func.func_name
        cache_res = cache.get(key)
        if cache_res:
            logger.info(u"get {} result from redis cache.".format(func.func_name))
            cache_res = json.loads(cache_res)
            return JsonResponse(cache_res)
        else:
            res = func(*args, **kwargs)
            cache.set(key, res.content, 5*60)
            logger.info(u"get {} result from view function.".format(func.func_name))
            return res
    return wrapper
```


#### redis 集合去重，一般不用，千万数量级以上才用   

```python  
# cyberin  

from django_redis import get_redis_connection  

cache = get_redis_connection("default")


if cache.sismember(u"urls-info-dedupe", trans_to_md5(d[u"url"])):
    continue
else:
    cache.sadd(u"urls-info-dedupe", trans_to_md5(d[u"url"]))
```


```python
def dedup(self, datas):
    start_time = time.time()
    redis_dedup_key = u"dazhong_author_set_mayanan:urls-dedup"
    deduped_data = []
    local_urls = set()
    for data in datas:
        if data['url'] in local_urls:
            continue
        local_urls.add(data['url'])
        if cache.sismember(redis_dedup_key, data['url']):
            continue
        deduped_data.append(data)
        if len(local_urls) >= 10000:
            cache.sadd(redis_dedup_key, *local_urls)
            local_urls = set()
    cache.sadd(redis_dedup_key, *local_urls)
    logger.info(u"dedup cost {}s".format(time.time() - start_time))
    return deduped_data
```



#### redis 用有序集合去重，有序集合是一种比较重的数据结构，一般去重用 set 即可，保留一个小时内的数据，超过一个小时的数据过期       

```python  
redis_dedup_key = u"crawlcomments:urls-info-url-dedup"
cache.zremrangebyscore(redis_dedup_key, 0, time.time() - 60 * 60)
rpush_data = []
for key, data in sorted(url_data_map.items(), key=lambda x: x[1][u"sort_id"]):
    # url 去重
    md5_url = trans_to_md5(data[u"url"])
    time_stamp = cache.zscore(redis_dedup_key, md5_url)
    if time_stamp:
        continue
    else:
        cache.zadd(redis_dedup_key, {md5_url: time.time()})
        # 低版本 redis（比如 Cyberin）（应该是 3.0 以下）不支持上面这种写法，低版本要用下面这种写法
        cache.zadd(redis_dedup_key, md5_url, time.time())
```

#### 有序集合的一种比较好的写法   

```python
def dedup_data(self):
    if self.options["cancel_dedup"]:
        return self.get_url_data_map()
    redis_dedup_key = u"crawlcomments:urls-info-url-dedup"
    cache.zremrangebyscore(redis_dedup_key, 0, time.time() - 60 * 60)  # 近一个小时的 url 做去重
    deduped_url_data_map = {}
    for key, data in self.get_url_data_map().items():
        try:
            md5_url = trans_to_md5(data[u"url"])
        except UnicodeEncodeError:
            logger.exception(u"UnicodeEncodeError {}".format(data[u"url"]))
            continue
        time_stamp = cache.zscore(redis_dedup_key, md5_url)
        if time_stamp:
            continue
        else:
            cache.zadd(redis_dedup_key, md5_url, time.time())
        deduped_url_data_map[key] = data
    return deduped_url_data_map
```


#### redis 批量 push（速度提高几十倍）    

```python  
    def handle(self, *args, **options):
        url_data_map = self.get_url_data_map(options)
        rpush_data = []
        for key, data in sorted(url_data_map.items(), key=lambda x: x[1][u"temp_id"]):
            rpush_dict = {
                u"url": data[u"url"],
                u"title": data[u"title"],
                u"fids": u",".join(data[u"facetid"])
            }
            rpush_data.append(json.dumps(rpush_dict))
            if len(rpush_data) >= 2000:
                cache.rpush(u"crawlcomments:urls-info", *rpush_data)
                rpush_data.clear()  
            count = data[u"temp_id"]
            if count % 1000 == 0:
                logger.info(u"数量 {}".format(count))
        cache.rpush(u"crawlcomments:urls-info", *rpush_data)
        logger.info(u"done.")
```



### 安装 redis   

安装 redis 注意事项：     
（高版本 redis 已经集成了 cluster 了，试试只装高版本）     
1. 先装 redis，再装 hiredis，再装 rediscluster，再装 redis-py-cluster，顺序不能颠倒。  
2. 注意版本。找一个能用的环境，看那个环境里的包的对应的版本。    


### Redis 简介  

#### NoSQL 概述  

单机时代  
访问量小、静态网页   

单机数据库的瓶颈  
数据量太大，数据库放不下  
数据库的索引太大，一个机器内存也放不下  
访问量(读写混合)，一个服务器承受不了  

缓存时代，Memcached + MySQL + 垂直拆分（读写分离）   
80% 的时间都是在读，使用哦缓存，可以减轻压力  

分库分表 + 水平拆分 + MySQL 集群  

现在数据量很大，数据交换变化很快。  
比如有 1 亿条数据，加一列数据都非常非常难   
MySQL 用来存大的图片、视频等文件  

用户的个人信息、社交网络、地理位置、用户上传的数据、用户日志等爆发式增长，NoSQL 可以很好地解决这些问题   

NoSQL = Not only SQL（不仅仅是 SQL）  
泛指非关系型数据库  

NoSQL 特点  
解耦  
方便扩展（数据之间没有关系，很好扩展）  
大数据量高性能（Redis 1 秒钟，写 8 万次，读 11 万次）  
NoSQL 是细粒级的缓存，性能会比较高  
数据类型是多样型的（不需要实现设计数据库，随取随用）  

NoSQL 四大分类  
KV 键值对  
文档型数据库  
列存储数据库  
图关系数据库  


### Redis 入门  

Redis（Remote dictionary server）远程字典服务，像是操作字典一样操作  
可以定时同步到磁盘  


内存中是断电即失的，所以要持久化（rdb、aof）  
效率高，可以用于高速缓存  
登录 session 会话存储：存储在 redis 中，与 memcached 相比，数据不会丢失。  
排行版/计数器：比如一些秀场类的项目，经常会有一些前多少名的主播排名。还有一些文章阅读量的技术，或者新浪微博的点赞数等。经常变化，而且访问量很大  
作为消息队列：比如 celery 就是使用 redis 作为中间人。  
当前在线人数：还是之前的秀场例子，会显示当前系统有多少在线人数。  
一些常用的数据缓存：比如我们的 BBS 论坛，板块不会经常变化的，但是每次访问首页都要从 mysql 中获取，可以在 redis 中缓存起来，不用每次请求数据库。  
把前 200 篇文章缓存或者评论缓存：一般用户浏览网站，只会浏览前面一部分文章或者评论，那么可以把前面 200 篇文章和对应的评论缓存起来。用户访问超过的，就访问数据库，并且以后文章超过 200 篇，则把之前的文章删除。  
好友关系：微博的好友关系使用 redis 实现。  
发布和订阅功能：可以用来做聊天软件。  
地图信息分析  

Redis 特性  
多样的数据类型   
持久化  
集群  
事务  

默认端口 6379  
```linux
apt-get install redis-server  
service redis-server start  
sudo service redis-server stop  
``` 

对 redis 的操作可以用两种方式，第一种方式采用 redis-cli，第二种方式采用编程语言，比如 Python、PHP 和 JAVA 等。  

使用 redis-cli 对 redis 进行字符串操作：  

启动redis：
`sudo service redis-server start`  

连接 redis-server：  
`ps -aux | grep redis`    
`redis-cli -h [ip] -p [端口]`   
b7 dingyong      
`redis-cli -c -h 192.168.241.7 -p 16379`       


添加：  
`set key value`  
`set name mayanan`   
`get name`   
如果有空格，要加引号 `set name "hello world"`  

将字符串值 value 关联到 key。如果 key 已经持有其他值，set 命令就覆写旧值，无视其类型。并且默认的过期时间是永久，即永远不会过期。  

删除：  
`del key`  
`del username`    

设置过期时间：  
expire key timeout(单位为秒)  

也可以在设置值的时候，一同指定过期时间（EX 应该就是 Expire ）：  
`set key value EX timeout`  
  或：  
`setex key timeout value`  

查看过期时间（till time line）：  
`ttl key`  
如：  
`ttl username`  

查看当前redis中的所有key：  
`keys *`  

#### 列表操作：  

l 一般代表 list，特殊情况代表 left  

在列表左边添加元素：  
  `lpush key value`  
将值value插入到列表key的表头。如果key不存在，一个空列表会被创建并执行lpush操作。当key存在但不是列表类型时，将返回一个错误。  

在列表右边添加元素：  
`rpush key value`  
将值value插入到列表key的表尾。如果key不存在，一个空列表会被创建并执行RPUSH操作。当key存在但不是列表类型时，返回一个错误。  

查看列表中的元素：  
`lrange key start stop`  
返回列表key中指定区间内的元素，区间以偏移量start和stop指定,如果要左边的第一个到最后的一个lrange key 0 -1。  

移除列表中的元素：  
移除并返回列表key的头元素：  
`lpop key`  
  
移除并返回列表的尾元素：  
`rpop key`  
移除并返回列表key的中间元素：  

remove  
`lrem key count value`  
将删除key这个列表中，count个值为value的元素。

指定返回第几个元素：
`lindex key index`
将返回key这个列表中，索引为index的这个元素。

获取列表中的元素个数：
`llen key`  
如：
`llen languages`  

删除指定的元素：
`lrem key count value`  
如：
`lrem languages 0 php`  

根据参数 count 的值，移除列表中与参数 value 相等的元素。count的值可以是以下几种：
`count > 0`：从表头开始向表尾搜索，移除与value相等的元素，数量为count。
`count < 0`：从表尾开始向表头搜索，移除与 value相等的元素，数量为count的绝对值。
`count = 0`：移除表中所有与value 相等的值。

#### set集合的操作：

s 代表 set  

添加元素：
`sadd set value1 value2....`  
如：
`sadd team xiaotuo datuo`  

查看元素：
`smembeers set`  
如：
`smembers team`  

移除元素：
`srem set member...`  
如：
`srem team xiaotuo datuo`  

查看集合中的元素个数：
`scard set`  
如：
`scard team1`  

获取多个集合的交集：
`sinter set1 set2`  
如：
`sinter team1 team2`  

获取多个集合的并集：
`sunion set1 set2`  
如：
`sunion team1 team2`  

获取多个集合的差集：
`sdiff set1 set2`  
如：
`sdiff team1 team2`  

#### hash 哈希操作：

添加一个新值：
`hset key field value`  
如：
`hset website baidu baidu.com`  
将哈希表key中的域field的值设为value。

如果key不存在，一个新的哈希表被创建并进行 HSET操作。如果域 field已经存在于哈希表中，旧值将被覆盖。

获取哈希中的field对应的值：
`hget key field`  
  如：
`hget website baidu`  

删除field中的某个field：
`hdel key field`  
如：
`hdel website baidu`  

获取某个哈希中所有的field和value：
`hgetall key`  
如：
`hgetall website`  

获取某个哈希中所有的field：
`hkeys key`  
如：
`hkeys website`  

获取某个哈希中所有的值：
`hvals key`  
如：
`hvals website`  

判断哈希中是否存在某个field：
`hexists key field`  
如：
`hexists website baidu`  

获取哈希中总共的键值对：
`hlen field`
如：
`hlen website`  

事务操作：Redis 事务可以一次执行多个命令，事务具有以下特征：  
隔离操作：事务中的所有命令都会序列化、按顺序地执行，不会被其他命令打扰。  
原子操作：事务中的命令要么全部被执行，要么全部都不执行。比如转账    

开启一个事务：
`multi`  
以后执行的所有命令，都在这个事务中执行的。

执行事务：
`exec`  
会将在multi和exec中的操作一并提交。

取消事务：
`discard`  
会将multi后的所有命令取消。

监视一个或者多个key：

`watch key...`  
监视一个(或多个)key，如果在事务执行之前这个(或这些) key被其他命令所改动，那么事务将被打断。

取消所有key的监视：
`unwatch`  

#### 发布/订阅操作：

订阅就是在一直监听  

给某个频道发布消息：
`publish channel message`  
订阅某个频道的消息：
`subscribe channel`

#### 同步机制  

持久化：redis提供了两种数据备份方式，一种是 RDB，另外一种是 AOF，以下将详细介绍这两种备份策略：

| | RDB | AOF | 
| --- | --- | --- | 
| 开启关闭 | 开启：默认开启。关闭：把配置文件中所有的save都注释，就是关闭了。 | 开启：在配置文件中appendonly yes即开启了aof，为no关闭。 | 
| 同步机制 | 可以指定某个时间内发生多少个命令进行同步。比如1分钟内发生了2次命令，就做一次同步。 | 每秒同步或者每次发生命令后同步 | 
| 存储内容 | 存储的是redis里面的具体的值 | 存储的是执行的更新数据的操作命令 | 
| 存储文件的路径 | 根据dir以及dbfilename来指定路径和具体的文件名 | 根据dir以及appendfilename来指定具体的路径和文件名 | 
| 优点 | （1）存储数据到文件中会进行压缩，文件体积比aof小。（2）因为存储的是redis具体的值，并且会经过压缩，因此在恢复的时候速度比AOF快。（3）非常适用于备份。 | （1）AOF的策略是每秒钟或者每次发生写操作的时候都会同步，因此即使服务器故障，最多只会丢失1秒的数据。 （2）AOF存储的是Redis命令，并且是直接追加到aof文件后面，因此每次备份的时候只要添加新的数据进去就可以了。（3）如果AOF文件比较大了，那么Redis会进行重写，只保留最小的命令集合。 | 
| 缺点 | （1）RDB在多少时间内发生了多少写操作的时候就会出发同步机制，因为采用压缩机制，RDB在同步的时候都重新保存整个Redis中的数据，因此你一般会设置在最少5分钟才保存一次数据。在这种情况下，一旦服务器故障，会造成5分钟的数据丢失。（2）在数据保存进RDB的时候，Redis会fork出一个子进程用来同步，在数据量比较大的时候，可能会非常耗时。 | （1）AOF文件因为没有压缩，因此体积比RDB大。 （2）AOF是在每秒或者每次写操作都进行备份，因此如果并发量比较大，效率可能有点慢。（3）AOF文件因为存储的是命令，因此在灾难恢复的时候Redis会重新运行AOF中的命令，速度不及RDB。 | 
| 更多 | http://redisdoc.com/topic/persistence.html#redis | |


安全：在配置文件中，设置requirepass password，那么客户端连接的时候，需要使用密码：
```linux
 > redis-cli -p 127.0.0.1 -p 6379
 redis> set username xxx
 (error) NOAUTH Authentication required.
 redis> auth password
 redis> set username xxx
 OK
```

### Python 操作 Redis  

在 文件中 import Redis，读源码   

