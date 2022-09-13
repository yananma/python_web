

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
        client.make_bucket("mayanan-bucket")   # bucket 名称不能有下划线
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





