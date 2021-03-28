

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




