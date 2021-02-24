
大体如此，操作的时候出现问题再修改补充

### 安装软件：

1、安装 Python  
这个再装的时候在谷歌搜一下，看看有没有好的教程  
apt-get update  
apt-get install software-properties-common  
apt-get install ppa-purge  
add-apt-repository ppa:deadsnakes/ppa  
apt-get install python3.6  

which python3  
rm python3  
ln -s python3.6 python3  

2、安装 MySQL  
dpkg -i mysql-apt-config_0.8.16-1_all.deb  
ps -aux | grep mysql  
apt-get install mysql-server  

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

vim xxkt.conf  
ln -s /etc/nginx/sites-available/xxkt.conf /etc/nginx/sites-enabled/xxkt.conf  

service nginx restart

5、安装配置 uwsgi  
pip3 install uwsgi  

mkdir xxkt_uwsgi  
vim xxkt_uwsgi.ini  
uwsgi --ini xxkt_uwsgi.ini   
ps -aux | grep uwsgi  

uwsgi --chdir /home/elearning/xxkt --http :80 --module xxkt.wsgi:application  
chmod 777 banner  


### Django 项目配置  

mkdir static_collected  
python3 manage.py collectstatic  
vim /etc/nginx/sites-enabled/xxkt.conf   



