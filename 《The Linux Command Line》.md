
一次整理，终生使用  


### 1-What Is the Shell  

The shell is a program that takes keyboard commands and passes them to the operating system to carry out.  


### 2-Navigation  

pwd: print working directory  
cd:change directory  
ls: list short  
ll: list long  
ls 和 ll 实际上并不是各自这两个单词的缩写，不过自己可以这么记  

目录文件按字母排序  

绝对路径和相对路径，哪一个 typing 最少就用哪一个  

cd 可以直接跳转到该用户的 home 文件下  
cd - 跳转到 previous working directory  

以 . 开头的文件，用 ls 命令看不到  
文件命名不要用空格，用下划线替代  


### 3-Exploring the System  

ls: list directory contents  
file: determine file type  
less: view file contents  

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

less /etc/passwd; 查看内容；查看的时候 h 查看其它命令; q 退出   

这一章有文件目录，和目录作用表格  


### 4-Manipulating Files and Directories  
cp: copy files and directories  
mv: move/rename files and directories  
mkdir: create directories  
rm: remove files and directories  
ln: create hard and symbolic links  

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

mkdir: create directories  
mkdir dir1  
mkdir dir1 dir2 dir3  
<br>
cp: copy files and directories  
cp 源文件 目标文件夹  
cp file1 file2; file2 不存在就创建，file2 存在就覆盖  
cp -i file1 file2; 如果 file2 存在，会有提示信息，询问是否覆盖  
cp file1 file2 dir1  
cp dir1/* dir2; 复制 dir1 下的所有文件到 dir2
<br>
mv: move and rename files  
mv 移动或重命名，取决于应用场景，不管是哪一种操作，执行命令以后源文件都不再存在  
mv file1 file2; 如果 file2 存在，就把 file1 的内容 overwritten 到 file2 中，如果 file2 不存在，就重命名  
mv -i file1 file2; 如果 file2 存在，就询问  
mv file1 file2 dir1  
mv dir1 dir2; 如果 dir2 不存在，创建 dir2，并且把 dir1 的 content move 到 dir2 中，并且删除 dir1；如果 dir2 存在，就把 dir1 和 dir1 所包含的内容移动到 dir2 中(也就是 dir1 或成为 dir2 的子文件夹)  
<br>
rm: remove files and directories  
rm remove  
rm -r file1 dir1; remove file1 dir1 的内容，和 dir1 文件夹(可以用 rm -v -r file1 dir1 命令执行，可以看到其实是三条命令：file1、dir1 的内容、dir1)  
rm -rf; 慎用，递归删除且不提示  
慎用 rm 和通配符的组合，很可能会删掉不该删的内容，解决办法是先 ls 通配符，看一看内容，再把 ls 替换成 rm  
<br>
ln: create links  
要重视 link，因为 you will encounter them from time to time  
ln file link; 硬链接  
ln -s item link 软链接; ln -s python3.6.7 python  
item 可以是 file 也可以是 directory  
symbolic link 很像 Windows 的快捷方式  
如果删除链接，文件没有变化；如果删除文件，链接还会 exist，但是 point to nothing，也就是 link broken 了，会显示红色  

\-i \-\-interactive 会询问  
\-r \-\-recursive; 递归操作  
\-f \-\-force  
\-v \-\-verbose; 会显示操作的具体内容，可以看到 what it does，比如：removed 'dir1/dir1/a.txt'  



案例：  
mkdir playground  
cd playground  
mkdir dir1 dir2  
cp -v /etc/passwd .; copy /etc/passwd 到当前目录下，\-v 查看做了什么  
cp -i /etc/passwd .; 再次复制，就会提示：cp: overwrite './passwd'?  
mv passwd fun; passwd 重命名为 fun  
mv fun dir1; fun 移动到 dir1 中  
mv dir1/fun dir2; fun 文件从 dir1 中移动到 dir2 中  
mv dir2/fun .  
mv fun dir1  
mv dir1 dir2; dir1 会成为 dir2 的子文件夹，里面有 fun 文件  

创建硬链接  
ln fun fun-hard  
ln fun dir1/fun-hard  
ln fun dir2/fun-hard  
使用 ls -l 命令可以看到在 fun 和 fun-hard 前面都有一个 4，代表这个文件有 4 个 hard-link，file 至少有一个 hard link，因为 file 的 name is created by a link  
当我们 thinking about hard link 的时候，可以想象文件有两部分，content 和 name，hard link 是不同的 name refer to 相同的 data  
可以使用 ls -li 命令，查看 inode number，就可以看到 inode number 相同，说明 they are the same file  
<br>
创建软链接  
symbolic link 克服了 hard link 的两个 disadvantages：不能 span physical devices；不能 reference directories  

symbolic links are a special file that contains a text pointer to the target file or directory  

ln -s fun fun-sym  
ln -s ../fun dir1/fun-sym  
ln -s ../fun dir2/fun-sym  

可以使用绝对路径，也可以使用相对路径；推荐使用相对路径，因为使用相对路径，文件移动或改名以后，不会影响 link 的有效性  

ln -s dir1 dir1-sym; 可以创建文件夹的软链接  

rm fun-hard  
rm -i fun  
删除 fun 以后，link 变成红色，link broken  
rm fun-sym  
关于 symbolic link，most file operations 作用在 link 的 target 上，而不是作用在 link itself 上，rm 命令是个例外，rm 作用在 link 上  
rm -r playground  

It is important to get a good understanding of basic file manipulation commands and wildcards  


### 5-Working with Commands  
type: indicate how a command name is interpreted  
which: display which executable program will be executed  
help: get help for shell builins  
man: display a command's manual page  
info: display a command's info entry  
whatis: display one-line manual page descriptions  
alias: create an alias for a command  


command can be four different things:  
1、An executable program  
2、A command built into the shell itself  
3、A shell function  
4、An alias  

It is often useful to know exactly which of the four kinds of commands is being used  

type: display a command's type  
可以使用 type 命令查看  
type type  
type ls  
type cp  


which: display an executable's location  
Sometimes there is more than one version of an executable program installed on a system, 使用 which 命令可以查看 exect location of a given executable  
which ls  
which 只能作用于 executable programs，not builtins nor alias  


help: get help for shell builtins  
square brackets indicate optional items, | 代表或的意思  

\-\-help: display Usage information  
mkdir \-\-help  
try 这个 command anyway，总会得到有用的信息  

man: display a program's munual page  
man ls  
man 用 less 命令来展示 manual page，less 的所有命令都可以在展示中使用  
manual 一般很难读懂，不是 tutorial  

whatis: display one-line manual page discriptions  
whatis ls  

info: display a program's info entry  
info coreutils  

我们 install 的 software 的 documentation file 一般都放在 /usr/share/doc 文件夹下  

creating our own commands with alias  
可以执行多个命令，用分号隔开  
command1; command2; command3...  
cd /usr; ls; cd -  
alias foo='cd /usr; ls; cd -'  
可以 use it anywhere  
foo  
type foo  
unalias foo; remove alias  

使用 alias 命令，不带参数，就可以查看所有的 alias  

### 6-Redirection  





