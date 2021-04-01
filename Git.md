
[Git 相关大全](https://gitee.com/all-about-git)  

[learn-git-branching](https://oschina.gitee.io/learn-git-branching/)  
练习 10 遍  
第一遍：03.28-  



## 视频教程  

1、[Git最新教程通俗易懂](https://www.bilibili.com/video/BV1FE411P7B3?from=search&seid=14100441261883488493)  

### 版本迭代
Git 非常简单  

版本迭代 新的版本创建了，但是老的版本也要保留  

可以查看修改记录，可以恢复历史版本  

多人协同开发、统计工作量、跟踪开发过程  

### 版本控制  
本地版本控制  

集中版本控制，比如 SVN  
所有的版本都保存在服务器上；缺点是服务器出问题，就没法用了  

分布式版本控制 Git  
每台电脑本地都有自己的版本控制中心，每个人都拥有全部的代码；工作时不需要联网  


### Git 必要配置

`git config -l` 查看配置列表  

配置用户和邮箱：  
`git config --global user.name "mayanan"`  
`git config --global user.email "emal@163.com"`  

### Git 工作原理  

工作目录(Working Directory) 本地目录; 自己的工作台  
暂存区(Stage/Index) 临时存放改动; 座位旁边的箱子  
资源库(Repository) 本地; 工厂成品库房  
远程仓库(Remote Directory); 商店出售区  

![Git](https://github.com/yananma/python_web/blob/main/%E4%B8%8D%E5%B8%B8%E7%94%A8/img/git.png)  

 #### Git 就记住这 3 个命令就够了   
`git add .` 添加到暂存区，没有保存 . 代表所有文件  
`git commit` 提交到本地仓库  
`git push` 提交到远程仓库  

<br> 

`git pull` 从远程拉到本地  
`git reset` 从 commit 回滚过来  
`git checkout` 从暂存区减除  

`git init` 初始化文件目录  


### Git 的基本操作命令  

`git status`  

`git commit -m` m message  


.gitignore  







