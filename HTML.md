
容器元素一般叫 wrapper   

## 实践笔记   

#### [a](https://www.w3school.com.cn/tags/tag_a.asp)  

```html
<a href="http://tools.mxspider.top/cyberin/updata_to_cyberin/" target="_blank">>跳转到加载配置页面</a>
```

在新窗口打开，target="\_blank"    


#### [hidden 属性](https://www.w3school.com.cn/tags/att_global_hidden.asp)    

不显示元素   

```html
<p hidden>这个段落应该被隐藏。</p>
```

取消时间提示：autocomplete="off"       


# 代码   

### textarea   

```html
<form method="post" id="search_urls_form" enctype="multipart/form-data" action="/cyberin/save_new_year_fixed_word/" >
    <div>
        <label>长城日报3导出url查询配置(每行一条)</label><br/>
        <textarea id='search_urls' name='search_urls' rows="10" cols="80"></textarea><br/>  # 指定宽高   
        <button id="btn_save" type="button" onclick="save_fixed()">查询</button>
    </div>
</form>

function save_fixed(){
    $("#search_urls_form").submit();
}
```


## 原来笔记   

### 工作的时候，没事就去审查别人的网站，然后把样式 copy 过来就行了  

HTML 非常简单，很容易学会，HTML 不是一种编程语言，而是一种标记语言  

HTML HyperText Markup Language, 超文本标记语言 超文本是说不只是文本，还包括图片、视频等等  

引入 CSS 和 JavaScript 就是 import，按照路径引入  

属性一般使用双引号  

属性主要是 class 和 id  


#### 元数据

在最后的结果中，不显示标签，只显示内容  

\<head> 元素包含了所有的头部标签元素。在 \<head>元素中你可以插入脚本（scripts）, 样式文件（CSS），及各种 meta 信息。  

可以添加在头部区域的元素标签为: \<title>, \<style>, \<meta>, \<link>, \<script>, \<noscript> 和 \<base>。  

title 是标题，就是标签页上面的文字，便于搜索引擎查找  

base 是 base URL，有了这个以后后面写连接就可以只写相对网址就可以了  
 
\<base> 标签描述了基本的链接地址/链接目标，该标签作为HTML文档中所有的链接标签的默认链接:`<base href="http://www.runoob.com/images/" target="_blank">`   

meta 元数据，增加说明信息，比如作者、简介等等  

`<meta charset="utf-8">` 声明编码，否则会出现乱码  

可以通过 3 中方式使用 CSS 样式  

内联样式- 在HTML元素中使用"style" 属性：`<p style="color:blue;margin-left:20px;">这是一个段落。</p>`  

内部样式表 -在HTML文档头部 \<head> 区域使用 \<style>，可以直接写 CSS 样式   

外部引用 - 使用外部 CSS 文件，\<link> 标签定义了文档与外部资源之间的关系。\<link> 标签通常用于链接到样式表: `<link rel="stylesheet" type="text/css" href="mystyle.css">` rel 就是 relation，href 就是地址；    

\<script> 标签用于定义客户端脚本，比如 JavaScript。\<script> 元素既可包含脚本语句，也可通过 src 属性指向外部脚本文件。

比如：  
```js
<script>
document.write("Hello World!");
</script>
```

#### 标记文字  

a 链接，href Hypertext Reference 指定链接的地址。target=\_blank 是在新窗口打开，target=\_self 是在当前页面打开   

`<a href="url">链接文本</a>`，href 的地址应该始终以 / 结尾    

有了 base，后面就可以用相对 URL  

href=\# 相对坐标，锚点，可以实现在页面内部跳转，比如跳转到某一个标题部分  

b 粗体 bold，em 斜体强调，i 也是斜体，和 em 很像，用于术语  

换行 br，就是 break  

空格 &nbsp;  

span 就是一段跨区很短的内容  


#### 组织段落  

HTML 区块元素（(block-level），块级元素在浏览器显示时，通常会以新行来开始（和结束）。实例: \<h1>, \<p>, \<ul>, \<table>  

div 区块，主要用在页面总体布局上，比如 header、footer、content、left、right 等等，其实看不到任何效果，主要是起到容器的作用  

HTML 内联元素（inline），内联元素在显示时通常不会以新行开始。实例: \<b>, \<td>, \<a>, \<img>  

\<span> 元素是内联元素，\<span> 元素也没有特定的含义。用作文本的容器  

HTML 通过 \<div> 和 \<span> 将元素组合起来。  
 
pre 预先编排好的格式，就是原来的格式保留下来，经常和 code 在一起，引用代码  

hr 水平线  

li 是 list，无序列表就是前面一个黑点 ul，有序列表就是前面是序号 ol，可能是 order list，自定义列表 dl，应该是 define list     

无序列表使用 \<ul> 标签：  
```html
<ul>
<li>Coffee</li>
<li>Milk</li>
</ul>
```

`<!-- 这是一个注释 -->`  


#### 文档划分  

h1-h6 标题 Header  

section 章节，没有什么效果，主要是人读的时候区分章节  

header 和 footer 也是没有什么效果，主要是语义上的区分  

nav 导航 navigation  

article 文章  

aside 边栏  


#### 表格  

table 表格、tr 一行 table row，td 表格数据 table data，th 表头 table header，有个黑体的样式  

```html
<table border="1">
    <tr>
        <th>Header 1</th>
        <th>Header 2</th>
    </tr>
 
    <tr>
        <td>row 1, cell 1</td>
        <td>row 1, cell 2</td>
    </tr>
 
    <tr>
        <td>row 2, cell 1</td>
        <td>row 2, cell 2</td>
    </tr>
</table>
```

rowspan、colspan 跨行跨列，效果就是 Excel 里的合并单元格  

caption 标题  


#### 表单

表单元素是允许用户在表单中输入内容，比如：文本域(textarea)、下拉列表、单选框(radio-buttons)、复选框(checkboxes)等等。表单使用表单标签 \<form> 来设置。  

表单 form，method 有 post 和 get  

GET 会把参数显示在地址栏中  

action 是表单内容提交的地址，把数据提交给这个 url，这个 url 会去匹配 urls.py 里的路由，然后根据路由找到视图函数，在视图函数中拿到数据，执行跳转，也是在视图函数中执行的。    

多数情况下被用到的表单标签是输入标签（\<input>）。输入类型是由类型属性（type）定义的。

用户名 type="text"，密码 type=password，就显示星号或者小圆点，单选按钮：type="radio"，复选框：type="checkbox"  

提交按钮(Submit Button)，\<input type="submit"> 定义了提交按钮。当用户单击确认按钮时，表单的内容会被传送到另一个文件。表单的 action 属性定义了目的文件的文件名。由动作属性定义的这个文件通常会对接收到的输入数据进行相关的处理。  

enctype 字符编码  

input 属性，autofocus，自动聚焦，就是打开网页鼠标自动到 input 上，disabled 禁用，灰色  

button 设置 type='submit' 提交，type='reset' 就是清空，value='按钮上显示的文字'  


#### 表单 input  

表单 input 的用法特别多  

type='text' 代表输入文本，name 代表名称，服务器端要通过 name 获得值  

placeholder 就是提示用户输入什么  

size 是显示长度，就是框的长度  

maxlength 就是最大输入长度  

required='True' 必填  

上传文件，要设置 enctype='multipart/from-data'  

textarea 文本框，比如留言板，评论区等等   

不显示历史记录：autocomplete="off"   


#### HTML5 语义元素  

语义= 意义，语义元素 = 有意义的元素  

一个语义元素能够清楚的描述其意义给浏览器和开发者。  

无语义 元素实例: \<div> 和 \<span> - 无需考虑内容。  

语义元素实例: \<form>, \<table>, \<img> - 清楚的定义了它的内容。  

\<section> 元素，\<section> 标签定义文档中的节（section、区段）。比如章节、页眉、页脚或文档中的其他部分。

\<article> 元素  

\<nav> 元素，\<nav> 标签定义导航链接的部分。  

\<aside> 元素，\<aside> 标签定义页面主区域内容之外的内容（比如侧边栏）。  

\<header> 元素  

\<footer> 元素  


#### 嵌入内容  

img 就可以嵌入图片，src 写文件路径加文件名。`<img src="/images/logo.png" width="258" height="39" />` 可以通过属性指定图片尺寸  

要在页面上显示图像，你需要使用源属性（src）。src 指 "source"。源属性的值是图像的 URL 地址。  

alt 属性用来为图像定义一串预备的可替换的文本。替换文本属性的值是用户定义的。

`<img src="boat.gif" alt="Big Boat">`在浏览器无法载入图像时，浏览器将显示这个替代性的文本而不是图像。为页面上的图像都加上替换文本属性是个好习惯。  

embed 和 object 嵌入内容，视频等等  

progress 进度条  

Canvas 就是画布的意思  

RGBA 的意思是（Red-Green-Blue-Alpha）它是在 RGB 上扩展包括了 “alpha” 通道，运行对颜色值设置透明度。  


#### [绘制图形 canvas](https://www.w3school.com.cn/html/html5_canvas.asp)   




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


[HTML 速查列表](HTML 速查列表)  

#### [HTML 单词简写及全称](https://www.runoob.com/html/html-tag-name.html)  

alt alter 替用(一般是图片显示不出的提示)  
br	Break	换行  
div	Division	分隔  
dl	Definition List	定义列表  
em	Emphasized	加重（文本）  
hr	Horizontal Rule	水平尺  
href	hypertext reference	超文本引用  
i	Italic	斜体（文本）  
li	List Item	列表项目  
ol	Ordered List	排序列表  
p	Paragraph	段落  
rel	Reload	加载  
span	Span	范围  
src	Source	源文件链接  
td	table data cell	表格中的一个单元格  
th	table header cell	表格中的表头  
tr	table row	表格中的一行  
ul	Unordered List	不排序列表  
var	Variable	变量（文本）  

