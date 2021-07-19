
Ctrl + Alt + 方向键左键 跳回光标原来所在的位置；读源码用  

Shift + F10 运行  

Shift + ESC 隐藏命令结果行  

Ctrl + Shift + F10 运行当前页面(右上角选择的不是当前页面的时候)  

Alt + 1 显示隐藏当前目录  

Alt + 7 查看方法列表  

格式化代码样式  Ctrl + Alt + l  

切换 Alt + 方向键  



*** 

可以 debug，选择 dj 项目，有些是要在网页发送请求的时候才会触发  

可以在源码中打断点，可以结合源码书共同学习  

可以使用右上角的搜索功能，查找类和函数，读源码非常有帮助  

点进源码以后，点击左侧 Structure 可以看到所有的类；读源码非常有用，自己写 model 或 view 导包的时候，可以点进去看还有什么相似的方法       


PyCharm 在编写标签的时候，输入 if 按 Tab 键，就可以自动创建标签，非常方便    

可以数值切分页面，这样就可以在写 CSS 的时候，可以看到 HTML 页面  

可以使用 PyCharm 连接 MySQL  

查找 Edit -> Find；用 Vim 的搜索功能    


项目是 pycharm 的最大的管理单元  

项目下面有包，包里面有各种模块  



#### 其他设置

pycharm 非常强大，可以创建 Django flask 项目、可以连接数据库、可以使用 git 进行版本控制、可以登录 GitHub、  

打开 settings，可以使用快捷键 Ctrl + Alt + s，可以配置  

Alt + Enter 快速修复错误  

进入全屏：View -> Appearance -> Enter Full Screen    

PyCharm -> Tools -> HTTP Client -> Test RESTful Web Service 可以做简单测试    

连接数据库也非常简单，输入用户名密码和数据库名字即可  

[PyCharm 连接 MySQL 报错解决办法](https://blog.csdn.net/liuqiker/article/details/102455077)：`set global time_zone = '+8:00';`  


自动导入包设置：File -> Settings -> General -> Auto Import -> Python -> Show import popup  
导入包是alt + enter 键组合，如果弹出下拉菜单选项，说明缺少依赖，选择即可导入（不知道为什么自己设置没有效果）  


### debug：不会 debug 根本就不可能学会编程
debug 是方法，可以解决几百万个问题  

如果学 Django 的时候会 debug 能解决多少问题？能省多少时间？会容易得多  

1、打开了读源码的大门，前景无限  
2、以后可以学习公司业务  
3、编程中 debug 时间最多  
4、不用再去依赖别人  
5、可以提高自己独立解决问题，理解问题的能力  
6、没有 debug 功能会极为麻烦，自己试过，拆分组合，极为复杂，效果甚微  

每天 debug 一段源码，一个月就能灵活运用了，也能极大提高自己对 Django  和 Flask 运行原理的理解，可以读懂源码  
