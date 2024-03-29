`nginx` 启动  
`nginx -s stop` 停止  
`nginx -s quit` 安全退出  
`nginx -s reload` 重新加载，用的非常多，每次更改配置文件，都要执行 reload  
`nginx -t` 查看 nginx 的状态  

`ps -aux | grep nginx`  

`uwsgi --ini /home/xxkt_uwsgi/xxkt_uwsgi.ini`   
`ps -aux | grep uwsgi`  
`uwsgi --stop /home/xxkt_uwsgi/master.pid`  
`uwsgi --reload /home/xxkt_uwsgi/master.pid`  


### 安装软件：

1、安装 Python  
这个再装的时候在谷歌搜一下，看看有没有好的教程  
apt-get update  
apt-get install software-properties-common  
add-apt-repository ppa:deadsnakes/ppa(安装源，可以是别的源)  
apt-get install python3.6  

创建软连接  
which python3  
cd /usr/bin  
rm python3  
ln -s python3.6 python  

删除软连接和删除快捷方式是一样的：rm python  

pip -V  
pip install --upgrade pip  

创建虚拟环境  
pip install virtualenv  

virtualenv django_env(先 cd 到文件夹下面，比如 cd /home；这个命令会创建文件夹)  
source django_env/bin/activate  
deactivate  


2、安装 MySQL  
先去 MySQL 官网去下载 APT 文件，也就是下面这个 deb 文件  
dpkg -i mysql-apt-config_0.8.16-1_all.deb(安装包)  
ps -aux | grep mysql  
apt-get install mysql-server  
(选择版本，输入密码)  

在本地项目文件中，在 manage.py 所在目录的上级目录，执行命令 mysqldump -u root -p xxkt_db > data.sql  

在服务器中，进入 mysql 命令行环境，创建数据库，use 数据库，然后 source data.sql  

vim /etc/ssh/sshd_config  
systemctl restart ssh  
systemctl status ssh  


3、安装 mysqlclient(这个非常麻烦，搜一下看看有没有好的教程)  
apt-get install libmysqlclient-dev  
apt install libssl-dev  
apt install libcrypto++-dev   
apt-get install python3.6-dev  
pip3 install mysqlclient  


4、安装 Redis  

apt-get install redis-server  
service redis-server start  
sudo service redis-server stop  


5、安装配置 Nginx  
apt-get install nginx  

cd /etc/nginx  

sites-avaliable 可用文件  
sites-enable 已经启用文件  

先在 sites-avaliable 中创建 xxkt.conf 文件  
vim /etc/nginx/sites-available/xxkt.conf  

    server {   
        listen 80;
        server_name mayanan.top;
        charset utf-8;

        client_max_body_size 75M;

        location /static {
            alias /home/elearning/xxkt/static_collected;
        }

        location / {
            uwsgi_pass 127.0.0.1:8001;     # 这个是接 uwsgi 用的  
            include /etc/nginx/uwsgi_params;
        }
    }

cd /home 
mkdir xxkt_uwsgi   
cd xxkt_uwsgi  
vim xxkt_uwsgi.ini  

    [uwsgi]
    chdir = /home/elearning/xxkt 
    module = xxkt.wsgi:application 

    master = True   
    processes = 2   
    harakiri = 60  
    max-requests = 5000  

    socket = 127.0.0.1:8001  
    uid = 1000  
    gid = 2000  

    pidfile = /home/xxkt_uwsgi/master.pid  
    daemonize = /home/xxkt_uwsgi/xxkt.log     # 在这里可以看 log  
    vacuum = True  

[Django 文档，看 uwsgi 参数意义和配置](https://docs.djangoproject.com/zh-hans/3.1/howto/deployment/wsgi/uwsgi/)  

配置完成以后，启动 uwsgi：uwsgi --ini xxkt_uwsgi.ini   

可以查看 xxkt.log 文件  

ln -s /etc/nginx/sites-available/xxkt.conf /etc/nginx/sites-enabled/xxkt.conf  


6、安装配置 uwsgi  
pip3 install uwsgi  

mkdir xxkt_uwsgi  
vim xxkt_uwsgi.ini  

uwsgi --ini /home/xxkt_uwsgi/xxkt_uwsgi.ini   

ps -aux | grep uwsgi  

uwsgi --stop /home/xxkt_uwsgi/master.pid  
uwsgi --reload /home/xxkt_uwsgi/master.pid  

uwsgi \-\-chdir /home/elearning/xxkt \-\-http :80 \-\-module xxkt.wsgi:application  
uwsgi 参数：  
\-\-chdir 指定文件目录  
\-\-home:/home/django_env/ 指定虚拟环境  


chmod 777 banner  


### Django 项目配置  

安装完 Nginx 和 uwsgi 之前可以先测试一下   
python manage.py runserver 0.0.0.0:8000(安全组要打开 8000 端口)，要在 settings.py 中设置 allow_host=\['*']，即允许所有网站访问，然后输入：ip:8000 访问  

mkdir static_collected  
python3 manage.py collectstatic  
vim /etc/nginx/sites-enabled/xxkt.conf   

chmod 777 -R images/  

视频播放：  
<a href="javascript:play_video('http://localhost:8000/{{video.video}}')">  
要把 localhost:8000 改成 mayanan.top, 不加端口号  

settings.py  
把 debug 改为 False  
ALLOW_HOST = \['mayanan.top']  



