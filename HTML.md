
 HTML HyperText Markup Language, 超文本标记语言 超文本是说不只是文本，还包括图片、视频等等  

href 是 Hypertext Reference 的缩写。意思是指定超链接目标的 URL。href 属性的值可以是任何有效文档的相对或绝对 URL，包括片段标识符和 JavaScript 代码段。  

引入 CSS 和 JavaScript 就是 import，按照路径引入  

#### 元数据

在最后的结果中，不显示标签，只显示内容  

head 是头部信息，title 是标题，就是标签页上面的文字，便于搜索引擎查找  

base 是 base URL，有了这个以后后面写连接就可以只写相对网址就可以了  

meta 元数据，增加说明信息，比如作者、简介等等  

style 增加 CSS 样式，rel 就是 relation，href 就是地址；可以通过 link 引入 CSS 样式    

script 写 JavaScript 代码，可以写在 JS 文件中，然后用 script 引用，src 上写 JS 文件名  

#### 标记文字  

a 链接，href 写网址， target=\_blank 是在新窗口打开，target=\_self 是在当前页面打开   

有了 base，后面就可以用相对 URL  

href=\# 相对坐标，锚点，可以实现在页面内部跳转，比如跳转到某一个标题部分  

b 粗体 bold，em 斜体强调，i 也是斜体，和 em 很像，用于术语  

换行 br，就是 break  

span 就是一段跨区很短的内容  

#### 组织段落  

p 段落  

div 区块，主要用在页面布局上，比如 header、footer、left、right 等等，其实看不到任何效果  

pre 预先编排好的格式，就是原来的格式保留下来，经常和 code 在一起，引用代码  

hr 水平线  

li 是 list，无序列表就是前面一个黑点 ul，有序列表就是前面是序号 ol，可能是 order list   

#### 文档划分  

h1-h6 标题 header  

section 章节，没有什么效果，主要是人读的时候区分章节  

header 和 footer 也是没有什么效果，主要是语义上的区分  

nav 导航 navigation  

article 文章  

aside 边栏  

#### 表格  

table 表格、tr 一行 table row，td 一列，th 表头 table header，有个黑体的样式  

rowspan、colspan 跨行跨列，效果就是 Excel 里的合并单元格  

caption 标题  

#### 表单

表单 form，method 有 post 和 get，action 会跳转到指定的页面  

用户名 type=text  
密码 type=password，就显示星号或者小圆点  

enctype 字符编码  

input 属性，autofocus，自动聚焦，就是打开网页鼠标自动到 input 上，disabled 禁用，灰色  

button 设置 type='submit' 提交，type='reset' 就是清空  

#### 表单 input  

表单 input 的用法特别多  

type='text' 代表输入文本，name 代表名称，服务器端要通过 name 获得值  

placeholder 就是提示用户输入什么  

size 是显示长度，就是框的长度  

maxlength 就是最大输入长度  

required='True' 必填  

上传文件，要设置 enctype='multipart/from-data'  

textarea 富文本框，比如留言板，评论区等等  

#### 嵌入内容  

img 就可以嵌入图片，src 写文件路径加文件名  

embed 和 object 嵌入内容，视频等等  

progress 进步条  

Canvas 就是画布的意思  

#### 多媒体  

video 视频，src 写文件名，poster 封面，autoplay 自动播放，controls 底下出现进度条暂停播放按钮音量全屏，source 格式  

audio 音频，和 video 差不多  

可以通过 DOM 操作多媒体  

#### web 存储  

localstorage 本地存储，有点儿像 cookie，关闭了以后还会存在   

sessionstorage 存储 session，关闭以后存储就消失了    

SQL storage 就是用数据库来存储  


select 下拉菜单  
```html
<select>  
  <option>北京市</option>
  <option>广州市</option>
  <option>兰州市</option>
</select>  
```
