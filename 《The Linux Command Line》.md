
一次整理，终生使用  


## 1-What Is the Shell  

The shell is a program that takes keyboard commands and passes them to the operating system to carry out.  


## 2-Navigation  

**pwd: print working directory  
cd:change directory  
ls: list short  
ll: list long**  

ls 和 ll 实际上并不是各自这两个单词的缩写，不过自己可以这么记  

目录文件按字母排序  

绝对路径和相对路径，哪一个 typing 最少就用哪一个  

`cd` 可以直接跳转到该用户的 home 文件下  
`cd -` 跳转到 previous working directory  

以 . 开头的文件，用 ls 命令看不到  
文件命名不要用空格，用下划线替代  



## 3-Exploring the System  

**ls: list directory contents  
file: determine file type  
less: view file contents**  

ls 可能是 Linux 上用得最多的命令  
`ls 当前目录下文件`  
`ls /usr`  
`ls /usr /tmp` 可以展示两个文件夹下的 content  

更常见的命令模式：  
command -options arguments  
options 会 modify command 的行为，经常会带有一个 -   

`ls -lh` h 是 human readable 的意思，会把大小转化成 K、M  

ll 可以看权限  
第一个 d 代表文件夹 directory，- 代表单个文件，l 代表软链接  

file 文件名 查看 file 类型  

`less /etc/passwd` 查看内容；查看的时候 h 查看其它命令; q 退出   

这一章有文件目录，和目录作用表格  


## 4-Manipulating Files and Directories  
**cp: copy files and directories  
mv: move/rename files and directories  
mkdir: create directories  
rm: remove files and directories  
ln: create hard and symbolic links**  

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

`ls /bin/c*` 所有以 c 开头的文件  

cp、mv、mkdir、rm、ln 这些命令都是 Linux 中最常用的命令  

mkdir: create directories  
`mkdir dir1`  
`mkdir dir1 dir2 dir3`  
<br>
cp: copy files and directories  
cp 源文件 目的地  
`cp file1 file2` file2 不存在就创建，file2 存在就覆盖  
`cp -i file1 file2` 如果 file2 存在，会有提示信息，询问是否覆盖  
`cp file1 file2 dir1`  
`cp dir1/* dir2` 复制 dir1 下的所有文件到 dir2
<br>
mv: move and rename files  
mv 移动或重命名，取决于应用场景，不管是哪一种操作，执行命令以后源文件都不再存在  
`mv file1 file2` 如果 file2 存在，就把 file1 的内容 overwritten 到 file2 中，如果 file2 不存在，就重命名  
`mv -i file1 file2` 如果 file2 存在，就询问  
`mv file1 file2 dir1`  
`mv dir1 dir2` 如果 dir2 不存在，创建 dir2，并且把 dir1 的 content move 到 dir2 中，并且删除 dir1；如果 dir2 存在，就把 dir1 和 dir1 所包含的内容移动到 dir2 中(也就是 dir1 成为 dir2 的子文件夹)  
<br>
rm: remove files and directories  
`rm -r file1 dir1` remove file1 dir1 的内容，和 dir1 文件夹(可以用 `rm -v -r file1 dir1` 命令执行，可以看到其实是三条命令：file1、dir1 的内容、dir1)  
`rm -rf` 慎用，递归删除且不提示  
慎用 rm 和通配符的组合，很可能会删掉不该删的内容，解决办法是先 ls 通配符，看一看内容，再把 ls 替换成 rm  
<br>
ln: create links  
要重视 link，因为 you will encounter them from time to time  
`ln file link` 硬链接  
`ln -s item link` 软链接 `ln -s python3.6.7 python`  
item 可以是 file 也可以是 directory  
symbolic link 很像 Windows 的快捷方式  
如果删除链接，文件没有变化；如果删除文件，链接还会 exist，但是 point to nothing，也就是 link broken 了，会显示红色  

\-i \-\-interactive 会询问  
\-r \-\-recursive; 递归操作  
\-f \-\-force  
\-v \-\-verbose; 会显示操作的具体内容，可以看到 what it does，比如：removed 'dir1/dir1/a.txt'  



案例：  
`mkdir playground`  
`cd playground`  
`mkdir dir1 dir2`  
`cp -v /etc/passwd .` copy /etc/passwd 到当前目录下，\-v 查看做了什么  
`cp -i /etc/passwd .` 再次复制，就会提示：cp: overwrite './passwd'?  
`mv passwd fun` passwd 重命名为 fun  
`mv fun dir1` fun 移动到 dir1 中  
`mv dir1/fun dir2` fun 文件从 dir1 中移动到 dir2 中  
`mv dir2/fun .`  
`mv fun dir1`  
`mv dir1 dir2` dir1 会成为 dir2 的子文件夹，里面有 fun 文件  

创建硬链接  
`ln fun fun-hard`  
`ln fun dir1/fun-hard`  
`ln fun dir2/fun-hard`  
使用 `ls -l` 命令可以看到在 fun 和 fun-hard 前面都有一个 4，代表这个文件有 4 个 hard-link，file 至少有一个 hard link，因为 file 的 name is created by a link  
当我们 thinking about hard link 的时候，可以想象文件有两部分，content 和 name，hard link 是不同的 name refer to 相同的 data  
可以使用 `ls -li` 命令，查看 inode number，就可以看到 inode number 相同，说明 they are the same file  
<br>
创建软链接  
symbolic link 克服了 hard link 的两个 disadvantages：不能 span physical devices；不能 reference directories  

symbolic links are a special file that contains a text pointer to the target file or directory  

`ln -s fun fun-sym`  
`ln -s ../fun dir1/fun-sym`  
`ln -s ../fun dir2/fun-sym`  

可以使用绝对路径，也可以使用相对路径；推荐使用相对路径，因为使用相对路径，文件移动或改名以后，不会影响 link 的有效性  

`ln -s dir1 dir1-sym` 可以创建文件夹的软链接  

`rm fun-hard`  
`rm -i fun`  
删除 fun 以后，link 变成红色，link broken  
`rm fun-sym`  
关于 symbolic link，most file operations 作用在 link 的 target 上，而不是作用在 link itself 上，rm 命令是个例外，rm 作用在 link 上  
`rm -r playground`  

It is important to get a good understanding of basic file manipulation commands and wildcards  


## 5-Working with Commands  
**type: indicate how a command name is interpreted  
which: display which executable program will be executed  
help: get help for shell builins  
man: display a command's manual page  
whatis: display one-line manual page descriptions  
alias: create an alias for a command**  


command can be four different things:  
1、An executable program  
2、A command built into the shell itself  
3、A shell function  
4、An alias  

It is often useful to know exactly which of the four kinds of commands is being used  

type: display a command's type  
可以使用 type 命令查看  
`type type`  
`type ls`  
`type cp`  


which: display an executable's location  
Sometimes there is more than one version of an executable program installed on a system, 使用 which 命令可以查看 exect location of a given executable  
`which ls`  
which 只能作用于 executable programs，not builtins nor alias  


help: get help for shell builtins  
square brackets indicate optional items, | 代表或的意思  

\-\-help: display Usage information  
`mkdir --help`  
try 这个 command anyway，总会得到有用的信息  

man: display a program's munual page  
`man ls`  
man 用 less 命令来展示 manual page，less 的所有命令都可以在展示中使用  
manual 一般很难读懂，不是 tutorial  

whatis: display one-line manual page discriptions  
`whatis ls`  

我们 install 的 software 的 documentation file 一般都放在 /usr/share/doc 文件夹下  

creating our own commands with alias  
可以执行多个命令，用分号隔开  
`command1; command2; command3...`  
`cd /usr; ls; cd -`  
`alias foo='cd /usr; ls; cd -'`  
可以 use it anywhere  
`foo`  
`type foo`  
`unalias foo` remove alias  

使用 alias 命令，不带参数，就可以查看所有的 alias  

## 6-Redirection  
In this lession we are going to unleash what may be the coolest feature of command line.It's called I/O rediction, I/O 代表 input/output  

**cat: concatenate files  
sort: sort lines of text  
uniq: report or omit repeated lines  
grep: print lines matching a patten; Global Regular Expression Print 全局正则表达式搜索  
wc: print newline, word, and byte counts for each file  
head: output the first part of a file  
tail: output the last part of a file  
tee: read from standard input and write to satandard output and files**  

output 一般是两类：运行结果 standard output(stdout)，或者是 status and error(stderr)    

stdout 和 stderr linked to the screen, and not saved into disk file, stdin attached to the keyboard  

I/O rediction 可以让我们 redefine where standard output goes, 可以 redirect standard output to another file instead of the screen，我们可以使用 \> redirection operator followed by the name of the file.  

`history > history_command.txt`  
`ls -l /usr/bin > ls-output.txt`  
`less ls-output.txt`  

`> ls-output.txt` 这条命令可以清空文件，如果文件不存在则是创建新的文件  

\>\> append
`ls -l /usr/bin >> ls-output.txt`  

要 redirect error，我们必须要使用文件描述符(file descriptor)  
standard input, output 和 error 分别对应 0, 1, 2  
`ls -l /bin/usr 2> ls-error.txt`  

Redirecting standard output and standard error to one file  
有两种办法：  
1、比较 traditional 的方法，在 old version shell 上运行，`ls -l /bin/usr > ls-output.txt 2\>&1`  
这条命令里有两个 redirections，第一个是 redirect standard output to the file ls-output.txt，然后是 redirect standard error to standard output  
这条命令中两个 redirection 的顺序是重要的，调换顺序 error 会在屏幕显示  

2、新的方法：`ls -l /bin/usr &> ls-output.txt`  
&\> redirect both standard output and standard error  
同样也可以 append，`ls -l /bin/usr/ &>> ls-output.txt`  

Somethimes silence is golden, and we don't want output from a command, we just want to throw it away, 可以 redirect output to a special file called "/dev/null", this file is a system device often referred to as a bit bucket, which accepts input and does noting with it.  

`ls -l /bin/usr 2> /dev/null`  

cat: concatenate files  
cat 会显示完整的文件内容  
`cat ls-output.txt`  
cat 还可以用来 join files together  
如果下载的文件被 split into multiple parts 了，比如 movie.mpeg.001 movie.mpeg.002 ... movie.mpeg.099, 就可以使用命令 `cat movie.mpeg.0* > movie.mpeg` 将文件 join back together  

输入 `cat` 命令，且不带参数，就可以接受输入，按 Ctrl + d 结束  
`cat > lazy_dog.txt` 然后输入的内容就会被写入 lazy_dog.txt 文件中  
输入完成以后，可以使用 `cat lazy_dog.txt` 来查看写入的内容  

pipeline  
管道是将第一个命令的输出传给第二个命令  
`ls -l /usr/bin | less`  
这个命令非常有用！我们使用这个命令可以非常方便地 examine the output of any command that produces standard output.  

\> 和 | 的区别：\> 后面接的是文件，| 后面接的是命令  
command1 > file1  
command1 | command2  

管道命令经常被用于 complex operations on data, 可以组合多个命令，经常被称为 filters  

`ls /bin /usr/bin | sort | less`  

uniq: report or omit repeated lines  
uniq 经常和 sort 一起使用，可以去重  

`ls /bin /usr/bin | sort | uniq | less`  
如果想看重复项，可以使用命令：`ls /bin /usr/bin | sort | uniq -d | less`  

wc(word count): print line, word, and byte counts  

`wc ls-output.txt`  
会打印三个数字，分别代表：lines, words and bytes.  

`ls /bin /usr/bin | sort | uniq | wc -l`  
\-l 参数，只 print lines  

grep: print lines matching a pattern  
grep is a powerful program used to find text patterns within files  
grep pattern \[file...]  
when grep encounters a "pattern" in the file, it prints out the lines containing it.  
`ls /bin /usr/bin | sort | uniq | grep zip`  
grep 对大小写敏感，可以使用参数 \-i 来 ignore  
参数 \-v invert 打印 those lines that do not match the pattern.  

head/tail: print first/last part of files  
有时候我们并不需要查看全部内容，就可以使用 head 和 tail, 默认显示 10 行，可以用 \-n 改变显示行数  
`head -n 5 ls-output.txt`  
`tail ls-output.txt`  

也可以使用 pipeline：`ls /usr/bin | tail -n 5`  

tail 命令可以 view files in real time，可以用来查看 log  
`tail -f /var/log/syslog`  
\-f follow 当内容更新的时候，会 append 在后面  

tee: read from stdin and output to stdout and files  
tee 命令 reads standard input and copies it to both standard out and to one or more files  
`ls /usr/bin | tee ls.txt | grep zip`  
在 grep 之前，会先写入 ls.txt  

As we gain Linux experience, we will see that the redirection feature of the command line is extemely useful for solving specialized problems.  

Windows 像是买的别人做好的玩具，你想增加一些简单的功能，他们会说市场需求少，他们不会去做；而 Linux 则像是一个工具材料店，it's just a huge collection of parts. There's a lot of steel struts, screws, nuts, gears, pulleys, motors, and a few suggestions on what to build. 你照着 suggestions 做了一会以后，you discover that you have your own ideas of what to make. You don't ever have to go back to the store, as you already have everything you need.  

## 7-Seeing the World as the Shell Sees It  

**echo: display a line of text**  
echo is a shell builtin that performs a very simple task, it prints its text arguments on standards output.  

expansion

` echo this is a test`  
`echo *`  
会 print current directory 下的所有的文件名，当按 Enter 键的时候，shell 会在 echo 命令执行前，先 expand 通配符 \*, 所以 echo 看不到 \*  

`echo l*` 显示 l 开头的文件名  
`echo *t`  
`echo [[:lower:]]*`  
`echo /usr/*/share`  

Tilde Expansion  
`echo ~` 会显示 the name of the home directory of the named user  

Arithmetic Expansion  

`echo $((2 + 2))`  
$((expression))  

% remainder 余数  

Brace Expansion  
`echo Front-{A,B,C}-Back`  
`echo Number_{1..5}`  
`echo {01..15}`  
`echo {001..15}`  
`echo {Z..A}`  
`echo a{A{1,2},B{3,4}}B`  

So what is this good for? The most common application is to make lists of files or directories to be created.  

`mkdir Photos`  
`cd Photos`  
`mkdir {2007..2009}-{01..12}`  
`ls`  

Parameter Expansion  
$ variables  

`echo $USER`  
`printenv | less`  

Command Substitution  
`echo $(ls)`  
`ls -l $(which cp)`  
`file $(ls -d /usr/bin* | grep zip)`  
这里 pipeline 的结果成为了 file 的参数  

Quoting  
`echo this is a  有空格  test`  
`echo The total is $100.00`  
第一个例子，会自动把空格取消，第二个例子会把 1 当做变量  

Double Quotes  
`touch "two words.txt"`  
`ls -l two words.txt`  
这里会把 two 和 words.txt 当做两个文件名  
正确的写法是：`ls -l "two words.txt"`  
`move "two words.txt" two_words.txt`  
double quotes 不影响 parameter expansion, arithmetic expansion, and command substitution  

`echo "$USER $((2+2)) $(cal)"`  

`echo "this is a 有空格 test"`  
`echo $(cal)` 没有换行  
`echo "$(cal)"`  

Single Quotes  
single quotes 会 supress all expansions  
`echo text ~/*.txt {a,b} $(echo foo) $((2+2)) $USER`  
`echo "text ~/*.txt {a,b} $(echo foo) $((2+2)) $USER"`  
`echo 'text ~/*.txt {a,b} $(echo foo) $((2+2)) $USER'`  

Escaping Characters  
`echo "The balance for user $USER is: \$5.00"`  
可以使用转义字符来消除 the special meaning of a character  
`mv bad\&filename good_filename`  

expansions 和 quoting 在 shell 中用得非常多，如果对 expansion 没有一个 good understanding，学 shell 的时候回经常感到 confusing  


## 8-Advanced Keyboard Tricks  

One of the most cherished goals of the command line is laziness; doing the most work with the fewest number of keystrokes. Another goal is never having to lift out fingers from keyboard and reach for the mouse.  

**clear: clear the screen  
history: display the contents of the history list**  

Cursor Movement  
`ctrl-a` 移动光标到行首  
`Ctrl-e` 移动光标当行尾(e 代表 end)  
`Ctrl-f` 右移一个字符(f forward)  
`Ctrl-b` 左移一个字符(b backward)  
`Alt-f` 右移一个单词  
`Alt-b` 左移一个单词  
`Ctrl-l` 清屏  

Modifying Text  
`Ctrl-d` 删除光标处的字符(d delete)  
`Ctrl-t` Transpose the character with the one preceding it.调换和前一个字符的顺序  
`Alt-t` 调换单词  
`Alt-l` 单词变小写(lower)  
`Alt-u` 单词变大写(upper)  

Cutting and Pasting(Killing and Yanking) Text  
`Ctrl-k` Kill 到行尾  
`Ctrl-u` Kill 到行首  
`Alt-d` Kill 到词尾  
`Alt-Backspace` Kill 到词首，如果 cursor 在词首，就 kill 前一个单词  
`Ctrl-y` Yank 缓存中的内容在 cursor 所处的位置  

Completion  
Tab 键自动补全  

Seaching History  
`history | less`  
`history | sort -r | less` r reverse  
`history | grep /usr/bin`  

可以使用 !数字 来执行这一条 history 命令，这就是 history expansion  

`Ctrl-r` 然后输入内容就可以逆向搜索历史命令，找到按 Enter 就可以执行，查找下一条接着按 `Ctrl-r`，`Ctrl-j` copy 命令，`Ctrl-c` 退出搜索  


## 9-Permissions  

Unix 系统不但是 multitasking，而且还是 multi-user system.  所以就有了权限系统，保证 the actions of one user could not be allowed to crash the computer, nor could one user interfere with the files belonging to another user.(和现实社会是一样的，你不能不经别人同意，随便动别人的东西)  

**id: display user identity  
chmod: change a file's mode  
umask: set the default file permissions  
su: run a shell as another user  
sudo: execute a command as another user  
chown: change a file's owner  
chgrp: change a file's group ownership  
passwd: change a user's password**  

Owners, Group Members, and Everybody Else  
`id`  
uid: user id  
gid: group id  

user accounts 存放在 /etc/passwd 中，groups 存放在 /etc/group 里  

Reading, Writing, and Executing  
权限指的就是 reading access, write access, and execution access  
`> foo.txt` 创建文件  
`ll foo.txt`  
前面的 10 个 characters are file attributes. 第一个是 file type  
\- A regular file  
d A directory  
l A symbolic. 当文件类型是 symbolic 的时候，file attributes 都是 "rwxrwxrwx", 这个是没什么意义的，重要的还是 real file 的权限，那个权限才是真实的权限  

后面的 9 个叫做 file mode, represent the read, write and execute permissions for the file's owner, the file's group owner, and everybody else.  

后面有两张表格，详细介绍了各种权限类型和组合的含义  

chmod: change file mode  
只有文件所有者和 superuser 可以 chmod，有两种方式：octal number(8 进制) representation, or symbolic representation.  

<table class="table">
  <thead>
    <tr>
      <th>Octal</th>
      <th>Binary</th>
      <th>File Mode</th>
    </tr>
  </thead>
  <tbody>
    <tr>
      <td>0</td>
      <td>000</td>
      <td>---</td>
    </tr>
    <tr>
      <td>1</td>
      <td>001</td>
      <td>--x</td>
    </tr>
    <tr>
      <td>2</td>
      <td>010</td>
      <td>-w-</td>
    </tr>
    <tr>
      <td>3</td>
      <td>011</td>
      <td>-wx</td>
    </tr>
    <tr>
      <td>4</td>
      <td>100</td>
      <td>r--</td>
    </tr>
    <tr>
      <td>5</td>
      <td>101</td>
      <td>r-x</td>
    </tr>
    <tr>
      <td>6</td>
      <td>110</td>
      <td>rw-</td>
    </tr>
    <tr>
      <td>7</td>
      <td>111</td>
      <td>rwx</td>
    </tr>
  </tbody>
</table>


`> foo.txt`  
`ls -l foo.txt`  
`chmod 600 foo.txt`  
`ls -l foo.txt`  

r 4  
w 2  
x 1  


