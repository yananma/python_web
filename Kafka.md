
ipython 生产数据    

```python
from mx_config import mxconfig
bootstrap_servers = mxconfig('/connection/kafka$kafka.servers')
from confluent_kafka import Producer

TOPIC = "interaction"
producer = Producer(**{"bootstrap.servers": bootstrap_servers})

d = {"url": "http://www.douyin.com/video/7329708531983174927", "read_num": -1, "like_num": 2, "collect_num": 0, "comment_num": 0, "repost_num": 0, "watch_num": -1, "extra": "{}", "include_time": "2024-01-31 16:05:15"}

import json
producer.produce(TOPIC, json.dumps(d))
``` 



ipython 命令行     

```python
import json
import time
import sys
import logging
import traceback

import more_itertools
import peewee
import pykafka.exceptions

from pymysql import MySQLError
from pykafka import KafkaClient
from pykafka.common import OffsetType
from mx_config import mxconfig
from hill.models import bsppr

bootstrap_servers = mxconfig('/connection/kafka$kafka.servers')

client = KafkaClient(hosts=bootstrap_servers, broker_version='1.1.1')


def make_consumer(client, topic, group):
    # 创建连接
    tpc = client.topics[topic]
    return tpc.get_balanced_consumer(
        consumer_group=group,
        managed=True,  # use kafka manager
        fetch_message_max_bytes=10240 * 1024,  # 获取到的数据最大 10M
        num_consumer_fetchers=1,  # 1个数据获取线程
        auto_commit_enable=False,  # 自动设置成已经消费
        queued_max_messages=2000,  # buffer 中的数据量
        auto_offset_reset=OffsetType.EARLIEST,  # 当数据出界时的行为
        consumer_timeout_ms=1000,  # 没有数据，多长时间返回一次 None
        auto_start=True,  # 初始化后不调用 start 就启动
        reset_offset_on_start=False,  # 默认从上一个没有 commit 的地方启动
        use_rdkafka=False,  # 不使用 C 扩展的 librdkafka，默认在可用时使用
    )


topic = 'interaction'
group = 'interaction'

client = KafkaClient(hosts=bootstrap_servers, broker_version='1.1.1')
consumer = make_consumer(client, topic, group)


msg = consumer.consume()

msg.value
'{"url": "http://www.douyin.com/video/7329708531983174927", "read_num": -1, "like_num": 2, "collect_num": 0, "comment_num": 0, "repost_num": 0, "watch_num": -1, "extra": "{}", "include_time": "2024-01-31 16:05:15"}'

```




消费脚本        

```python
# -*- coding: utf-8 -*-
import json
import time
import sys
import logging
import traceback

import more_itertools
import peewee
import pykafka.exceptions

from pymysql import MySQLError
from pykafka import KafkaClient
from pykafka.common import OffsetType
from mx_config import mxconfig
from hill.models import bsppr

logging.basicConfig(
    format='[%(asctime)s] - %(levelname)s - [%(name)s] %(message)s',
    level=logging.INFO,
)
logger = logging.getLogger(__name__)

bootstrap_servers = mxconfig('/connection/kafka$kafka.servers')

client = KafkaClient(hosts=bootstrap_servers, broker_version='1.1.1')


def make_consumer(client, topic, group):
    # 创建连接
    tpc = client.topics[topic]
    return tpc.get_balanced_consumer(
        consumer_group=group,
        managed=True,  # use kafka manager
        fetch_message_max_bytes=10240 * 1024,  # 获取到的数据最大 10M
        num_consumer_fetchers=1,  # 1个数据获取线程
        auto_commit_enable=False,  # 自动设置成已经消费
        queued_max_messages=2000,  # buffer 中的数据量
        auto_offset_reset=OffsetType.EARLIEST,  # 当数据出界时的行为
        consumer_timeout_ms=1000,  # 没有数据，多长时间返回一次 None
        auto_start=True,  # 初始化后不调用 start 就启动
        reset_offset_on_start=False,  # 默认从上一个没有 commit 的地方启动
        use_rdkafka=False,  # 不使用 C 扩展的 librdkafka，默认在可用时使用
    )


class UpdateInteract(object):
    def __init__(self):
        self._cache = []
        self._cache_size = 2000
        self._model = None

    def upload(self, data, commit_offsets):
        if isinstance(data, bytes):
            data = data.decode('utf-8')
        data = json.loads(data)
        if isinstance(data, dict):
            data = [data]
        for d in data:
            self._cache.append(d)
            if len(self._cache) >= self._cache_size:
                self._flush()
                commit_offsets()

    def _flush(self):
        for d in self._cache:
            logger.info(d)
        self._cache = []


def start_consumer():
    topic = 'interaction'
    group = 'interaction'
    logger.info("Consume %s-%s" % (topic, group))

    client = KafkaClient(hosts=bootstrap_servers, broker_version='1.1.1')
    consumer = make_consumer(client, topic, group)
    update_interact = UpdateInteract()

    count = 0
    no_new_data_count = 0
    while True:
        try:
            message = consumer.consume(block=not update_interact._cache)
            if message is not None:
                no_new_data_count = 0
                try:
                    update_interact.upload(message.value, consumer.commit_offsets)
                    if message.offset % 1000 == 0:
                        logger.info("Topic: %s, Consumer Partitions: %s. Current partition is %d, offset is %d"
                                    % (topic, str(consumer.partitions.keys()), message.partition_id,
                                       message.offset))
                    count += 1
                    if count >= 50000:
                        logger.info("Count: %s, not Exit for memory release ...", count)
                        if update_interact._cache:  # 太多了，先刷新一下
                            update_interact._flush()
                        consumer.commit_offsets()
                        count = 0
                        # exit(0)
                except (pykafka.exceptions.UnknownMemberId, pykafka.exceptions.SocketDisconnectedError):
                    logger.error("Exception: \n%s" % traceback.format_exc())
                    logger.info("Sleep to protect from supervisor ...")
                    exit(1)
                except (MySQLError, peewee.PeeweeException):
                    logger.exception('error with database, will exit.')
                    sys.exit(2)
                except SystemExit as e:
                    sys.exit(3)
                except:
                    logger.error("Exception: \n%s \nwith data\n %s" % (traceback.format_exc(), message.value))
            else:  # no new data
                if update_interact._cache:  # 没有新数据，先把缓存的数据处理掉
                    update_interact._flush()
                    consumer.commit_offsets()
                    count = 0
                logger.info("No new data, waiting 5s ...")
                time.sleep(5)
                if no_new_data_count > 100:
                    logger.info(u"more than 100 times no data, restart process.")
                    sys.exit(1)
                no_new_data_count += 1
        except KeyboardInterrupt:
            logger.info("Receive C-c, shut down!")
            break
        except SystemExit as e:
            sys.exit(3)
        except Exception as e:
            logger.info("Wait 10s before raising an exception ...")
            time.sleep(10)
            raise e


if __name__ == "__main__":
    start_consumer()
```
