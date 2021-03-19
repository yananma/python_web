
[正向代理和反向代理](https://www.zhihu.com/question/24723688/answer/128105528)


[root 和 alias 的区别](https://blog.csdn.net/CodeLixj/article/details/107859266?utm_medium=distribute.pc_relevant.none-task-blog-baidujs_title-0&spm=1001.2101.3001.4242)  

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
    
    
