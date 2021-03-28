

1、[正向代理和反向代理](https://www.zhihu.com/question/24723688/answer/128105528)  
正向代理隐藏真实客户端，反向代理隐藏真实服务端。  

2、[root 和 alias 的区别](https://blog.csdn.net/CodeLixj/article/details/107859266?utm_medium=distribute.pc_relevant.none-task-blog-baidujs_title-0&spm=1001.2101.3001.4242)  

        location = /test {
                root /home/nginx/nginx/html;
        }
请求 http\://xxx/test/a.html 这个地址时，那么在服务器里面对应的真正的资源是 /home/nginx/nginx/html/test/a.html 文件  

注意：真实的路径是root指定的值加上location指定的值  

而 alias 正如其名，alias指定的路径是location的别名，不管location的值怎么写，资源的 真实路径都是 alias 指定的路径   

        location = /test {
                alias /home/nginx/nginx/html/;
        }
同样请求 http\://xxxxx/test/a.html 时，在服务器查找的资源路径是： /home/nginx/nginx/html/a.html  


#### 一个负载均衡例子  

    http {
        upstream myproject {
            server 127.0.0.1:8000 weight=3;
            server 127.0.0.1:8001;
            server 127.0.0.1:8002;
            server 127.0.0.1:8003;
        }

        server {
            listen 80;
            server_name www.domain.com;

            location / {
                proxy_pass http://myproject;
            }
        }
    }
    
    

## 视频课程  
1、[nginx反向代理与负载均衡教程](https://www.bilibili.com/video/BV1Bx411Z7Do?from=search&seid=8411968358464384743)  

location 匹配优先级：  
= 精确匹配  
^~ 匹配路径前缀  
~ 正则匹配  
/ 一般匹配  

(location =) > (location 完整路径) > (location ^~ 路径) > (location ~,~* 正则顺序) > (location 部分起始路径) > (/)  



2、[Nginx最新教程通俗易懂，40分钟搞定！](https://www.bilibili.com/video/BV1F5411J7vK?p=7&spm_id_from=pageDriver)    

Nginx 三个功能：反向代理、负载均衡、动静分离  

负载均衡，比如有的服务器 64G，有的 16G，有的 8G，那就让 64G 的权重大一些  

轮询就是顺序遍历  

`./nginx` 启动  
`./nginx -s stop` 停止  
`./nginx -s quit` 安全退出  
`./nginx -s reload` 重新加载，用的非常多，每次更改配置文件，都要执行 reload  

`ps -aux | grep nginx`  

反向代理 proxy_pass  

负载均衡 upstream  


3、[尚硅谷Nginx教程由浅入深](https://www.bilibili.com/video/BV1zJ411w7SV?from=search&seid=8411968358464384743)  

目录 /usr/sbin/  

查看版本号：./nginx -v  


全局块：  
work_processes 并发数量  

events 块：  
worker_connections 1024 支持的最大连接数 1024 个  

http 块：  
配置最多的部分，反向代理、负载均衡、动静分离都是在这里配置，还有缓存、日志等  

主要是其中的 server 块，location 位置路径，注释的部分都是例子，不能运行，用作参考  

反向代理，输入 server_name 网址，转发到 proxy_pass 网址  

        server {   
            listen 80;
            server_name mayanan.top;

            location ~ /django/ {
                proxy_pass 127.0.0.1:8000;
            }
            
            location ~ /flask/ {
                proxy_pass 127.0.0.1:5000;
            }
            
        }


负载均衡：轮询、weight、ip_hash、fair(按照后端响应时间分配)  

动静分离：动态请求，比如请求数据库内容；静态请求，比如图片和 HTML；  

通过 location 配置来访问静态资源  


        location /www/ {
            root /data/;
        }

        location /image/ {
            root /data/;
        }
    
第一个访问 data/www/ 下的内容，比如 HTML，第二个访问 data/image/ 下的内容，比如图片  

nginx 运行原理：
有一个 master 有很多 workers；master 是领导，worker 是员工；master 做的事情就是分配任务，调度  

这样重新启动的时候，有任务的可以执行任务，不受影响，其他的重新启动就行  

每一个 worker 都是一个独立的进程，一个出现异常，其他的不受影响  

一般来说 worker 数要和 CPU 数量一致  

每个 worker 的连接数，如果只是访问静态资源，就是 2 个，如果还访问动态资源，就是 4 个  

4 个 workers，每个最大连接数是 1024，那么并发请求量是：4 \* 1024 再除以 2 或 4   

