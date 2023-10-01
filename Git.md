
git --help     
git --help a   
git config     


## 低版本 git，本地已有项目 push 到远程 （服务器）  

1. 在 gitlab 上 new project，选择 Create blank project  
2. 创建仓库，不勾选 Initialize repository with a README  
3. 看 Push an existing folder，按照提示，复制命令运行（在 git add . 之前添加 .gitignore）
4. vim .gitignore，添加 .idea/，添加 \_\_pycache__/   
5. 低版本没有 `git init --initial-branch=main`，要自己修改分支名    
6. 先 `git init` 创建仓库，然后 `git add` 和 `git commit -m` 以后才会有 master 分支   
7. `git branch -M main`(把当前分支重命名为 main) (如果是修改任意分支命令是：`git branch -m old_name new_name`)   
8. 要用 http，不要用 ssh：`git remote add origin http://gitlab.maixunbytes.com/mayanan/extract_subtitles2.git` （如果之前已经 remote add origin 为 ssh 了，要先删除：`git remote rm origin`，再执行 remote add origin）  
9. 不用 add 和 commit，直接 push：`git push -u origin main`   


#### 高版本 git，本地已有项目 push 到远程  

1. 在 gitlab 上 new project，选择 Create blank project  
2. 创建仓库，不勾选 Initialize repository with a README  
3. 看 Push an existing folder，按照提示，复制命令运行（在 git add . 之前添加 .gitignore）    
4. vim .gitignore，添加 .idea/，添加 \_\_pycache__/   



## 基础命令  

![Git](https://github.com/yananma/python_web/blob/main/%E4%B8%8D%E5%B8%B8%E7%94%A8/img/git_command.png)  

```linux  
git status  

git add a.txt 
git commit -m "add a.txt" 
git push  

git pull   

# 删除文件要用 `git rm` 不要用 linux 的 rm 命令，如果用了 linux 的 rm 命令，就要 `git add .` 来使删除被 git 管理   

# 比较文件工作区和暂存区之间的差异
git diff -- 文件名 
```


分支  
```linux 
# 拉取特定分支  
git clone -b branch-name url   

# 创建分支  
git branch mayanan-book  

# 查看分支  
git branch -av  

# 切换分支  
git checkout mayanan-book  

# 当前分支，本地存在，远程不存在，push 到远程  
git push --set-upstream origin mayanan-book

# 删除分支  
git branch -D mayanan-book  

# 删除远程分支  
git push origin --delete mayanan-project-patch-27407  
```

删除远程 .idea 文件夹   
```python 
vim .gitignore   

添加 .idea/  

git rm --cache -r .idea  

git commit -m "delete .idea"  

git push   
```

## 功能   


### 撤销服务器上没有提交的改动    

用 git status 看，看提示信息。      

git checkout -- xposts/management/commands/push_hefushe.py    

或者用 git reset --hard HEAD     


### 回滚到指定位置   

```python 
git log -n 5  # 看要到的那个 commit 的数字   
git reset --hard 数字   
git push -f   

# 如果报错，protect branch 
在 settings -> Repository -> Protected branches 底下表格选择 Allowed to push 下拉框，可以选择 developers + maintainers，有一个 Allow force push 要选上允许，或者选择 Unprotect      

```


### git pull 不要每次都输入密码   

先在命令行输入 
```python 
git config --global credential.helper store  
```

再 git pull，再输一次用户名密码，以后就不用输了。    

可以通过 

```python 
vim ~/.git-credentials
``` 

查看里面存的用户名密码。    

如果要清除，就用 vim 打开文件，手动删除。   

查看当前策略：`git config --global credential.helper`   

暂停存储策略：`git config --global credential.helper wincred`(不知道为什么报错，不知道是不是版本的问题)   

设置缓存，默认 15 分钟内不用重复输入密码：`git config --global credential.helper cache`   



## 报错

### gitlab、pycharm 和远程服务器的关系   

运行的时候，运行的是远程服务器上的代码，也就是点 run 的时候，会连接远程，然后运行远程代码。      

git pull 的时候，pycharm 的代码和 gitlab 上的代码是一样的，但是和远程服务器的代码不一样，还要上传才行。     

如果 git push 的时候，提示 merge，merge 完以后，和上面的情况一样，远程服务器的代码是旧代码，看 merge 的文件，要从 pycharm 上传 merge 以后的文件才行。可能是一个很偏的自己不用的文件。    


### 服务器没有配置用户名密码，git clone 的时候报错说，仓库不存在    

在命令中添加用户名密码：`git clone http://user:password@gitlab.maixunbytes.com/media-library/mxlabeltool.git`，只要配置一次，以后就都可以了。   


### git pull 的时候报错：fatal: repository 'http://gitlab.maixunbytes.com/doukuan/crisis_admin.git/' not found 其实和上面的一样，也是服务器上默认的用户改变了(感觉这种方法没效果)   

`git pull http://user:password@gitlab.maixunbytes.com/doukuan/crisis_admin.git/`    


### git 拉代码报错  

fatal: Not a git repository (or any parent up to mount point /home)     
Stopping at filesystem boundary (GIT_DISCOVERY_ACROSS_FILESYSTEM not set).    

应该用 git clone 命令拉代码，却用了 git pull    


### git pull aborting   

因为服务器上的代码有改动，git pull 不成功。   

先用 git diff 文件名，比如 git diff xposts/management/commands/crisis_warning_send.py 看这个文件的修改的地方，然后复制备份文件，然后把 + 的地方删除，把 - 的地方恢复。然后再 git pull。   

git pull 成功以后，再把备份文件替换，再 git pull。   


### git pull aborting, git diff No newline at end of file   

`git reset --hard HEAD` 撤销所有未提交改动。     

或者删除本地文件，再去 git 下原文件，上传。      


### git pull aborting   

error: The following untracked working tree files would be overwritten by merge:
	models/models/origin_models.py
Please move or remove them before you merge.
Aborting    

本地文件没 git add，对比本地和远程，如果一样就删除本地，然后再 git pull       


### pycharm git push 不成功  

push 不成功，看左下角的 git 的 log  


### git push 报错   

```shell
(cyberin_env) [deploy@b79 cyberin_backend]$ git push
warning: push.default is unset; its implicit value is changing in
Git 2.0 from 'matching' to 'simple'. To squelch this message
and maintain the current behavior after the default changes, use:

  git config --global push.default matching

To squelch this message and adopt the new behavior now, use:

  git config --global push.default simple

See 'git help config' and search for 'push.default' for further information.
(the 'simple' mode was introduced in Git 1.7.11. Use the similar mode
'current' instead of 'simple' if you sometimes use older versions of Git)

Everything up-to-date
```

文件没有 commit 成功      


### git push 报错：kex_exchange_identification: Connection closed by remote host   

可能是原来是 ssh，但是服务器不再允许通过 ssh 访问了，要改成 http   

```git 
# 1. 查看当前remote
git remote -v

# 2. 切换到http：
git remote set-url origin https://github.com/username/repository.git

# 3. 切换到ssh：
git remote set-url origin git@github.com:username/repository.git
``` 


### protect branch   

在 settings -> Repository -> Protected branches 底下表格选择 Allowed to push 下拉框，可以选择 developers + maintainers 或者选择 Unprotect    


### git push 报错说请联系 maintainer   

没有权限，当前是 developer，应该改成 maintainer       




*** 

为什么要学 Git？  

1. GitHub 就是一个巨大的代码仓库，有众多的开源代码，可以创造巨大的价值，可以节省大量的时间和精力  
2. 版本管理，可以恢复  
3. 协同开发  


## gitlab 相关  

在 gitlab 中搜代码，可以在右上角搜，然后选择项目就可以在这个项目下搜索     


## [玩转 Git 三剑客](https://time.geekbang.org/course/intro/100021601?tab=catalog)  


### 第一章 Git 基础  

### 01 课程综述  

没有 Git 之前，就是 copy 目录，自己设置版本，沟通成本极高，容易覆盖文件  

分布式版本控制系统，各自都拥有完整的一套版本库。脱离服务端以后，客户端仍然可以管理版本  

Git 的优势：最优的存储能力、非凡的性能、开源、容易备份、支持离线操作、容易定制工作流程  


### 02 安装 Git  

安装教程：https://git-scm.com/book/zh/v2/%E8%B5%B7%E6%AD%A5-%E5%AE%89%E8%A3%85-Git  


### 03 Git 配置  

`git config` 直接回车，显示的是各种可用参数  

`git config --list` 查看所有配置  

查看 git 的用户名和邮箱  
```python 
git config user.name
git config user.email
```

设置 git 用户名和邮箱  
```python 
$ git config --global user.name  "mayanan"     
$ git config --global user.email "yanan.ma@maixunbytes.com"          
```

设置了以后，就可以看到是谁提交的代码，有问题就可以发邮件交流  

不写 global 参数，默认是 \-\-local 是对某一个仓库生效。不常用，global 最常用。    


查看配置  
```python 
git config --list --local  
git config --list --global  
```


### 04 创建第一个仓库  

建仓库有两种情况，一种是代码已经存在，一种是代码还不存在。  

第一种情况：  
```python 
cd 项目所在的文件夹  
git init  
```

第二种情况：  
```python 
cd 到某个文件夹  
git init 项目名  
cd 项目名  
```

创建一个文件：`touch readme.md`  
add: `git add readme.md`  
查看：`git status`  
commit：`git commit -m "add readme"`  
查看：`git log`  


### 05 认识工作区和暂存区  

add 放入暂存区，表示已经被 git 管理了，不过暂存就是暂时存放的意思，还没有正式提交的。  

如果新做的修改，还不如暂存区的效果好，就可以回退。  

经常要看状态，所以经常需要使用命令 `git status`  

add 后面可以加多个文件，包括文件夹  
`git add 文件名 文件名 文件夹名`  

add 全部使用命令 `git add .` 或 `git add -u` 


### 06 重命名文件  

`git mv readme readme.md`  


### 07 








[Git 相关大全](https://gitee.com/all-about-git)  

[learn-git-branching](https://oschina.gitee.io/learn-git-branching/)  



## 1、[Git与GitHub基础全套完整版教程](https://www.bilibili.com/video/BV1pW411A7a5)  

数据备份保存所有历史版本、版本管理可以切换到历史版本、查看修改时间，修改人，修改内容的历史记录、多人协同修改、权限控制、分支管理多线开发，提高效率；一个错误，其他不受影响  

git logo 上就是一个分支，课件分支是其引以为傲的一个特性  

git 在本地开发，不需要联网，与 Linux 全面兼容  

fork 以后就是改变了所有者了，复制一份，改成自己的名字，就有了所有的权限；可以发起 pull request 审核以后 merge 到原来的版本  

### git 本地配置  

右键，git bash here  

`git init` 初始化本地库  

.git 目录下存放的是和本地库相关的子目录和文件，不要修改  

签名的作用就是区分不同的开发人员的身份，所以要求很弱，这个签名和 GitHub 登录账号没有任何关系    

签名级别  
* 项目级别/仓库级别，仅在本地库范围内生效，就是当前文件夹下: `git config user.name tom` 和 `git config user.email tom@gmail.com`  
* 系统用户级别，就是在当前操作系统的范围。`git config --global user.name tom` 和 `git config --global user.email tom@gmail.com`    


### git 基本命令  

`git status` 查看工作区、暂存区状态，会显示在哪个分支上，会显示待提交的内容；这个命令和 Linux 里的 ll 一样的作用，用的最多  

以下命令执行完以后，可以经常使用 `git status` 查看状态  
`vim hello.txt` 创建文件，里面写两行 aaaaa 和 bbbbbb  

`git add hello.txt` 将文件从工作区放入暂存区   

`git commit -m 'add hello.txt file' hello.txt` 写注释，因为是团队合作，自己看历史记录也更清楚  

`cat hello.txt`  

`vim hello.txt` 添加一行 ccccc，修改文件  

`git add hello.txt`  

`git commit -m 'modify hello.txt' hello.txt`  

`git log` 查看历史版本，从而可以实现前进后退，head 就是指针  

多添加几次 commit，添加一行提交一次，一直到 h  

再用 `git log` 命令，内容就非常多了，要使用 `git log --oneline`  

`git reflog` 会显示移动指针的相对次数，在 head 后面的花括号里  

版本前进后退的本质就是移动指针  

有三种移动方式  
* 基于索引值，最方便，推荐方式
* 使用 ^，一个 ^ 后退一步  
* 使用 ~，指定数值，不用写很多 ^，就好像一万写'万'字就行了，不用写一万条横线  

`git reset --hard [局部索引值，就是 git reflog 后每一行最前面的一段 hash 值]`  
比如 `git reset --hard c5fc5b9`  
使用 `git reflog` 可以看到 head 已经改变了位置  
使用 `cat hello.txt` 可以看到，内容变成了之前版本的内容  

`git reset --hard HEAD^`  
`git reset --hard HEAD~n`  


删除恢复命令  
`vim a.txt` 创建新的文件，写入 aaaaa  
`git add a.txt`  
`git commit -m 'create new file a.txt' a.txt` 删除文件可以再次恢复的前提就是删除之前提交过，就是有这一步  

`rm a.txt` 删除文件  
`git status`  

`git add a.txt`  
`git commit -m 'delete a.txt' a.txt`  
`git reflog`  
`git reset --hard HEAD^` 删除的文件就恢复了  


比较文件的差异，查看修改的内容  
`vim apple.txt` 写入 5 行 apple  
`git add apple.txt`  
`git commit -m 'add apple.txt' apple.txt`  

`vim apple.txt` 在第三行后面添加一个 apple  
`git diff apple.txt`  

`git add apple.txt` 添加到暂存区  
`git diff` 不会有内容显示  
`git diff HEAD apple.txt`  

### git 分支  

git 分支功能是用的最多的  

`git brance -v` 查看所有分支  
`git branch bugFix` 创建分支  
`git branch -v`  
`git checkout bugFix`  
`git branch -v`  

`ll` 可以看到 bugFix 分支下的文件和 master 分支下的文件一模一样  

`vim apple.txt` 在第五行添加 edit by bugFix  
`git add apple.txt`  
`git commit -m 'modify apple.txt by bugFix branch' apple.txt`  

这时候 bugFix 分支就已经比 master 分支前进了一步了，比如说已经修复了 bug 了，要让 master 分支上也生效，首先要先切换到 master 分支上  
`git checkout master`  
`git branch -v`  
`git merge bugFix`  
`cat apple.txt` 就可以看到修改内容已经合并到 master 分支上了  

合并冲突  
如果修改的是同一文件的同一位置，而内容又不一样，就会产生冲突  
`git branch -v` 可以看到合并以后，两个分支的 hash 值是一样的，说明指向的是同一个内容  
`vim hello.txt` 在最后一行最后添加 edit by master  
`git add hello.txt`  
`git commit -m 'edit by master' hello.txt`  
`git branch -v` 可以看到 master 分支已经比 bugFix 分支领先一步了  
`git checkout bugFix`  
`git branch -v`  
`vim hello.txt` 在最后一行最后添加 edit by bugFix  
`git add hello.txt`  
`git commit -m 'edit by bugFix' hello.txt`  
`git merge master` 会显示产生冲突，命令行最后会显示分支处于 merging 状态  
`vim hello.txt` 会显示冲突内容，然后和同事交流沟通，看看怎么解决  

`git status`  
`git add hello.txt`  
`git commit -m 'solve conflict'`  


### git 基本原理  


hash 操作，hash 就是一个函数，输入没变，输出一直不变，如果输入改了一点，输出就完全不同，git 靠这种机制从根本上保证数据的完整性  

git 是基于快照流来管理文件的  

创建分支，本质上就是切换了指针，并没有复制整套内容，所以效率极高  


### github 

new respository 创建新的远程仓库  

创建的时候不要添加 README，因为添加 README 时会自动创建分支 main，而后面用的分支叫 master  

复制地址，就是在 clone 地址的位置：https://github.com/yananma/10programs.git    

`git remote -v` 查看远程库  
`git remote add [别名] [远程地址]` 比如 `git add origin https://github.com/yananma/10programs.git` origin 就是别名  

`git push [别名] [分支]` 比如 `git push origin master`  

`git clone` 命令有 3 个效果，把完整的远程库下载到本地; 创建 origin 远程库别名; 初始化本地库  

`git pull` 等于 `git fetch + git merge`  

如果修改的是同一个地方，内容又不相同，先 push 的会被接受，后 push 的 push 失败，要先 pull 下来，在本地 merge  

冲突以后商量解决  

跨团队协作，比如需要别人帮忙，而这个人是别的公司的，不能跳槽过来，就要先 fork，修改以后在 github 页面，选择 Pull requests，点 New pull request，点 Create pull requests  

可以聊天交流，说明问题，详细解释自己的想法，审核代码  

使用用户密码，每次 push 都要输入用户名和密码  

先删除原内容 `rm -r ~/.ssh/`  

`ssh-keygen -t rsa -C 邮箱@qq.com` 然后一路回车，使用默认值  

`ll ~/.ssh/`  
`cat ~/.ssh/id_rsa.pub` 复制内容  

到 github settings 里，点 SSH and GPG keys，new SSH key，粘贴，title 随便取，比如 mykey  

`git remote -v` 用的还是原来的密码的地址  
在 github 上 clone 地址的地方选择 ssh 方式，复制内容 git@github.com:yananma/10programs.git  
在本地使用 `git remote add origin_ssh git@github.com:yananma/10programs.git` 创建 ssh 登录方式  
`git remote -v` 就有了 ssh 方式  
修改文件，add commit 以后使用 `git push origin_ssh master` 第一次输入 yes 确认，就不用再每次输入用户名密码了  


搜 pycharm 配置 git

gitlab 局域网搭建 github 速度快  





## 2、[Git最新教程通俗易懂](https://www.bilibili.com/video/BV1FE411P7B3?from=search&seid=14100441261883488493)  

Git 非常简单  

版本迭代 新的版本创建了，但是老的版本也要保留  

可以查看修改记录，可以恢复历史版本  

多人协同开发、统计工作量、跟踪开发过程  

集中版本控制，比如 SVN，所有的版本都保存在服务器上；缺点是服务器出问题，就没法用了  

分布式版本控制 Git，每台电脑本地都有自己的版本控制中心，每个人都拥有全部的代码；工作时不需要联网  


### Git 必要配置

`git config -l` 查看配置列表  

配置用户和邮箱：  
`git config --global user.name "mayanan"`  
`git config --global user.email "emal@163.com"`  

### Git 工作原理  

工作目录(Working Directory) 本地目录; 自己的工作台; 写代码  
暂存区(Stage/Index) 临时存放改动; 座位旁边的箱子  
资源库(Repository) 本地; 工厂成品库房; 历史版本  
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

`git commit -m` m 就是 message 备注  


.gitignore  







