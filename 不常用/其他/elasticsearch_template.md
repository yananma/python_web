
```python 
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
  },
  "aliases": {
    "zjgdk-v1": {}
  }
}
```
