
激活环境：`activate django_rest`  
退出环境：`deactivate`  
查看已有环境 `conda env list`

    django-admin startproject mysite  

    python manage.py runserver  
    python manage.py createsuperuser  
    python manage.py makemigration  
    python manage.py migrate  

    django-admin startapp polls  


LANGUAGE_CODE = 'zh-hans';  
TIME_ZONE = 'Asia/Shanghai'  

admin.site.site_header = '在线教育平台后台管理系统'  




多写注释  
改一改，看变化，比如 models.py 中的 verbose_name 的作用  
在报错位置使用 pysnooper  
用 python manage.py -h 查看命令  
print(Banner.objects.all().query) 看 sql 命令  
可以在 views 中使用 pysnooper  
可以看别人的网站的源码  

