
```python

GET _cat/indices?v

GET page,wei,community2/_search
{
  "query": {
    "terms": {
      "url": [
"http://weibo.com/6185411484/OtgrHrkHv/",
"https://weibo.com/6185411484/OtgrHrkHv/",
"http://weibo.com/6185411484/OtgrHrkHv",
"https://weibo.com/6185411484/OtgrHrkHv"
      ]
    }
  },
  "size": 20
}



GET page,wei,community2/_search
{
  "query": {
    "terms": {
      "url": [
"http://news0.vsxv.net/show-htm-itemid-804947.html/",
"https://news0.vsxv.net/show-htm-itemid-804947.html/",
"http://news0.vsxv.net/show-htm-itemid-804947.html",
"https://news0.vsxv.net/show-htm-itemid-804947.html"
      ]
    }
  },
  "size": 20
}

GET page,wei,community2/_search
{
  "query": {
    "terms": {
      "url": [
"https://www.miguvideo.com/p/detail/910451960"
      ]
    }
  },
  "size": 20
}


GET page,wei,community2/_search
{
  "query": {
    "terms": {
      "entry_name": [
"统一企业"
      ]
    }
  },
  "size": 20
}



GET page,wei,community2/_search
{
  "query": {
    "terms": {
      "url": [
        "https://user.guancha.cn/wap/content?id=1196215"
      ]
    }
  },
  "size": 20
}



GET data_king-202402,community2-202402,weixin_weibo-202402/_search
{
  "size": 200,
  "_source": ["post_time", "include_time", "title", "url"],
  "sort": [{"post_time": "asc"}, {"include_time": "asc"},{"url": "asc"}]
}



GET page,wei,community2/_search
{
  "query": {
    "terms": {
      "title": [
        "受日本排污影响，SK-II中国市场销售额暴跌34%"
      ]
    }
  },
  "size": 20
}


GET page,wei,community2/_search
{
  "query": {
    "bool": {
      "must": [
        {
          "match_phrase": {
            "title": "受日本排污影响，SK-II中国市场销售额暴跌34%"
          }
        }
      ]
    }
  },
  "size": 200
}



GET page,wei,community2/_search
{
  "query": {
    "bool": {
      "must": [
        {
          "match_phrase": {
            "text": "能不能换一个好看一点的车标"
          }
        }
      ]
    }
  },
  "size": 100
}



GET page,wei,community2/_search
{
  "query": {
    "terms": {
      "author_name": [
        "狐椒文旅"
      ]
    }
  },
  "sort": [
    {
      "include_time": {
        "order": "desc"
      }
    }
  ],
  "_source": ["include_time", "author_name", "url", "title", "spider_source", "entry_id"], 
  "size": 200
}




GET page,wei,community2/_search
{
  "query": {
    "terms": {
      "author_id": [
        "631c14210000000023039183"
      ]
    }
  }
}



GET page,wei,community2/_search
{
  "query": {
    "terms": {
      "entry_id": [
        "679622", "701637", "706799", "701444", "694220", "690458"
      ]
    }
  },
  "size": 100
}


GET page,wei,community2/_search
{
    "sort": [
        {
            "post_time": "asc"
        }, 
        {
            "include_time": "asc"
        }
    ], 
    "query": {
        "bool": {
            "filter": {
                "bool": {
                    "should": [
                        {
                            "terms": {
                                "entry_id": [
                                    679622, 
                                    701637, 
                                    706799, 
                                    701444, 
                                    694220, 
                                    690458
                                ]
                            }
                        }
                    ], 
                    "must": [
                        {
                            "range": {
                                "post_time": {
                                    "gte": "2022-09-01 00:00:00", 
                                    "lte": "2024-03-21 23:59:59"
                                }
                            }
                        }
                    ]
                }
            }
        }
    }
}










# -------------------------------------------


GET zjgdk-v2-202407/_search
{
  "size": 5000,
  "sort": [
    {
      "include_time": {
        "order": "desc"
      }
    }
  ]
}



GET zjgdk-v2/_search 
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


GET _cat/indices?v&s=store.size:desc



GET page,wei,community2/_search
{
  "query": {
    "bool": {
      "must": [
        {
          "match_phrase": {
            "title": "巨亏13亿，路特斯裁员"
          }
        }
      ]
    }
  },
  "size": 100
}


GET page,wei,community2/_search
{
  "query": {
    "bool": {
      "must": [
        {
          "match_phrase": {
            "url": "64bc78be000000000103f65c"
          }
        }
      ]
    }
  },
  "size": 100
}


GET page,wei,community2/_search 
{
  "query": {
    "bool": {
      "must": [
        {
          "terms": {
            "url": [
              "http://mp.weixin.qq.com/s?__biz=MjM5ODQ0NTgzNQ==&mid=2651027214&idx=1&sn=96f9505fa1183d560eef8c0ae326caf5"
            ]
          }
        }
      ]
    }
  }
}


GET page,wei,community2/_search
{
  "query": {
    "bool": {
      "must": [
        {
          "range": {
            "include_time": {
              "gte": "2023-05-05 00:00:00",
              "lte": "2023-05-15 00:00:00"
            }
          }
        },
        {
          "term": {
            "spider_source": {
              "value": "b63_yqt_sub_api_consume"
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
        "field": "include_time",
        "interval": "day"
      }
    }
  }
}


GET page,wei,community2/_search
{
  "query": {
    "bool": {
      "must": [
        {
          "range": {
            "include_time": {
              "gte": "2023-05-05 00:00:00",
              "lte": "2023-05-15 00:00:00"
            }
          }
        },
        {
          "term": {
            "spider_source": {
              "value": "b63_yqt_sub_api_consume"
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
        "field": "include_time",
        "interval": "day"
      }
    }
  }
}



GET page,wei,community2/_search
{
  "query": {
    "bool": {
      "must": [
        {
          "range": {
            "include_time": {
              "gte": "2023-05-11 00:00:00",
              "lte": "2023-05-12 00:00:00"
            }
          }
        },
        {
          "match_phrase": {
            "text": "梦廊坊"
          }
        }
      ]
    }
  }
}


GET page/_count
{
  "query": {
    "bool": {
      "must": [
        {
          "range": {
            "include_time": {
              "gte": "2023-07-01 00:00:00",
              "lte": "2023-07-31 10:10:00"
            }
          }
        },
        {
          "multi_match": {
            "query": "衣服",
            "fields": ["title", "abstract"]
          }
        }
      ]
    }
  }
}


GET weixin_weibo-202305/_search 
{
  
}


GET page,wei,community2/_search
{
  "query": {
    "bool": {
      "must": [
        {
          "range": {
            "include_time": {
              "gte": "2023-06-06 00:00:00",
              "lte": "2023-06-07 00:00:00"
            }
          }
        },
        {
          "terms": {
            "author_id": [
              "xinyi-wenhuazhongxin", 
              "gh_d30780c5307e", 
              "zhiyouhongloumeng", 
              "6518825414", 
              "6512922896"
              ]
          }
        }
      ]
    }
  },
  "_source": ["author_name", "author_id"],
  "size": 200
}


GET page,wei,community2/_search
{
  "query": {
    "bool": {
      "must": [
        {
          "range": {
            "include_time": {
              "gte": "2023-12-12 00:00:00",
              "lte": "2023-12-13 00:00:00"
            }
          }
        },
        {
          "terms": {
            "site_name": ["微信"]
          }
        }
      ]
    }
  },
  "size": 10000
}



GET page,wei,community2/_search
{
  "query": {
    "bool": {
      "must": [
        {
          "range": {
            "include_time": {
              "gte": "2023-06-26 00:00:00",
              "lte": "2023-06-27 00:00:00"
            }
          }
        },
        {
          "terms": {
            "author_id": [
              "chinacosmeticsreview",
              "qingyanhw",
              "jumeili-cn",
              "huazhuangpinbao",
              "F-beauty0312",
              "qingyanwh",
              "wowjiemian",
              "thepapernews"
            ]
          }
        }
      ]
    }
  },
  "size": 200
}


GET data_king-202312,community2-202312,weixin_weibo-202312/_search
{
  "query": {
    "bool": {
      "must": [
        {
          "range": {
            "post_time": {
              "gte": "2023-12-01 01:00:00",
              "lte": "2023-12-01 02:00:59"
            }
          }
        },
        {
          "match_phrase": {
            "title": "亿联"
          }
        },
        {
          "match_phrase": {
            "text": "亿联"
          }
        }
      ]
    }
  },
  "size": 200
}


GET page,wei,community2/_search
{
  "query": {
    "terms": {
      "url": [
        "http://www.douyin.com/video/7229937968914468148"
      ]
    }
  },
  "size": 20
}


GET page,wei,community2/_search
{
  "query": {
    "terms": {
      "url": [
        "http://www.douyin.com/video/7229973663607491873"
      ]
    }
  },
  "size": 20
}


GET data_king-202304,weixin_weibo-202304,community2-202304/_search
{
  "query": {
    "terms": {
      "url": [
        "https://www.handannews.com.cn/news/content/2023-04/27/content_20108889.html"
      ]
    }
  }
}


GET kejisousou-yuce-formal-v4/_search
{
  "query": {
    "range": {
      "post_time": {
        "gte": "2021-11-15 00:00:00",
        "lte": "2021-12-03 00:00:00"
      }
    }
  }, 
  "size": 0, 
  "aggs": {
    "NAME": {
      "date_histogram": {
        "field": "post_time",
        "interval": "day"
      }
    }
  }
}

GET kejisousou-zhili-formal-v3/_search
{
  "query": {
    "range": {
      "post_time": {
        "gte": "2021-11-15 00:00:00",
        "lte": "2021-12-03 00:00:00"
      }
    }
  }, 
  "size": 0, 
  "aggs": {
    "NAME": {
      "date_histogram": {
        "field": "post_time",
        "interval": "day"
      }
    }
  }
}

GET kejisousou-en-yuce-formal-v3/_count

GET kejisousou-en-yuce-formal-v3/_search
{
  "query": {
    "range": {
      "post_time": {
        "gte": "2021-10-01 00:00:00",
        "lte": "2021-12-03 00:00:00"
      }
    }
  }, 
  "size": 0, 
  "aggs": {
    "NAME": {
      "date_histogram": {
        "field": "post_time",
        "interval": "day"
      }
    }
  }
}

GET kejisousou-zhili-formal-v3/_search 
{
  "size": 200, 
  "sort": [
    {
      "post_time": {
        "order": "desc"
      }
    }
  ]
}

GET kejisousou-en-zhili-formal-v2/_search 
{
  "query": {
    "range": {
      "post_time": {
        "gte": "2021-10-01 00:00:00",
        "lte": "2021-12-04 00:00:00"
      }
    }
  }, 
  "size": 0, 
  "aggs": {
    "NAME": {
      "date_histogram": {
        "field": "post_time",
        "interval": "day"
      }
    }
  }
}

GET kejisousou-formal/_count

GET kejisousou-formal/_search
{
  "query": {
    "term": {
      "entry_id": {
        "value": "647571"
      }
    }
  }, 
  "size": 0, 
  "aggs": {
    "NAME": {
      "date_histogram": {
        "field": "post_time",
        "interval": "day"
      }
    }
  }
}

GET page/_search 
{
  "query": {
    "term": {
      "entry_id": {
        "value": "647601"
      }
    }
  }, 
  "size": 0, 
  "aggs": {
    "NAME": {
      "date_histogram": {
        "field": "post_time",
        "interval": "day"
      }
    }
  }
}

GET kejisousou-yuce-formal-v4/_search
{
  "query": {
    "query_string": {
      "default_field": "include_time",
      "query": "\"\""
    }
  }
}

GET kejisousou-yuce-formal-v4/_search
{
  "query": {
    "term": {
      "include_time": {
        "value": ""
      }
    }
  }
}

GET kejisousou-zhili-formal-v3/_search
{
  "query": {
    "bool": {
      "must_not": [
        {
          "exists": {
            "field": "include_time"
          }
        },
        {
          "range": {
            "post_time": {
              "gte": "2021-11-01 00:00:00",
              "lte": "2021-12-01 00:00:00"
            }
          }
        }
      ]
    }
  }
}


GET data_king-202304,weixin_weibo-202304,community2-202304/_search
{
  "query": {
    "terms": {
      "url": [
        "http://www.douyin.com/video/7224079029245152550"
      ]
    }
  }
}



GET page/_search
{
  "query": {
    "range": {
      "post_time": {
        "gte": "2023-03-29 00:00:00",
        "lte": "2023-04-03 00:00:00"
      }
    }
  }, 
  "size": 10, 
  "_source": ["text", "site_name", "url"]
}

GET kejisousou-yuce-formal-v4/_search 
{
  "size": 0, 
  "aggs": {
    "NAME": {
      "date_histogram": {
        "field": "include_time",
        "interval": "day"
      }
    }
  }
}

GET kejisousou-yuce-formal-v4/_search
{
  "query": {
    "range": {
      "post_time": {
        "gte": "2021-11-01 00:00:00",
        "lte": "2021-12-05 00:00:00"
      }
    }
  }, 
  "size": 0, 
  "aggs": {
    "NAME": {
      "date_histogram": {
        "field": "post_time",
        "interval": "day"
      }
    }
  }
}

GET kejisousou-yuce-formal-v4/_search
{
  "sort": [
    {
      "include_time": {
        "order": "desc"
      }
    }
  ]
}

GET kejisousou-yuce-formal-v4/_count
{
  "query": {
    "range": {
      "include_time": {
        "gte": "2022-01-01 00:00:00"
      }
    }
  }
}

GET kejisousou-en-zhili-formal-v2/_count

GET kejisousou-en-yuce-formal-v3/_search
{
  "size": 0, 
  "aggs": {
    "NAME": {
      "date_histogram": {
        "field": "include_time",
        "interval": "day"
      }
    }
  }
}


GET kejisousou-en-zhili-formal-v2/_search
{
  "size": 0, 
  "aggs": {
    "NAME": {
      "date_histogram": {
        "field": "include_time",
        "interval": "day"
      }
    }
  }
}

GET kejisousou-en-zhili-formal-v2/_search
{
  "query": {
    "bool": {
      "must": [
        {
          "exists": {
            "field": "include_time"
          }
        }
      ]
    }
  }
}

GET kejisousou-zhili-formal-v3/_search
{
  "size": 0, 
  "aggs": {
    "NAME": {
      "date_histogram": {
        "field": "include_time",
        "interval": "day"
      }
    }
  }
}

GET kejisousou-formal


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

GET mayanan

PUT mayanan/zky_doc/1
{
  "author_id":10
}
GET mayanan/_search
{
  "_source": ["author_id_str"]
}

GET kejisousou-en-yuce-formal-v3/_search 
{
  "size": 0, 
  "aggs": {
    "NAME": {
      "date_histogram": {
        "field": "include_time",
        "interval": "day"
      }
    }
  }
}

GET kejisousou-en-zhili-formal-v2/_search
{
  "size": 0, 
  "aggs": {
    "NAME": {
      "date_histogram": {
        "field": "include_time",
        "interval": "day"
      }
    }
  }
}

GET kejisousou-en-yuce-formal-v3/_search 
{
  "size": 20, 
  "sort": [
    {
      "post_time": {
        "order": "desc"
      }
    }
  ]
}

GET kejisousou-en-formal/_search
{
  "size": 20, 
  "sort": [
    {
      "post_time": {
        "order": "desc"
      }
    }
  ]
}

GET kejisousou-en-zhili-formal-v2/_search 
{
  "size": 0, 
  "aggs": {
    "NAME": {
      "date_histogram": {
        "field": "include_time",
        "interval": "day"
      }
    }
  }
}

GET kejisousou-en-yuce-formal-v3/_search 
{
  "size": 0, 
  "aggs": {
    "NAME": {
      "date_histogram": {
        "field": "include_time",
        "interval": "day"
      }
    }
  }
}

GET kejisousou-en-formal/_search 
{
  "size": 20, 
  "sort": [
    {
      "post_time": {
        "order": "desc"
      }
    }
  ]
}

GET kejisousou-en-formal/_search 
{
  "query": {
    "query_string": {
      "default_field": "text",
      "query": "的"
    }
  }, 
  "size": 0, 
  "aggs": {
    "NAME": {
      "terms": {
        "field": "entry_id",
        "size": 1000
      }
    }
  }
}

GET kejisousou-en-formal/_search 
{
  "query": {
    "query_string": {
      "default_field": "entry_id",
      "query": "\"647193\" OR \"647196\" OR \"646447\" OR \"646342\" OR \"647194\" OR \"646448\" OR \"647195\" OR \"647197\" OR \"646449\" OR \"646450\""
    }
  }, 
  "size": 0, 
  "aggs": {
    "NAME": {
      "terms": {
        "field": "entry_id",
        "size": 1000
      }
    }
  }
}

GET kejisousou-en-formal/_search 
{
  "query": {
    "term": {
      "site_name": {
        "value": "The University of Western Australia"
      }
    }
  }, 
  "size": 200
}


GET page/_search 
{
  "query": {
    "query_string": {
      "default_field": "entry_id",
      "query": "\"647342\""
    }
  }
}


GET kejisousou-en-formal/_count


GET kejisousou-yuce-formal-v4/_search 
{
  "size": 0, 
  "aggs": {
    "NAME": {
      "date_histogram": {
        "field": "include_time",
        "interval": "day"
      }
    }
  }
}

GET kejisousou-yuce-formal-v4/_search 
{
  "query": {
    "term": {
      "yuce_text.raw": {
        "value": "实现自动泊车"
      }
    }
  }
}

GET kejisousou-zhili-formal-v3/_search  
{
  "sort": [
    {
      "post_time": {
        "order": "asc"
      }
    }
  ], 
  "size": 50
}

GET kejisousou-en-formal/_count

GET page/_search
{
  "query": {
    "bool": {
      "must": [
        {
          "term": {
            "site_name": {
              "value": "腾讯新闻_APP"
            }
          }
        },
        {
          "term": {
            "entry_name": {
              "value": "腾讯新闻_APP"
            }
          }
        }
      ]
    }
  },
  "_source": ["text"],
  "size": 200
}

GET kejisousou-zhili-formal-v3/

PUT zjgdk-ceshi
{
  "mappings": {
    "zjgdk_doc": {
      "properties": {
        "author_name": {
          "type": "text",
          "fields": {
            "raw": {
              "type": "keyword"
            }
          },
          "fielddata": true
        },
        "include_time": {
          "type": "date",
          "format": "yyyy-MM-dd HH:mm:ss"
        },
        "is_split": {
          "type": "boolean"
        },
        "talent_text_hash": {
          "type": "text",
          "fields": {
            "keyword": {
              "type": "keyword",
              "ignore_above": 256
            }
          }
        },
        "post_time": {
          "type": "date",
          "format": "yyyy-MM-dd HH:mm:ss"
        },
        "text": {
          "type": "text"
        },
        "title": {
          "type": "text",
          "fields": {
            "raw": {
              "type": "keyword"
            }
          },
          "fielddata": true
        },
        "url": {
          "type": "text",
          "fields": {
            "raw": {
              "type": "keyword"
            }
          },
          "fielddata": true
        },
        "author": {
          "type": "text",
          "fields": {
            "keyword": {
              "type": "keyword",
              "ignore_above": 256
            }
          }
        },
        "author_type": {
          "type": "long"
        },
        "talent_text": {
          "type": "text",
          "fields": {
            "raw": {
              "type": "keyword"
            }
          }
        },
        "title_hash": {
          "type": "text",
          "fields": {
            "keyword": {
              "type": "keyword",
              "ignore_above": 256
            }
          }
        },
        "reserve_field": {
          "type": "text"
        },
        "author_id": {
          "type": "long"
        },
        "reserve_type": {
          "type": "long"
        }
      }
    }
  }
}

GET page/_search

GET _template/zjgdk-v1


GET zjgdk-v1/_search

DELETE zjgdk-v1

GET kejisousou-formal/

GET _template/kejisousou-formalv1

PUT _template/zjgdk-v1
{
  "order": 1,
  "template": "zjgdk-v1-*",
  "settings": {
    "index": {
      "analysis": {
        "analyzer": {
          "sharp_analy": {
            "lowercase": "false",
            "pattern": "#",
            "type": "pattern"
          }
        }
      },
      "number_of_shards": "1"
    }
  },
  "mappings": {
    "zjgdk_doc": {
      "properties": {
        "author_name": {
          "type": "keyword",
          "fields": {
            "text": {
              "type": "text",
              "fielddata": true
            }
          }
        },
        "include_time": {
          "type": "date",
          "format": "yyyy-MM-dd HH:mm:ss"
        },
        "is_split": {
          "type": "boolean"
        },
        "talent_text_hash": {
          "type": "keyword"
        },
        "post_time": {
          "type": "date",
          "format": "yyyy-MM-dd HH:mm:ss"
        },
        "text": {
          "type": "text"
        },
        "title": {
          "type": "text",
          "fields": {
            "keyword": {
              "type": "keyword"
            }
          },
          "fielddata": true
        },
        "url": {
          "type": "keyword",
          "fields": {
            "text": {
              "type": "text",
              "fielddata": true
            }
          }
        },
        "author": {
          "type": "keyword",
          "ignore_above": 256,
          "fields": {
            "text": {
              "type": "text"
            }
          }
        },
        "author_type": {
          "type": "long"
        },
        "talent_text": {
          "type": "text",
          "fields": {
            "keyword": {
              "type": "keyword"
            }
          }
        },
        "title_hash": {
          "type": "keyword"
        },
        "reserve_field": {
          "type": "text"
        },
        "author_id": {
          "type": "long"
        },
        "reserve_type": {
          "type": "long"
        },
        "random_num": {
          "type": "double"
        }
      }
    }
  },
  "aliases": {
    "zjgdk-v1": {}
  }
}

GET kejisousou-formal/_search 


GET kejisousou-yuce-formal-v4/_search 


GET community2/_search 
{
  "query": {
    "query_string": {
      "default_field": "url",
      "query": "http://weibo.com/1862172703/L5oiDnk4I"
    }
  }
}

GET community2/_search 
{
	"query": {
		"bool": {
			"must": [{
				"term": {
					"entry_name": {
						"value": "新浪微博"
					}
				}
			}, {
				"term": {
					"url.keyword": {
						"value": "http://weibo.com/1862172703/L5oiDnk4I"
					}
				}
			}, {
				"range": {
					"post_time": {
						"gte": "2021-12-06 00:05:00",
						"lt": "2021-12-10 00:08:00"
					}
				}
			}]
		}
	}
}


GET community2/_search 
{
  "_source": [
      "url",
      "text"
  ],
  "sort": "post_time",
  "query": {
      "bool": {
          "must": [
              {
                  "term": {
                      "entry_name": {
                          "value": "新浪微博"
                      }
                  }
              },
              {
                  "term": {
                      "author_id": {
                          "value": "1934183965"
                      }
                  }
              }
          ]
      }
  }
}

GET wei/_search
{
  "size": 0, 
  "aggs": {
    "category_aggs": {
      "terms": {
        "field": "entry_name",
        "size": 10
      }
    }
  }
}

GET wei/_search 
{
  "query": {
    "term": {
      "entry_name": {
        "value": "微信"
      }
    }
  }
}

GET wei/_count
{
  "query": {
    "bool": {
      "must": [
        {
          "term": {
            "entry_name": {
              "value": "微信"
            }
          }
        },
        {
          "range": {
            "post_time": {
              "gte": "2021-12-06 00:00:00",
              "lt": "2021-12-06 23:59:59"
            }
          }
        }
      ]
    }
  }
}

GET wei/_search 
{
  "query": {
    "bool": {
      "must": [
        {
          "term": {
            "entry_name": {
              "value": "微信"
            }
          }
        },
        {
          "range": {
            "post_time": {
              "gte": "2021-12-06 00:00:00",
              "lte": "2021-12-12 23:59:59"
            }
          }
        }
      ]
    }
  }
}

GET page/_search
{
  "query": {
    "term": {
      "site_name": {
        "value": "网易"
      }
    }
  }, 
  "size": 0,
  "aggs": {
    "cat": {
      "terms": {
        "field": "entry_id",
        "size": 10
      }
    }
  }
}


GET page/_search
{
  "query": {
    "term": {
      "entry_id": {
        "value": 48037
      }
    }
  }, 
  "size": 0,
  "aggs": {
    "cat": {
      "terms": {
        "field": "site_name",
        "size": 10
      }
    }
  }
}


GET community2/_search
{
  "query": {
    "term": {
      "url": {
        "value": "http://new.qq.com/rain/a/20211214A0CP8J00"
      }
    }
  }
}


GET page/_search
{
  "query": {
    "term": {
      "url": {
        "value": "https://new.qq.com/rain/a/20211214A0CP8J00"
      }
    }
  }
}

GET page/_search
{
  "query": {
    "match_phrase": {
      "title": "预约页面秒崩！玲娜贝儿被炒出天价？上海迪士尼回应……"
    }
  }
}

GET page/_search
{
  "query": {
    "term": {
      "entry_id": {
        "value": 120
      }
    }
  },
  "size": 500
}

GET page/_search
{
  "query": {
    "term": {
      "entry_name": {
        "value": "易车号"
      }
    }
  },
  "size": 500
}


GET page/_search
{
  "query": {
    "match_phrase": {
      "title": "预约页面秒崩！玲娜贝儿被炒出天价？上海迪士尼回应……"
    }
  }
}



GET page/_search
{
  "query": {
    "bool": {
      "must": [
        {
          "term": {
            "site_name": {
              "value": "大风号"
            }
          }
        },
        {
          "term": {
            "entry_id": {
              "value": 625936
            }
          }
        }
      ]
    }
  }
}


GET page/_search
{
  "query": {
    "term": {
      "media_id": {
        "value": 166055
      }
    }
  }
}


GET page/_search 
{
  "query": {
    "term": {
      "site_name": {
        "value": "舆情通"
      }
    }
  }
}


GET page/_search 
{
  "query": {
    "bool": {
      "must": [
        {
          "term": {
            "site_name": {
              "value": "舆情通"
            }
          }
        },
        {
          "query_string": {
            "default_field": "entry_name",
            "query": "\"今日头条\" OR \"一点资讯\" OR \"搜狐号\" OR \"网易号\" OR \"大鱼号\" OR \"百家号\" OR \"南方号\" OR \"太平洋号\" OR \"知乎专栏\" OR \"新华社\" OR \"经济日报\" OR \"红星新闻\" OR \"上游新闻\" OR \"紫牛新闻\" OR \"周到上海\" OR \"金融时报\" OR \"晶报\" OR \"二三里\""
          }
        },
        {
          "range": {
            "post_time": {
              "gte": "2021-12-06 00:00:00",
              "lt": "2021-12-12 23:59:59"
            }
          }
        }
      ]
    }
  }
}


GET page/_search
{
  "query": {
    "bool": {
      "must": [
        {
          "term": {
            "entry_name": {
              "value": "媒体库"
            }
          }
        }
      ]
    }
  },
  "size": 0, 
  "aggs": {
    "category_aggs": {
      "terms": {
        "field": "media_id",
        "size": 1000
      }
    }
  }
}


GET data_king-202207,weixin_weibo-202207,community2-202207/_search
{
  "query": {
    "bool": {
      "filter": {
        "bool": {
          "must": [
            {
              "bool": {
                "should": [
                  {
                    "match_phrase": {
                      "title": "元宇宙"
                    }
                  },
                  {
                    "match_phrase": {
                      "text": "元宇宙"
                    }
                  },
                  {
                    "match_phrase": {
                      "title": "Metaverse"
                    }
                  },
                  {
                    "match_phrase": {
                      "text": "Metaverse"
                    }
                  }
                ]
              }
            }
          ]
        }
      }
    }
  }
}



GET data_king-202207,weixin_weibo-202207,community2-202207/_search
{
  "query": {
    "terms": {
      "url": [
        "https://xueqiu.com/2115521729/224245029"
      ]
    }
  }
}


GET zjgdk-v2/_search
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


GET zjgdk-v2-202207/_search
{
  "size": 5000,
  "sort": [
    {
      "include_time": {
        "order": "desc"
      }
    }
  ]
}


GET zjgdk-v2/_search
{
  "query": {
    "terms": {
      "url": [
        "https://tech.ifeng.com/c/8RE5XXwcwXA"
      ]
    }
  }
}


GET zjgdk-v2/_search 
{
  "query": {
    "bool": {
      "must": [
        {
          "match_phrase": {
            "talent_text": "玲娜贝儿"
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
  },
  "size": 100
}


GET zjgdk-v1/_search 
{
  "size": 0, 
  "aggs": {
    "cat": {
      "terms": {
        "field": "author_type",
        "size": 10
      }
    }
  }
}


PUT _template/zjgdk-v2
{
  "order": 1,
  "template": "zjgdk-v2-*",
  "settings": {
    "index": {
      "analysis": {
        "analyzer": {
          "sharp_analy": {
            "lowercase": "false",
            "pattern": "#",
            "type": "pattern"
          }
        }
      },
      "number_of_shards": "1"
    }
  },
  "mappings": {
    "zjgdk_doc": {
      "properties": {
        "author_name": {
          "type": "keyword",
          "fields": {
            "text": {
              "type": "text",
              "fielddata": true
            }
          }
        },
        "include_time": {
          "type": "date",
          "format": "yyyy-MM-dd HH:mm:ss"
        },
        "is_split": {
          "type": "boolean"
        },
        "talent_text_hash": {
          "type": "keyword"
        },
        "post_time": {
          "type": "date",
          "format": "yyyy-MM-dd HH:mm:ss"
        },
        "text": {
          "type": "text"
        },
        "title": {
          "type": "text",
          "fields": {
            "keyword": {
              "type": "keyword"
            }
          },
          "fielddata": true
        },
        "site_name": {
          "type": "keyword",
          "fields": {
            "text": {
              "type": "text",
              "fielddata": true
            }
          }
        },
        "entry_name": {
          "type": "keyword",
          "fields": {
            "text": {
              "type": "text",
              "fielddata": true
            }
          }
        },
        "url": {
          "type": "keyword",
          "fields": {
            "text": {
              "type": "text",
              "fielddata": true
            }
          }
        },
        "author": {
          "type": "keyword",
          "ignore_above": 256,
          "fields": {
            "text": {
              "type": "text"
            }
          }
        },
        "author_type": {
          "type": "long"
        },
        "talent_text": {
          "type": "text",
          "fields": {
            "keyword": {
              "type": "keyword"
            }
          }
        },
        "title_hash": {
          "type": "keyword"
        },
        "reserve_field": {
          "type": "text"
        },
        "author_id": {
          "type": "long"
        },
        "reserve_type": {
          "type": "long"
        },
        "random_num": {
          "type": "double"
        }
      }
    }
  },
  "aliases": {
    "zjgdk-v2": {}
  }
}


GET _template/zjgdk-v2

GET zjgdk-v2/_search


GET zjgdk-v1/_search 
{
  "query": {
    "bool": {
      "must": [
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


GET zjgdk-v1/_search 
{
  "query": {
    "term": {
      "url": {
        "value": "http://mp.weixin.qq.com/s?__biz=MzI5MjExMTkwMw==&mid=2650939414&idx=1&sn=c1299161236950dfff8d5a6657b4b315"
      }
    }
  }
}


GET zjgdk-v2/_search 
{
  "query": {
    "bool": {
      "must": [
        {
          "term": {
            "author_type": {
              "value": 2
            }
          }
        }
      ]
    }
  }
}


GET zjgdk-v2/_search 
{
  "query": {
    "bool": {
      "must": [
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


GET zjgdk-v1/_count 
{
  "query": {
    "bool": {
      "must": [
        {
          "match_phrase": {
            "talent_text": "奥密克戎"
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


GET zjgdk-v2/_search 
{
  "query": {
    "term": {
      "url": {
        "value": "http://mp.weixin.qq.com/s?__biz=MzIwOTI3NTYwMQ==&mid=2650333109&idx=1&sn=8e5189d6ba3b67fd607031c14223227c"
      }
    }
  }
}


GET zjgdk-v2/_search
{
  "size": 20, 
  "sort": [
    {
      "include_time": {
        "order": "desc"
      }
    }
  ]
}


GET zjgdk-v2/_update_by_query
{
  "query": {
    "term": {
      "author": {
        "value": "中国CEO冯思瀚"
      }
    }
  }
}


GET zjgdk-v2/_search 

{
  "query": {
    "term": {
      "author": {
        "value": "大众中国CEO冯思瀚"
      }
    }
  }
}


POST zjgdk-v2/_delete_by_query
{
  "query": {
    "term": {
      "url": {
        "value": "http://mp.weixin.qq.com/s?__biz=MzA4NTk5NTcwNg==&mid=2650174720&idx=6&sn=9b0260215f968ab3e040d139569b6912"
      }
    }
  }
}

GET zjgdk-v2/_search  
{
  "size": 10,
  "_source": "post_time",
  "sort": [
    {
      "post_time": {
        "order": "desc"
      }
    }
  ]
}


GET zjgdk-v2/_search  
{
  "query": {
    "range": {
      "include_time": {
        "gte": "2022-01-14 00:00:00",
        "lte": "2022-02-06 23:59:59"
      }
    }
  }
}

GET zjgdk-v2/_search  
{
  "query": {
    "range": {
      "post_time": {
        "gte": "2022-01-14 00:00:00",
        "lte": "2022-02-06 23:59:59"
      }
    }
  }
}

GET zjgdk-v2/_search 
{
  "query": {
    "bool": {
      "must": [
        {
          "range": {
            "post_time": {
              "gte": "2022-01-14 00:00:00",
              "lte": "2022-02-06 23:59:59"
            }
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

GET zjgdk-v2/_search  
{
  "query": {
    "range": {
      "post_time": {
        "gte": "2021-01-14 00:00:00",
        "lte": "2022-01-13 23:59:59"
      }
    }
  }
}


GET kejisousou-yuce-formal-v4/_search 
{
  "query": {
    "terms": {
      "yuce_author_type": [
        0,
        1,
        4
      ]
    }
  }
}


GET kejisousou-zhili-formal-v3/_search 
{
  "query": {
    "terms": {
      "zhili_author_type": [
        0,
        1,
        4
      ]
    }
  }
}


GET kejisousou-formal/_search 
{
  "size": 1,
  "_source": "include_time",
  "sort": [
    {
      "include_time": {
        "order": "desc"
      }
    }
  ]
}

GET zjgdk-v2/_search 
{
  "size": 100,
  "_source": "post_time",
  "sort": [
    {
      "post_time": {
        "order": "asc"
      }
    }
  ]
}

GET zjgdk-v2/_search 
{
  "query": {
    "match_phrase": {
      "talent_text": "\"冰墩墩\" OR \"雪容融\""
    }
  }
}


GET zjgdk-v2/_search 
{
  "query": {
    "query_string": {
      "default_field": "talent_text",
      "query": "\"乌克兰\""
    }
  }
}


GET zjgdk-v2/_search 
{
	"query": {
		"bool": {
			"must": [{
				"query_string": {
					"default_field": "talent_text",
					"query": "\"乌克兰\" OR \"冰墩墩\""
				}
			}, {
				"term": {
					"author_type": {
						"value": 1
					}
				}
			}]
		}
	}
}

GET zjgdk-v2/_search 

GET zjgdk-v2/_search
{
  "query": {
    "bool": {
      "filter": {
        "bool": {
          "must": [
            {
              "query_string": {
                "default_field": "talent_text",
                "query": "汽车"
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

GET zjgdk-v2/_search
{
  "query": {
    "bool": {
      "filter": {
        "bool": {
          "must": [
            {
              "query_string": {
                "default_field": "talent_text",
                "query": "两会"
              }
            }
          ]
        }
      }
    }
  }
}


GET zjgdk-v2/_search 
{
  "query": {
    "match_phrase": {
      "talent_text": "冰墩墩"
    }
  },
  "size": 0,
  "aggs": {
    "NAME": {
      "date_histogram": {
        "field": "post_time",
        "interval": "day"
      }
    }
  }
}


GET kejisousou-yuce-formal-v4/_search 
{
  "size": 0, 
  "aggs": {
    "NAME": {
      "date_histogram": {
        "field": "include_time",
        "interval": "day"
      }
    }
  }
}


GET kejisousou-zhili-formal-v3/_search 
{
  "size": 0, 
  "aggs": {
    "NAME": {
      "date_histogram": {
        "field": "post_time",
        "interval": "day"
      }
    }
  }
}


GET kejisousou-zhili-formal-v3/_search 
{
  "size": 0, 
  "aggs": {
    "NAME": {
      "date_histogram": {
        "field": "include_time",
        "interval": "day"
      }
    }
  }
}

GET kejisousou-en-zhili-formal-v2/_search 
{
  "size": 0, 
  "aggs": {
    "NAME": {
      "date_histogram": {
        "field": "include_time",
        "interval": "day"
      }
    }
  }
}

GET kejisousou-zhili-formal-v3/_search 
{
  "query": {
    "match_phrase": {
      "point_text": "要提高政治站位，服从服务于国家重大战略，积极担当作为，结合我区资源禀赋和产业结构实际，加强顶层设计"
    }
  }
}

GET kejisousou-zhili-formal-v3/_search
{
  "size": 1,
  "sort": [
    {
      "include_time": {
        "order": "desc"
      }
    }
  ]
}


GET zjgdk-v2/_search
{
  "query": {
    "bool": {
      "filter": {
        "bool": {
          "must": [
            {
              "query_string": {
                "default_field": "talent_text",
                "query": "利用"
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

GET zjgdk-v2/_search
{
  "query": {
    "match_phrase": {
      "author": "乘联会秘书长崔东树"
    }
  }
}

GET zjgdk-v2/_search
{
  "size": 0,
  "aggs": {
    "time_aggs": {
      "date_histogram": {
        "field": "post_time",
        "time_zone": "+08:00",
        "interval": "day",
        "format": "yyyy-MM"
      }
    }
  }
}

GET zjgdk-v2/_search
{
  "query": {
    "term": {
      "url": {
        "value": "http://mp.weixin.qq.com/s?__biz=MzA4NTM5OTQxOQ==&mid=2447600578&idx=1&sn=5c54dfaf53065154cd93ee2220eca6be"
      }
    }
  }
}

GET zjgdk-v2/_search
{
  "query": {
    "bool": {
      "must": [
        {
          "term": {
            "author": {
              "value": "乘联会秘书长崔东树"
            }
          }
        },
        {
          "range": {
            "post_time": {
              "gte": "2022-01-04 00:00:00",
              "lte": "2022-01-06 02:03:00"
            }
          }
        }
      ]
    }
  },
  "sort": [
    {
      "post_time": {
        "order": "desc"
      }
    }
  ],
  "size": 200,
  "_source": ["post_time", "talent_text"]
}

GET zjgdk-v2/_search
{
  "size": 20,
  "_source": "include_time",
  "sort": [
    {
      "include_time": {
        "order": "asc"
      }
    }
  ]
}

GET zjgdk-v2/_search
{
  "query": {
    "bool": {
      "must": [
        {
          "match_phrase": {
            "text": "乘联会秘书长崔东树"
          },
          
        }
      ]
    }
  }
}

zjgdk-v2/_delete_by_query
{
  "query": {
    "match_phrase": {
      "author": ""
    }
  }
}

GET page,wei,community2/_search 
{
  "query": {
    "query_string": {
      "default_field": "text",
      "query": "乘联会秘书长崔东树"
    }
  }
}

GET page,wei,community2/_search 
{
  "query": {
    "query_string": {
      "default_field": "title",
      "query": "条款不平等，多家新能源车企被点名！比亚迪、小鹏问题率超53%"
    }
  }
}


GET page,wei,community2/_search 
{
  "query": {
    "bool": {
      "must": [
        {
          "term": {
            "title.keyword": {
              "value": "条款不平等，多家新能源车企被点名！比亚迪、小鹏问题率超53%"
            }
          }
        }
      ]
    }
  }
}


GET page,wei,community2/_search
{
  "query": {
    "bool": {
      "must": [
        {
          "match_phrase": {
            "text": "乘联会秘书长崔东树"
          }
        },
        {
          "range": {
            "post_time": {
              "gte": "2021-12-06 00:00:00",
              "lte": "2022-03-19 00:00:00"
            }
          }
        }
      ]
    }
  }
}

GET page,wei,community2/_search
{
  "query": {
    "bool": {
      "must": [
        {
          "match_phrase": {
            "text": "乘联会秘书长崔东树"
          }
        },
        {
          "range": {
            "post_time": {
              "gte": "2022-01-04 20:00:00",
              "lte": "2022-01-05 02:03:00"
            }
          }
        }
      ]
    }
  }
}

GET wei/_search 
{
  	"query": {
		"bool": {
			"must": [{
				"term": {
					"entry_name": {
						"value": "微信"
					}
				}
			}, {
				"range": {
					"include_time": {
						"gte": "2021-12-06 00:00:00",
						"lt": "2022-03-19 00:00:00"
					}
				}
			}, {
				"match_phrase": {
					"text": "乘联会秘书长崔东树"
				}
			}]
		}
	}
}

GET zjgdk-v2/_search
{
  "query": {
    "term": {
      "author_type": {
        "value": 1
      }
    }
  },
  "_source": []
}

PUT _template/zjgdk-fullname-v1
{
  "order": 1,
  "template": "zjgdk-fullname-v1-*",
  "settings": {
    "index": {
      "analysis": {
        "analyzer": {
          "sharp_analy": {
            "lowercase": "false",
            "pattern": "#",
            "type": "pattern"
          }
        }
      },
      "number_of_shards": "1"
    }
  },
  "mappings": {
    "zjgdk_doc": {
      "properties": {
        "author_name": {
          "type": "keyword",
          "fields": {
            "text": {
              "type": "text",
              "fielddata": true
            }
          }
        },
        "include_time": {
          "type": "date",
          "format": "yyyy-MM-dd HH:mm:ss"
        },
        "is_split": {
          "type": "boolean"
        },
        "talent_text_hash": {
          "type": "keyword"
        },
        "post_time": {
          "type": "date",
          "format": "yyyy-MM-dd HH:mm:ss"
        },
        "text": {
          "type": "text"
        },
        "title": {
          "type": "text",
          "fields": {
            "keyword": {
              "type": "keyword"
            }
          },
          "fielddata": true
        },
        "site_name": {
          "type": "keyword",
          "fields": {
            "text": {
              "type": "text",
              "fielddata": true
            }
          }
        },
        "entry_name": {
          "type": "keyword",
          "fields": {
            "text": {
              "type": "text",
              "fielddata": true
            }
          }
        },
        "url": {
          "type": "keyword",
          "fields": {
            "text": {
              "type": "text",
              "fielddata": true
            }
          }
        },
        "author": {
          "type": "keyword",
          "ignore_above": 256,
          "fields": {
            "text": {
              "type": "text"
            }
          }
        },
        "author_type": {
          "type": "long"
        },
        "talent_text": {
          "type": "text",
          "fields": {
            "keyword": {
              "type": "keyword"
            }
          }
        },
        "title_hash": {
          "type": "keyword"
        },
        "reserve_field": {
          "type": "text"
        },
        "author_id": {
          "type": "long"
        },
        "reserve_type": {
          "type": "long"
        },
        "random_num": {
          "type": "double"
        }
      }
    }
  },
  "aliases": {
    "zjgdk-fullname-v1": {}
  }
}

GET zjgdk-fullname-v1/_search

GET /zjgdk-v2*/_alias

GET zjgdk-v2/_search


GET page,wei,community2/_search
{
  "query": {
    "bool": {
      
    }
  }
}

GET _cat/indices?v

GET weixin_weibo-201*/_count

GET page,wei,community2/_search 
{
  "query": {
    "term": {
      "url": {
        "value": "https://www.toutiao.com/i1737524469057549"
      }
    }
  }
}


GET zjgdk-v2-20/_search 

GET zjgdk-v2-202101/_search

GET zjgdk-v2-202102/_search


GET zjgdk-v2/_search
{
  "size": 0,
  "aggs": {
    "time_aggs": {
      "date_histogram": {
        "field": "post_time",
        "time_zone": "+08:00",
        "interval": "day",
        "format": "yyyy-MM"
      }
    }
  }
}

GET zjgdk-v2/_count


GET zjgdk-v2/_count
{
  "query": {
    "bool": {
      "must": [
        {
          "query_string": {
            "default_field": "talent_text",
            "query": "\"元宇宙\" OR \"Metaverse\" OR \"虚拟现实\" OR \"VR\" OR \"增强现实\" OR \"AR\" OR \"混合现实\" OR \"MR\" OR \"人机交互\" OR \"HMI\" OR \"裸眼3D\" OR \"数字化身\" OR \" Autostereoscopy\" OR \"Digital avatar\" OR \"NFT\" OR \"物联网\" OR \"数字孪生\" OR \"云计算\" OR \"人工智能\" OR \"AI\" OR \"区块链\" OR \"Blockchain\" OR \"数字藏品\" OR \"Digital Collections\" OR \"5G\" OR \"6G\" OR \"沉浸式体验\" OR \"大数据\" OR \"围墙花园\" OR \"智能合约\" OR \"虚拟世界\""
          }
        },
        {
          "range": {
            "post_time": {
              "gte": "2021-01-01 00:00:00",
              "lte": "2022-07-15 00:00:00"
            }
          }
        }
      ]
    }
  }
}


GET kejisousou-zhili-formal-v3/_count

GET kejisousou-zhili-formal-v3/_count
{
  "query": {
    "bool": {
      "must": [
        {
          "query_string": {
            "default_field": "zhili_text",
            "query": "\"元宇宙\" OR \"Metaverse\" OR \"虚拟现实\" OR \"VR\" OR \"增强现实\" OR \"AR\" OR \"混合现实\" OR \"MR\" OR \"人机交互\" OR \"HMI\" OR \"裸眼3D\" OR \"数字化身\" OR \" Autostereoscopy\" OR \"Digital avatar\" OR \"NFT\" OR \"物联网\" OR \"数字孪生\" OR \"云计算\" OR \"人工智能\" OR \"AI\" OR \"区块链\" OR \"Blockchain\" OR \"数字藏品\" OR \"Digital Collections\" OR \"5G\" OR \"6G\" OR \"沉浸式体验\" OR \"大数据\" OR \"围墙花园\" OR \"智能合约\" OR \"虚拟世界\""
          }
        },
        {
          "range": {
            "post_time": {
              "gte": "2021-01-01 00:00:00",
              "lte": "2021-11-07 00:00:00"
            }
          }
        }
      ]
    }
  }
}


GET kejisousou-points-formal/_search
{
  "query": {
    "bool": {
      "must": [
        {
          "query_string": {
            "default_field": "point_text",
            "query": "\"元宇宙\" OR \"Metaverse\" OR \"虚拟现实\" OR \"VR\" OR \"增强现实\" OR \"AR\" OR \"混合现实\" OR \"MR\" OR \"人机交互\" OR \"HMI\" OR \"裸眼3D\" OR \"数字化身\" OR \" Autostereoscopy\" OR \"Digital avatar\" OR \"NFT\" OR \"物联网\" OR \"数字孪生\" OR \"云计算\" OR \"人工智能\" OR \"AI\" OR \"区块链\" OR \"Blockchain\" OR \"数字藏品\" OR \"Digital Collections\" OR \"5G\" OR \"6G\" OR \"沉浸式体验\" OR \"大数据\" OR \"围墙花园\" OR \"智能合约\" OR \"虚拟世界\""
          }
        },
        {
          "range": {
            "post_time": {
              "gte": "2021-01-01 00:00:00",
              "lte": "2021-11-07 00:00:00"
            }
          }
        }
      ]
    }
  }
}


GET page,wei,community2/_count 
{
  "query": {
    "bool": {
      "must": [
        {
          "query_string": {
            "default_field": "title",
            "query": "\"元宇宙\" OR \"Metaverse\" OR \"虚拟现实\" OR \"VR\" OR \"增强现实\" OR \"AR\" OR \"混合现实\" OR \"MR\" OR \"人机交互\" OR \"HMI\" OR \"裸眼3D\" OR \"数字化身\" OR \" Autostereoscopy\" OR \"Digital avatar\" OR \"NFT\" OR \"物联网\" OR \"数字孪生\" OR \"云计算\" OR \"人工智能\" OR \"AI\" OR \"区块链\" OR \"Blockchain\" OR \"数字藏品\" OR \"Digital Collections\" OR \"5G\" OR \"6G\" OR \"沉浸式体验\" OR \"大数据\" OR \"围墙花园\" OR \"智能合约\" OR \"虚拟世界\""
          }
        },
        {
          "range": {
            "post_time": {
              "gte": "2021-01-01 00:00:00",
              "lte": "2021-11-07 00:00:00"
            }
          }
        }
      ]
    }
  }
}


GET page/_count 
{
  "query": {
    "bool": {
      "must": [
        {
          "query_string": {
            "default_field": "text",
            "query": "\"元宇宙\" OR \"Metaverse\" OR \"虚拟现实\" OR \"VR\" OR \"增强现实\" OR \"AR\" OR \"混合现实\" OR \"MR\" OR \"人机交互\" OR \"HMI\" OR \"裸眼3D\" OR \"数字化身\" OR \" Autostereoscopy\" OR \"Digital avatar\" OR \"NFT\" OR \"物联网\" OR \"数字孪生\" OR \"云计算\" OR \"人工智能\" OR \"AI\" OR \"区块链\" OR \"Blockchain\" OR \"数字藏品\" OR \"Digital Collections\" OR \"5G\" OR \"6G\" OR \"沉浸式体验\" OR \"大数据\" OR \"围墙花园\" OR \"智能合约\" OR \"虚拟世界\""
          }
        },
        {
          "range": {
            "post_time": {
              "gte": "2021-01-01 00:00:00",
              "lte": "2021-11-07 00:00:00"
            }
          }
        }
      ]
    }
  }
}

GET wei/_count 
{
  "query": {
    "bool": {
      "must": [
        {
          "query_string": {
            "default_field": "text",
            "query": "\"元宇宙\" OR \"Metaverse\" OR \"虚拟现实\" OR \"VR\" OR \"增强现实\" OR \"AR\" OR \"混合现实\" OR \"MR\" OR \"人机交互\" OR \"HMI\" OR \"裸眼3D\" OR \"数字化身\" OR \" Autostereoscopy\" OR \"Digital avatar\" OR \"NFT\" OR \"物联网\" OR \"数字孪生\" OR \"云计算\" OR \"人工智能\" OR \"AI\" OR \"区块链\" OR \"Blockchain\" OR \"数字藏品\" OR \"Digital Collections\" OR \"5G\" OR \"6G\" OR \"沉浸式体验\" OR \"大数据\" OR \"围墙花园\" OR \"智能合约\" OR \"虚拟世界\""
          }
        },
        {
          "range": {
            "post_time": {
              "gte": "2021-01-01 00:00:00",
              "lte": "2021-11-07 00:00:00"
            }
          }
        }
      ]
    }
  }
}

GET community2/_count 
{
  "query": {
    "bool": {
      "must": [
        {
          "query_string": {
            "default_field": "text",
            "query": "\"元宇宙\" OR \"Metaverse\" OR \"虚拟现实\" OR \"VR\" OR \"增强现实\" OR \"AR\" OR \"混合现实\" OR \"MR\" OR \"人机交互\" OR \"HMI\" OR \"裸眼3D\" OR \"数字化身\" OR \" Autostereoscopy\" OR \"Digital avatar\" OR \"NFT\" OR \"物联网\" OR \"数字孪生\" OR \"云计算\" OR \"人工智能\" OR \"AI\" OR \"区块链\" OR \"Blockchain\" OR \"数字藏品\" OR \"Digital Collections\" OR \"5G\" OR \"6G\" OR \"沉浸式体验\" OR \"大数据\" OR \"围墙花园\" OR \"智能合约\" OR \"虚拟世界\""
          }
        },
        {
          "range": {
            "post_time": {
              "gte": "2021-01-01 00:00:00",
              "lte": "2021-11-07 00:00:00"
            }
          }
        }
      ]
    }
  }
}


GET wei/_count 
{
  "query": {
    "bool": {
      "must": [
        {
          "query_string": {
            "default_field": "title",
            "query": "\"元宇宙\" OR \"Metaverse\" OR \"虚拟现实\" OR \"VR\" OR \"增强现实\" OR \"AR\" OR \"混合现实\" OR \"MR\" OR \"人机交互\" OR \"HMI\" OR \"裸眼3D\" OR \"数字化身\" OR \" Autostereoscopy\" OR \"Digital avatar\" OR \"NFT\" OR \"物联网\" OR \"数字孪生\" OR \"云计算\" OR \"人工智能\" OR \"AI\" OR \"区块链\" OR \"Blockchain\" OR \"数字藏品\" OR \"Digital Collections\" OR \"5G\" OR \"6G\" OR \"沉浸式体验\" OR \"大数据\" OR \"围墙花园\" OR \"智能合约\" OR \"虚拟世界\""
          }
        },
        {
          "range": {
            "post_time": {
              "gte": "2021-01-01 00:00:00",
              "lte": "2021-11-07 00:00:00"
            }
          }
        }
      ]
    }
  }
}

GET zjgdk-v2/_count
{
  "query": {
    "bool": {
      "must": [
        {
          "range": {
            "post_time": {
              "gte": "2021-01-01 00:00:00",
              "lte": "2021-11-06 00:00:00"
            }
          }
        }
      ]
    }
  }
}


GET weixin_weibo-202001

GET zjgdk-v2/_count
{
  "query": {
    "bool": {
      "must": [
        {
          "query_string": {
            "default_field": "title",
            "query": "\"元宇宙\" OR \"Metaverse\" OR \"虚拟现实\" OR \"VR\" OR \"增强现实\" OR \"AR\" OR \"混合现实\" OR \"MR\" OR \"人机交互\" OR \"HMI\" OR \"裸眼3D\" OR \"数字化身\" OR \" Autostereoscopy\" OR \"Digital avatar\" OR \"NFT\" OR \"物联网\" OR \"数字孪生\" OR \"云计算\" OR \"人工智能\" OR \"AI\" OR \"区块链\" OR \"Blockchain\" OR \"数字藏品\" OR \"Digital Collections\" OR \"5G\" OR \"6G\" OR \"沉浸式体验\" OR \"大数据\" OR \"围墙花园\" OR \"智能合约\" OR \"虚拟世界\""
          }
        },
        {
          "range": {
            "post_time": {
              "gte": "2021-01-01 00:00:00",
              "lte": "2022-07-18 00:00:00"
            }
          }
        }
      ]
    }
  }
}


GET data_king-202106/_count
{
  "query": {
    "bool": {
      "must": [
        {
          "query_string": {
            "default_field": "text",
            "query": "\"元宇宙\" OR \"Metaverse\" OR \"虚拟现实\" OR \"VR\" OR \"增强现实\" OR \"AR\" OR \"混合现实\" OR \"MR\" OR \"人机交互\" OR \"HMI\" OR \"裸眼3D\" OR \"数字化身\" OR \" Autostereoscopy\" OR \"Digital avatar\" OR \"NFT\" OR \"物联网\" OR \"数字孪生\" OR \"云计算\" OR \"人工智能\" OR \"AI\" OR \"区块链\" OR \"Blockchain\" OR \"数字藏品\" OR \"Digital Collections\" OR \"5G\" OR \"6G\" OR \"沉浸式体验\" OR \"大数据\" OR \"围墙花园\" OR \"智能合约\" OR \"虚拟世界\""
          }
        }
      ]
    }
  }
}

GET zjgdk-v2/_count
{
  "query": {
    "bool": {
      "must": [
        {
          "range": {
            "post_time": {
              "gte": "2021-01-01 00:00:00",
              "lte": "2021-11-06 00:00:00"
            }
          }
        }
      ]
    }
  }
}


GET zjgdk-v2/_count
{
  "query": {
    "bool": {
      "must": [
        {
          "query_string": {
            "default_field": "title",
            "query": "\"元宇宙\" OR \"Metaverse\" OR \"虚拟现实\" OR \"VR\" OR \"增强现实\" OR \"AR\" OR \"混合现实\" OR \"MR\" OR \"人机交互\" OR \"HMI\" OR \"裸眼3D\" OR \"数字化身\" OR \" Autostereoscopy\" OR \"Digital avatar\" OR \"NFT\" OR \"物联网\" OR \"数字孪生\" OR \"云计算\" OR \"人工智能\" OR \"AI\" OR \"区块链\" OR \"Blockchain\" OR \"数字藏品\" OR \"Digital Collections\" OR \"5G\" OR \"6G\" OR \"沉浸式体验\" OR \"大数据\" OR \"围墙花园\" OR \"智能合约\" OR \"虚拟世界\""
          }
        },
        {
          "range": {
            "post_time": {
              "gte": "2021-01-01 00:00:00",
              "lte": "2021-11-06 00:00:00"
            }
          }
        }
      ]
    }
  }
}


GET community2-202207,data_king-202207,weixin_weibo-202207/_count
{
  "query": {
    "terms": {
      "url": [
        "http://www.dongchedi.com/ugc/article/1738844790495256",
        "https://www.dongchedi.com/ugc/article/1738844790495256",
        "http://www.dongchedi.com/ugc/article/1738860727840782",
        "https://www.dongchedi.com/ugc/article/1738860727840782",
        "http://www.dongchedi.com/ugc/article/1738844790495256/",
        "https://www.dongchedi.com/ugc/article/1738844790495256/",
        "http://www.dongchedi.com/ugc/article/1738860727840782/",
        "https://www.dongchedi.com/ugc/article/1738860727840782/"
      ]
    }
  }
}

GET community2-202207,data_king-202207,weixin_weibo-202207/_count
{
  "query": {
    "terms": {
      "url": [
        "http://www.toutiao.com/i1738844790495256",
        "https://www.toutiao.com/i1738844790495256",
        "http://www.toutiao.com/i1738860727840782",
        "https://www.toutiao.com/i1738860727840782",
        "http://www.toutiao.com/i1738844790495256/",
        "https://www.toutiao.com/i1738844790495256/",
        "http://www.toutiao.com/i1738860727840782/",
        "https://www.toutiao.com/i1738860727840782/"
      ]
    }
  }
}


GET community2-202207,data_king-202207,weixin_weibo-202207/_count
{
  "query": {
    "terms": {
      "url": [
        "https://www.douyin.com/video/7122045284531588393",
        "https://www.douyin.com/video/7122045284531588393"
      ]
    }
  }
}


GET .kibana/_count

GET .kibana/_search 

GET _cat/indices?v

GET kejisousou-formalv1-202009

GET mayanan/_search 

GET kejisousou-formal/_search


GET zjgdk-v2/_count
{
  "query": {
    "bool": {
      "must": [
        {
          "query_string": {
            "default_field": "talent_text",
            "query": "\"核废水\""
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

GET zjgdk-v2/_count
{
  "query": {
    "bool": {
      "must": [
        {
          "query_string": {
            "default_field": "talent_text",
            "query": "\"核污染水\""
          }          
        }
      ]
    }
  }
}

GET zjgdk-v2/_count
{
  "query": {
    "bool": {
      "must": [
        {
          "query_string": {
            "default_field": "talent_text",
            "query": "\"核废水\""
          }          
        }
      ]
    }
  }
}

GET page,wei,community2/_count 
{
  "query": {
    "bool": {
      "should": [
        {
          "query_string": {
            "default_field": "text",
            "query": "\"核废水\""
          }
        }
      ]
    }
  }
}

GET page,wei,community2/_count 
{
  "query": {
    "bool": {
      "should": [
        {
          "match_phrase": {
            "text": "核废水"
          }
        }
      ]
    }
  }
}

GET _cat/indices?v

GET page,wei,community2/_count 
{
  "query": {
    "bool": {
      "must": [
        {
          "query_string": {
            "default_field": "text",
            "query": "\"元宇宙\" OR \"Metaverse\""
          }
        },
        {
          "range": {
            "post_time": {
              "gte": "2021-01-01 00:00:00",
              "lte": "2022-06-30 23:59:59"
            }
          }
        }
      ]
    }
  }
}

GET zjgdk-v2/_count
{
  "query": {
    "bool": {
      "must": [
        {
          "query_string": {
            "default_field": "text",
            "query": "\"元宇宙\" OR \"Metaverse\""
          }
        },
        {
          "range": {
            "post_time": {
              "gte": "2021-01-01 00:00:00",
              "lte": "2022-06-30 23:59:59"
            }
          }
        }
      ]
    }
  }
}



GET zjgdk-v2/_count
{
  "query": {
    "bool": {
      "must": [
        {
          "query_string": {
            "default_field": "title",
            "query": "\"元宇宙\" OR \"Metaverse\""
          }
        },
        {
          "range": {
            "post_time": {
              "gte": "2021-01-01 00:00:00",
              "lte": "2022-06-30 23:59:59"
            }
          }
        }
      ]
    }
  }
}


GET page,wei,community2/_search 
{
  "query": {
    "bool": {
      "must": [
        {
          "query_string": {
            "default_field": "text",
            "query": "\"元宇宙\" OR \"Metaverse\""
          }
        },
        {
          "range": {
            "post_time": {
              "gte": "2021-01-01 00:00:00",
              "lte": "2022-06-30 23:59:59"
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
        "time_zone": "+08:00",
        "interval": "month",
        "format": "yyyy-MM"
      }
    }
  }
}

GET page,wei,community2/_search 
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


GET data_king-202208/_search
{
  "query": {
    "bool": {
      "filter": [
        {
          "range": {
            "post_time": {
              "gte": "2022-08-30 00:00:00",
              "lte": "2022-08-30 23:59:59"
            }
          }
        }
      ],
      "must": [
        {
          "match_phrase": {
            "text": "核废水"
          }
        }
      ]
    }
  }
}


GET kejisousou-formal/_count

GET kejisousou-formal/_search
{
  "query": {
    "range": {
      "post_time": {
        "gte": "2020-01-01 00:00:00",
        "lt": "2022-01-01 00:00:00"
      }
    }
  },
  "size": 0
  , "aggs": {
    "moth": {
      "date_histogram": {
        "field": "post_time",
        "interval": "month"
      }
    }
  }
}


GET kejisousou-formal/_search
{
  "query": {
    "range": {
      "post_time": {
        "gte": "2020-01-01 00:00:00",
        "lt": "2022-01-01 00:00:00"
      }
    }
  },
  "size": 10000,
  "sort": [
    {
      "post_time": "desc",
      "include_time": "desc"
    }
  ]
}


GET kejisousou-formal/_search
{
  "query": {
    "range": {
      "post_time": {
        "gte": "2022-01-01 00:00:00"
      }
    }
  },
  "size": 100,
  "sort": [
    {
      "post_time": "asc",
      "include_time": "asc"
    }
  ]
}

GET data
GET weixin_weibo-202210,data_king-202210,community2-202210/_search
{
  "query": {
    "terms": {
      "url": [
"http://k.sina.cn/article_5069495542_12e2a5cf602701dcvx.html?sinawapsharesource=newsapp",
"http://cj.sina.com.cn/articles/view/5069495542/12e2a5cf602701dcvx",
"http://www.qctt.cn/news/1363429",
"http://www.qctt.cn/news/1363456",
"http://www.ixigua.com/i7159102508395171085",
"http://www.bilibili.com/read/cv19355897",
"http://www.douyin.com/video/7159121144728079630",
"http://mp.weixin.qq.com/s?__biz=Mzg3NDY2MTYzNg==&mid=2247487149&idx=2&sn=dbba12aab94b14432d406af6e9cdd852",
"http://m.qctt.cn/news/1363470",
"http://www.qctt.cn/news/1363470",
"http://www.yidianzixun.com/article/0jh0hKf7",
"http://www.autohome.com.cn/dealer/202210/930766429.html",
"http://www.yidianzixun.com/article/0jh214nR",
"http://www.sohu.com/a/600258151_104421",
"http://m.sohu.com/a/600258151_104421",
"http://mp.weixin.qq.com/s?__biz=MzA5NjA4NTAxMw==&mid=2651647597&idx=4&sn=2fb1872b798456bf942c54b789dcdabc",
"http://mp.weixin.qq.com/s?__biz=Mzg3NTE5MDA4NA==&mid=2247538545&idx=1&sn=c5276fc8b0d9d8135f43a820622b8f4d",
"https://k.sina.cn/article_5069495542_12e2a5cf602701dcvx.html?sinawapsharesource=newsapp",
"https://cj.sina.com.cn/articles/view/5069495542/12e2a5cf602701dcvx",
"https://www.qctt.cn/news/1363429",
"https://www.qctt.cn/news/1363456",
"https://www.ixigua.com/i7159102508395171085",
"https://www.bilibili.com/read/cv19355897",
"https://www.douyin.com/video/7159121144728079630",
"https://mp.weixin.qq.com/s?__biz=Mzg3NDY2MTYzNg==&mid=2247487149&idx=2&sn=dbba12aab94b14432d406af6e9cdd852",
"https://m.qctt.cn/news/1363470",
"https://www.qctt.cn/news/1363470",
"https://www.yidianzixun.com/article/0jh0hKf7",
"https://www.autohome.com.cn/dealer/202210/930766429.html",
"https://www.yidianzixun.com/article/0jh214nR",
"https://www.sohu.com/a/600258151_104421",
"https://m.sohu.com/a/600258151_104421",
"https://mp.weixin.qq.com/s?__biz=MzA5NjA4NTAxMw==&mid=2651647597&idx=4&sn=2fb1872b798456bf942c54b789dcdabc",
"https://mp.weixin.qq.com/s?__biz=Mzg3NTE5MDA4NA==&mid=2247538545&idx=1&sn=c5276fc8b0d9d8135f43a820622b8f4d"

      ]
    }
  }
}


GET wei/_search 
{
  "query": {
    "term": {
      "url": {
        "value": "http://mp.weixin.qq.com/s?__biz=MzU4OTYwMDg4Mg==&mid=2247502656&idx=3&sn=c05db640da620038b0ccd274acf93ed0"
      }
    }
  }
}


GET data_king-202210, weixin_weibo-202210, community2-202210/_search 

GET weixin_weibo-202210,data_king-202210,community2-202210/_search
{
  "query":{
    "term": {
      "url": {
        "value": "http://www.douyin.com/video/7158865001070005517"
      }
    }
  }
}


GET kejisousou-points-formal/_search
{
  "sort": [
    {
      "include_time": {
        "order": "desc"
      }
    }
  ]
  , "size": 100
}

GET kejisousou-points-formal/_count 
{
  "query": {
    "range": {
      "include_time": {
        "gte": "2022-01-01 00:00:00"
      }
    }
  }
}


GET kejisousou-points-formal/_count


GET kejisousou-formal/_count


GET page,wei,community2/_search 
{
  "query": {
    "term": {
      "url": {
        "value": "http://www.douyin.com/video/7214851580636515584"
      }
    }
  }
}

GET _template/data_king*


GET page,wei,community2/_count
{
  "query": {
    "bool": {
      "must": [
        {
          "range": {
            "post_time": {
              "gte": "2022-01-01 00:00:00",
              "lte": "2022-12-31 23:59:59"
            }
          }
        }
      ],
      "should": [
        {
          "bool": {
            "must": [
              { "match_phrase": { "text": "C-HR" } },
              { "match_phrase": { "text": "广汽丰田" } }
            ]
          }
        },
        { "match_phrase": { "text": "锋兰达" } },
        {
          "bool": {
            "must": [
              { "match_phrase": { "text": "iA5" } },
              { "match_phrase": { "text": "广汽丰田" } }
            ]
          }
        },
        {
          "bool": {
            "must": [
              { "match_phrase": { "text": "埃尔法" } },
              { "match_phrase": { "text": "广汽丰田" } }
            ]
          }
        },
        { "match_phrase": { "text": "汉兰达" } },
        { "match_phrase": { "text": "凯美瑞" } },
        { "match_phrase": { "text": "雷凌" } },
        { "match_phrase": { "text": "凌尚" } },
        { "match_phrase": { "text": "威兰达" } },
        { "match_phrase": { "text": "致享" } },
        { "match_phrase": { "text": "致炫" } },
        {
          "bool": {
            "must": [
              { "match_phrase": { "text": "赛那" } },
              { "match_phrase": { "text": "广汽丰田" } }
            ]
          }
        },
        {
          "bool": {
            "must": [
              { "match_phrase": { "text": "bZ4X" } },
              { "match_phrase": { "text": "广汽丰田" } }
            ]
          }
        },
        {
          "bool": {
            "must": [
              { "match_phrase": { "text": "CHR" } },
              { "match_phrase": { "text": "广汽丰田" } }
            ]
          }
        }
      ],
      "minimum_should_match": 1
    }
  }
}


GET data_king-2022*,community2-2022*,weixin_weibo-2022*/_count 
{
  "query": {
    "bool": {
      "must": [
        {
          "range": {
            "post_time": {
              "gte": "2022-01-01 00:00:00",
              "lte": "2022-12-31 23:59:59"
            }
          }
        }
      ],
      "should": [
        { "match_phrase": { "text": "广汽丰田" } },
        {
          "bool": {
            "must": [
              { "match_phrase": { "text": "C-HR" } },
              { "match_phrase": { "text": "丰田" } }
            ]
          }
        },
        { "match_phrase": { "text": "锋兰达" } },
        {
          "bool": {
            "must": [
              { "match_phrase": { "text": "iA5" } },
              { "match_phrase": { "text": "丰田" } }
            ]
          }
        },
        {
          "bool": {
            "must": [
              { "match_phrase": { "text": "埃尔法" } },
              { "match_phrase": { "text": "丰田" } }
            ]
          }
        },
        { "match_phrase": { "text": "汉兰达" } },
        { "match_phrase": { "text": "凯美瑞" } },
        { "match_phrase": { "text": "雷凌" } },
        { "match_phrase": { "text": "凌尚" } },
        { "match_phrase": { "text": "威兰达" } },
        { "match_phrase": { "text": "致享" } },
        { "match_phrase": { "text": "致炫" } },
        {
          "bool": {
            "must": [
              { "match_phrase": { "text": "赛那" } },
              { "match_phrase": { "text": "丰田" } }
            ]
          }
        },
        {
          "bool": {
            "must": [
              { "match_phrase": { "text": "bZ4X" } },
              { "match_phrase": { "text": "丰田" } }
            ]
          }
        },
        {
          "bool": {
            "must": [
              { "match_phrase": { "text": "CHR" } },
              { "match_phrase": { "text": "丰田" } }
            ]
          }
        }
      ],
      "minimum_should_match": 1
    }
  }
}



GET page,wei,community2/_search
{
  "query": {
    "bool": {
      "must": [
        {
          "range": {
            "post_time": {
              "gte": "2023-03-01 00:00:00",
              "lte": "2023-03-31 23:59:59"
            }
          }
        }
      ],
      "should": [
        { "match_phrase": { "text": "一汽丰田" } },
        { "match_phrase": { "text": "RAV4" } },
        {
          "bool": {
            "must": [
              { "match_phrase": { "text": "荣放" } },
              { "match_phrase": { "text": "一汽丰田" } }
            ]
          }
        },
        { "match_phrase": { "text": "卡罗拉" } },
        { "match_phrase": { "text": "柯斯达" } },
        { "match_phrase": { "text": "威驰" } },
        { "match_phrase": { "text": "威尔法" } },
        {
          "bool": {
            "must": [
              { "match_phrase": { "text": "亚洲龙" } },
              { "match_phrase": { "text": "一汽丰田" } }
            ]
          }
        },
        { "match_phrase": { "text": "亚洲狮" } },
        {
          "bool": {
            "must": [
              { "match_phrase": { "text": "奕泽" } },
              { "match_phrase": { "text": "一汽丰田" } }
            ]
          }
        }
      ],
      "minimum_should_match": 1
    }
  }
}



GET page,wei,community2/_count 
{
  "query": {
    "bool": {
      "must": [
        {
          "range": {
            "post_time": {
              "gte": "2023-03-01 00:00:00",
              "lte": "2023-03-31 23:59:59"
            }
          }
        }
      ],
      "should": [
        { "match_phrase": { "text": "东风日产" } },
        { "match_phrase": { "text": "Nissan" } },
        { "match_phrase": { "text": "e-POWER轩逸" } },
        {
          "bool": {
            "must": [{ "match_phrase": { "text": "奇骏" } }],
            "must_not": [{ "match_phrase": { "text": "宫奇骏" } }]
          }
        },
        { "match_phrase": { "text": "逍客" } },
        {
          "bool": {
            "must": [
              { "match_phrase": { "text": "劲客" } },
              { "match_phrase": { "text": "日产" } }
            ]
          }
        },
        {
          "bool": {
            "must": [
              { "match_phrase": { "text": "天籁" } },
              { "match_phrase": { "text": "日产" } }
            ]
          }
        },
        { "match_phrase": { "text": "轩逸" } },
        { "match_phrase": { "text": "骐达" } },
        {
          "bool": {
            "must": [
              { "match_phrase": { "text": "楼兰" } },
              { "match_phrase": { "text": "日产" } }
            ]
          }
        },
        { "match_phrase": { "text": "轩逸∙纯电" } },
        {
          "bool": {
            "must": [
              { "match_phrase": { "text": "Ariya" } },
              { "match_phrase": { "text": "日产" } }
            ]
          }
        }
      ],
      "minimum_should_match": 1
    }
  }
}


GET page,wei,community2/_count 
{
  "query": {
    "bool": {
      "must": [
        {
          "range": {
            "post_time": {
              "gte": "2023-03-01 00:00:00",
              "lte": "2023-03-31 23:59:59"
            }
          }
        }
      ],
      "should": [
        { "match_phrase": { "text": "上汽通用" } },
        { "match_phrase": { "text": "别克" } },
        { "match_phrase": { "text": "昂科威" } },
        { "match_phrase": { "text": "昂科拉" } },
        { "match_phrase": { "text": "昂科旗" } },
        { "match_phrase": { "text": "威朗" } },
        { "match_phrase": { "text": "雪佛兰" } },
        { "match_phrase": { "text": "凯越" } },
        { "match_phrase": { "text": "君越" } },
        { "match_phrase": { "text": "君威" } },
        { "match_phrase": { "text": "迈锐宝XL" } },
        { "match_phrase": { "text": "科鲁泽" } },
        { "match_phrase": { "text": "科沃兹" } },
        { "match_phrase": { "text": "科迈罗" } },
        { "match_phrase": { "text": "沃兰多" } },
        {
          "bool": {
            "must": [{ "match_phrase": { "text": "探界者" } }],
            "must_not": [{ "match_phrase": { "text": "辰探界" } }]
          }
        },
        { "match_phrase": { "text": "创酷" } }
      ],
      "minimum_should_match": 1
    }
  }
}


GET page,wei,community2/_count 
{
  "query": {
    "bool": {
      "must": [
        {
          "range": {
            "post_time": {
              "gte": "2023-03-01 00:00:00",
              "lte": "2023-03-31 23:59:59"
            }
          }
        }
      ],
      "should": [
        { "match_phrase": { "text": "一汽大众" } },
        { "match_phrase": { "text": "迈腾" } },
        {
          "bool": {
            "must": [
              { "match_phrase": { "text": "宝来" } },
              { "match_phrase": { "text": "大众" } }
            ]
          }
        },
        { "match_phrase": { "text": "高尔夫" } },
        { "match_phrase": { "text": "速腾" } },
        {
          "bool": {
            "must": [
              { "match_phrase": { "text": "CC" } },
              { "match_phrase": { "text": "大众" } }
            ]
          }
        },
        { "match_phrase": { "text": "探岳" } },
        { "match_phrase": { "text": "探歌" } },
        { "match_phrase": { "text": "探影" } },
        { "match_phrase": { "text": "蔚领" } },
        { "match_phrase": { "text": "揽境" } }
      ],
      "minimum_should_match": 1
    }
  }
}



GET page,wei,community2/_count 
{
  "query": {
    "bool": {
      "must": [
        {
          "range": {
            "post_time": {
              "gte": "2023-03-01 00:00:00",
              "lte": "2023-03-31 23:59:59"
            }
          }
        }
      ],
      "should": [
        { "match_phrase": { "text": "上汽大众" } },
        {
          "bool": {
            "must": [
              { "match_phrase": { "text": "ID3" } },
              { "match_phrase": { "text": "大众" } }
            ]
          }
        },
        {
          "bool": {
            "must": [
              { "match_phrase": { "text": "ID.4X" } },
              { "match_phrase": { "text": "大众" } }
            ]
          }
        },
        {
          "bool": {
            "must": [
              { "match_phrase": { "text": "ID.6X" } },
              { "match_phrase": { "text": "大众" } }
            ]
          }
        },
        { "match_phrase": { "text": "POLO PLUS" } },
        { "match_phrase": { "text": "朗逸" } },
        { "match_phrase": { "text": "凌渡" } },
        { "match_phrase": { "text": "帕萨特" } },
        { "match_phrase": { "text": "桑塔纳" } },
        { "match_phrase": { "text": "途昂" } },
        { "match_phrase": { "text": "途观" } },
        { "match_phrase": { "text": "途铠" } },
        { "match_phrase": { "text": "途岳" } },
        {
          "bool": {
            "must": [
              { "match_phrase": { "text": "威然" } },
              { "match_phrase": { "text": "大众" } }
            ]
          }
        },
        { "match_phrase": { "text": "新辉昂" } }
      ],
      "minimum_should_match": 1
    }
  }
}



GET page,wei,community2/_count 
{
  "query": {
    "bool": {
      "must": [
        {
          "range": {
            "post_time": {
              "gte": "2023-03-01 00:00:00",
              "lte": "2023-03-31 23:59:59"
            }
          }
        }
      ],
      "should": [
        { "match_phrase": { "text": "东风本田" } },
        { "match_phrase": { "text": "CR-V" } },
        {
          "bool": {
            "must": [
              { "match_phrase": { "text": "LIFE" } },
              { "match_phrase": { "text": "本田" } }
            ]
          }
        },
        { "match_phrase": { "text": "M-NV" } },
        { "match_phrase": { "text": "UR-V" } },
        { "match_phrase": { "text": "XR-V" } },
        { "match_phrase": { "text": "艾力绅" } },
        { "match_phrase": { "text": "思域" } },
        { "match_phrase": { "text": "享域" } },
        { "match_phrase": { "text": "CIVIC TypeR" } },
        { "match_phrase": { "text": "英仕派" } },
        { "match_phrase": { "text": "e:NS1" } },
        {
          "bool": {
            "must": [
              { "match_phrase": { "text": "CRV" } },
              { "match_phrase": { "text": "本田" } }
            ]
          }
        }
      ],
      "minimum_should_match": 1
    }
  }
}



# 174w
GET page,wei,community2/_count 
{
  "query": {
    "bool": {
      "must": [
        {
          "range": {
            "post_time": {
              "gte": "2023-03-01 00:00:00",
              "lte": "2023-03-31 23:59:59"
            }
          }
        }
      ],
      "should": [
        { "match_phrase": { "text": "广汽本田" } },
        { "match_phrase": { "text": "VE-1" } },
        {
          "bool": {
            "must": [
              { "match_phrase": { "text": "奥德赛" } },
              { "match_phrase": { "text": "本田" } }
            ]
          }
        },
        {
          "bool": {
            "must": [
              { "match_phrase": { "text": "奥德赛" } },
              { "match_phrase": { "text": "广汽" } }
            ]
          }
        },
        { "match_phrase": { "text": "缤智" } },
        { "match_phrase": { "text": "飞度" } },
        { "match_phrase": { "text": "冠道" } },
        { "match_phrase": { "text": "皓影" } },
        { "match_phrase": { "text": "凌派" } },
        { "match_phrase": { "text": "雅阁" } },
        { "match_phrase": { "text": "绎乐" } },
        { "match_phrase": { "text": "型格" } },
        { "match_phrase": { "text": "极湃1" } },
        { "match_phrase": { "text": "致在" } },
        {
          "bool": {
            "must": [
              { "match_phrase": { "text": "VE1" } },
              { "match_phrase": { "text": "本田" } }
            ]
          }
        }
      ],
      "minimum_should_match": 1
    }
  }
}




GET page,wei,community2/_count 
{
  "query": {
    "bool": {
      "must": [
        {
          "range": {
            "post_time": {
              "gte": "2023-03-01 00:00:00",
              "lte": "2023-03-31 23:59:59"
            }
          }
        }
      ],
      "should": [
        { "match_phrase": { "text": "小鹏汽车" } },
        {
          "bool": {
            "must": [
              { "match_phrase": { "text": "G3i" } },
              { "match_phrase": { "text": "小鹏" } }
            ]
          }
        },
        {
          "bool": {
            "must": [
              { "match_phrase": { "text": "G9" } },
              { "match_phrase": { "text": "小鹏" } }
            ]
          }
        },
        {
          "bool": {
            "must": [
              { "match_phrase": { "text": "P5" } },
              { "match_phrase": { "text": "小鹏" } }
            ]
          }
        },
        {
          "bool": {
            "must": [
              { "match_phrase": { "text": "P7" } },
              { "match_phrase": { "text": "小鹏" } }
            ]
          }
        },
        {
          "bool": {
            "must": [
              { "match_phrase": { "text": "P7i" } },
              { "match_phrase": { "text": "小鹏" } }
            ]
          }
        }
      ],
      "minimum_should_match": 1
    }
  }
}



# 下边没跑
GET page,wei,community2/_count 
{
  "query": {
    "bool": {
      "must": [
        {
          "range": {
            "post_time": {
              "gte": "2023-03-01 00:00:00",
              "lte": "2023-03-31 23:59:59"
            }
          }
        }
      ],
      "should": [
        { "match_phrase": { "text": "蔚来" } }
      ],
      "minimum_should_match": 1
    }
  }
}

GET community2,page,wei/_search
{
  "query": {
    "term": {
      "url": {
        "value": "http://www.douyin.com/video/7224281180089175328"
      }
    }
  }
}
```

