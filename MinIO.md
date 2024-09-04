
pandas 读取 minio 文件：   

```python
from minio import Minio
from mx_config import mxconfig
import pandas as pd

# 设置 Minio 客户端
client = Minio(
    endpoint=mxconfig('{cyberin_minio}.host'),
    access_key=mxconfig('{cyberin_minio}.access_key'),
    secret_key=mxconfig('{cyberin_minio}.secret_key'),
    secure=False  # 如果启用 SSL，请将此选项设���为 True
)

# 设置要删除的文件夹路径和时间戳
bucket = mxconfig('{cyberin_minio}.bucket')
file_name = "static/offline/1821/测试离线匹配.csv"
client.get_object(bucket, object_name=file_name)
obj = client.get_object(bucket, object_name=file_name)


df = pd.read_csv(obj, encoding="gbk")

df.head()
```



QuickStart   

```python 
from minio import Minio
from minio.error import S3Error


def main():
    client = Minio(
        "play.min.io",  # 网址
        access_key="Q3AM3UQ867SPQQA43P2F",  # 账号
        secret_key="zuf+tfteSlswRu7BJ86wekitnifILbZam1KYY3TG",  # 密码   
    )

    found = client.bucket_exists("mayanan-bucket")  
    if not found:
        client.make_bucket("mayanan-bucket")   # bucket 名称不能有下划线，可以有中划线。
    else:
        print("Bucket already exists.")

    client.fput_object("mayanan-bucket", "in_bucket_name_一二三级分类V17.xlsx",
                       r"C:\Users\mx\PycharmProjects\local_scripts\crisis_admin\data\一二三级分类V17.xlsx")  
    # fput_object() 上传文件，参数：self；bucket 名称；上传到 bucket 以后的，在 bucket 里的文件名；本地文件。    
    print("uploaded.")


if __name__ == '__main__':
    try:
        main()
    except S3Error as e:
        print(f"error: {e}")
```

fget_object    

```python 
from minio import Minio
from minio.error import S3Error


def main():
    client = Minio(
        "play.min.io",
        access_key="Q3AM3UQ867SPQQA43P2F",
        secret_key="zuf+tfteSlswRu7BJ86wekitnifILbZam1KYY3TG",
    )
    client.fget_object("mayanan-bucket", "in_bucket_name_一二三级分类V17.xlsx",
                       r"C:\Users\mx\PycharmProjects\local_scripts\crisis_admin\data\一二三级分类V16.xlsx")
    print("download.")


if __name__ == '__main__':
    try:
        main()
    except S3Error as e:
        print(f"error: {e}")
```   





