
大体如此，操作的时候出现问题再修改补充

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
版本高的可能已经装好了，如果需要安装pip，可以使用命令：apt-get install python3-pip  
pip install --upgrade pip  

创建虚拟环境  
pip install virtualenv  

virtualenv django_env(先 cd 到文件夹下面，比如 cd /home；这个命令会创建文件夹；可以指定 python 版本)  
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


4、安装配置 Nginx  
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
        uwsgi_pass 127.0.0.1:8001;
        include /etc/nginx/uwsgi_params;
    }

}

cd /home 
mkdir xxkt_uwsgi   
vim xxkt.ini  
\[uwsgi]
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
daemonize = /home/xxkt_uwsgi/xxkt.log 
vacuum = True 

配置完成以后，启动 uwsgi：uwsgi --ini xxkt_uwsgi.ini   

ln -s /etc/nginx/sites-available/xxkt.conf /etc/nginx/sites-enabled/xxkt.conf  

nginx -t 看一下 nginx 的状态  

service nginx start  
service nginx stop  
service nginx restart  

history | grep nginx  


5、安装配置 uwsgi  
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
python manage.py runserver 0.0.0.0:8000(安全组要打卡 8000 端口)，要在 settings.py 中设置 allow_host=\['*']，即允许所有网站访问，然后输入：ip:8000 访问  

mkdir static_collected  
python3 manage.py collectstatic  
vim /etc/nginx/sites-enabled/xxkt.conf   


settings.py 把 debug 改为 False  

chmod 777 -R images/  

视频播放：  
<a href="javascript:play_video('http://localhost:8000/{{video.video}}')">  
要把 localhost:8000 改成 mayanan.top, 不加端口号  
