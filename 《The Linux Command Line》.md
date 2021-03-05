
一次整理，终生使用  


### 1-What Is the Shell  

df: disk file 查看剩余内存  

### 2-Navigation  

pwd: print working directory  
ls: list short  
ll: list long  
实际上并不是这样，不过自己可以这么记  

目录文件按字母排序  

绝对路径和相对路径，哪一个 typing 最少就用哪一个  

cd 可以直接跳转到该用户的 home 文件下  
cd - 跳转到 previous working directory  

以 . 开头的文件，用 ls 命令看不到  
文件命名不要用空格，用下划线替代  


### 3-Exploring the System  

ls 可能是 Linux 上用得最多的命令  
ls 当前目录下文件  
ls /usr  
ls /usr /tmp; 可以展示两个文件夹下的 content  

更常见的命令模式：  
command -options arguments  
options 会 modify command 的行为，经常会带有一个 -  

ls -lh; h 是 human readable 的意思，会把大小转化成 K、M  

ll 可以看权限  
第一个 d 代表文件夹 directory，- 代表单个文件，l 代表软链接  

file 文件名 查看 file 类型  

less /etc/passwd; 查看内容；查看的时候 h 查看其它命令   

这一章有文件目录，和目录作用表格  


### 4-Manipulating Files and Directories  

用命令行可以做到图形界面所无法完成的功能，比如复制一个文件夹中所有的 HTML 文件到另一个文件夹，只复制目的地文件夹下没有的文件，或新的版本的文件。在图形界面很难做到，在 Linux 中一行命令就可以  
因为 Linux 中一切皆文件，考虑到其使用文件名是如此之多，所以提供了通配符，可以使用模式，来快速查找符合条件的文件集合  

\* 任意字符  
？ 单个字符  
\[characters] Matches any character that is a member of the set characters  
\[\!characters] 非  

\* All files  
g\* g 开头的 file  
b\*.txt b 开头的，后面任意多个字符的，txt 文件  
Data??? Data 后面三个字符的  
\[abc]\* Any file beginning with either 'a','b' or 'c'  
BACKUP.\[0-9]\[0-9]\[0-9] BACKUP 开头，后面 followed by exactly three numerals  

通配符非常重要，是因为 they are so frequently used on the command line   

ls /bin/c* 所有以 c 开头的文件  

cp、mv、mkdir、rm、ln 这些命令都是 Linux 中最常用的命令  

mkdir dir1  
mkdir dir1 dir2 dir3  
<br>
cp 源文件 目标文件夹  
cp file1 file2; file2 不存在就创建，file2 存在就覆盖  
cp -i file1 file2; 如果 file2 存在，会有提示信息，询问是否覆盖  
cp file1 file2 dir1  
cp dir1/* dir2; 复制 dir1 下的所有文件到 dir2  
<br>  
mv 移动或重命名，取决于应用场景，不管是哪一种操作，执行命令以后源文件都不再存在  
mv file1 file2; 如果 file2 存在，就把 file1 的内容 overwritten 到 file2 中，如果 file2 不存在，就重命名  
mv -i file1 file2; 如果 file2 存在，就询问  
mv file1 file2 dir1  
mv dir1 dir2; 如果 dir2 不存在，创建 dir2，并且把 dir1 的 content move 到 dir2 中，并且删除 dir1；如果 dir2 存在，就把 dir1 和 dir1 所包含的内容移动到 dir2 中(也就是 dir1 或成为 dir2 的子文件夹)  
<br>
rm remove  
rm -r file1 dir1; remove file1 dir1 的内容，和 dir1 文件夹(可以用 rm -v -r file1 dir1 命令执行，可以看到其实是三条命令：file1、dir1 的内容、dir1)  
rm -rf; 慎用，递归删除且不提示  
慎用 rm 和通配符的组合，很可能会删掉不该删的内容，解决办法是先 ls 通配符，看一看内容，再把 ls 替换成 rm  
<br>  
要重视 link，因为 you will encounter them from time to time  
ln file link; 硬链接  
ln -s item link 软链接  
item 可以是 file 也可以是 directory  
symbolic link 很像 Windows 的快捷方式  
如果删除链接，文件没有变化；如果删除文件，链接还会 exist，但是 point to nothing，也就是 link broken 了，会显示红色  

案例：  
cp /etc/passwd .; copy /etc/passwd 到当前目录下  
mv passwd fun; passwd 重命名为 fun  



\-i \-\-interactive 会询问  
\-r \-\-recursive  
\-f \-\-force  
\-v \-\-verbose; 会显示操作的具体内容，可以看到 what it does，比如：removed 'dir1/dir1/a.txt'  






