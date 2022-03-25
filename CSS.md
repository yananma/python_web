
### 1. 去 bootstrap 上复制代码  
### 2. 在浏览器中，复制 css 样式  

*** 

## 元素样式   

#### a 链接  

所有的 a 标签全部都取消下划线，全部都修改颜色   
```css 
a {
    text-decoration: none;
}
```


#### [button](https://www.w3school.com.cn/jsref/dom_obj_pushbutton.asp)  

去除 button 边框，展现扁平化效果：`border: none`   

去除 button 边框：`box-shadow: none`   


#### select   

点击后去除黑框：`outline:none`，样式要作用在 select 上，不要作用在父级 wrapper 上，写在 wrapper 上不生效        

不显示外面的 border：`border-style: none`   


## CSS 属性   

### 布局   

#### [对齐](https://www.w3school.com.cn/css/css_align.asp)  

button 右对齐：
```css  
float: right;   
margin-right: 30px;   
```


#### margin   

[margin 文档](https://www.w3school.com.cn/cssref/pr_margin.asp)  

在 CSS 中对元素进行水平居中是非常简单的：如果它是一个行内元素，就对它的父元素应用 text-align: center；如果它是一个块级元素，就对它自身应用 margin: auto。   

div 中包含 span，要让 span 居中，就要在 div 中添加样式：`vertical-align: middle; text-align: center;`  

容器居中：`margin: 0 auto`  

容器居中指定上边距：`margin: 50px auto auto`  

#### [float](https://www.w3school.com.cn/cssref/pr_class_float.asp)   

浮动元素会生成一个块级框，而不论它本身是何种元素。   

假如在一行之上只有极少的空间可供浮动元素，那么这个元素会跳至下一行，这个过程会持续到某一行拥有足够的空间为止。    


#### float left   

父元素：`position: relative`   
所有子元素：`float: left`   


### 样式   

#### [font-size](https://www.w3school.com.cn/cssref/pr_font_font-size.asp)   

如果一个 div 下有很多 a 链接，要改变所有的 a 链接字号，就在 div 里设置 font-size   

可以设置大小   
```css
div.img-area {
    font-size:18px; 
}
```

可以通过形容词指定大小，默认 medium，可选项：xx-small、x-small、small、medium、large、x-large、xx-large   
```css
div.img-area {
    font-size:large; 
}
```

还可以指定百分比    


#### [font-weight](https://www.w3school.com.cn/cssref/pr_font-weight.asp)   

```css 
font-weight:bold;   
```


## 组件代码片段   

#### 搜索框   

要下载 [icon](https://icons.bootcss.com/#install) 文件，不要全部都下载，数量太多了，上传下载到服务器，同步 gitlab 都很不方便，只下载需要的一两张 icon 就可以了    

```css
<div class="input-group input-group" id="list-search-div">
    <label for="list-search"></label>
    <input type="text" name="table_search" class="form-control" id="list-search">
    <div class="input-group-append" id="search-btn">
      <div class="input-group-text"><img src="plugins/bootstrap-icons-1.8.1/search.svg" alt="Bootstrap" id="search-icon"></div>
    </div>
</div>
```


## 样式代码片段  

#### 去除 a 标签默认样式  

```css
a {
    text-decoration: none;
    color: #212529;   /*去看没有 a 标签的时候的文字颜色，然后写在这里*/  
}
```


#### bootstrap 长按 button 样式修改   
```css
.select-button:active {
    background-color: #409EFF!important;
    border-color: #409EFF!important;
    color: #FFF!important;
    box-shadow: none!important;  /*取消 button 阴影*/
}
```

***  

#### CSS 基础  

CSS 层叠样式表 Cascading Style Sheets   

定义了如何显示 HTML 元素，CSS 做到了样式和内容的分离  

CSS 主要由两个部分构成：**选择器，以及一条或多条声明**，每条属性由一个属性和一个值构成  

h1(选择器) {color:red(这两个是一条声明，color 是属性，red 是值);font-size:14px;}  

`p {color:red;text-align:center;}`  

或  
```css
p {
    color:red;
    text-align:center;
}
```

`/*这是个注释*/`  


在 HTML 中使用 CSS 有 3 种方式  
外部样式表(External style sheet)  
内部样式表(Internal style sheet)  
内联样式(Inline style)  

样式多的时候，外部样式表是最理想的选择。页面使用 \<link> 标签链接到样式表。    
```css 
<head>
<link rel="stylesheet" type="text/css" href="mystyle.css">
</head>
```

当单个文档需要特殊的样式时，就应该使用内部样式表。可以使用 \<style> 标签在文档头部定义内部样式表。  
```html
<head>
<style>
hr {color:sienna;}
p {margin-left:20px;}
body {background-image:url("images/back40.gif");}
</style>
</head>
```

由于要将表现和内容混杂在一起，内联样式会损失掉样式表的许多优势。要慎用这种方法，特殊情况下才使用，例如当样式仅需要在一个元素上应用一次时。  

要使用内联样式，需要在相关的标签内使用样式（style）属性。Style 属性可以包含任何 CSS 属性：`<p style="color:sienna;margin-left:20px">这是一个段落。</p>`  

  
#### CSS 选择器

如果要在 HTML 元素中设置 CSS 样式，就需要在元素中设置 "id" 和 "class" 选择器。  

通用选择器，就是选择文件所有的内容，用 \*  

类型选择器，比如 a 标签，li 等等  

id 选择器，用的是 id 属性，以 "\#" 来定义  

样式规则应用于元素属性 id="para1":
```css
#para1 {
    text-align:center;
    color:red;
}
```

类选择器，用 class 选择，用的符号是一个点 .  

`.center {text-align:center;}`  

所有的 p 元素使用 class="center" 让该元素的文本居中：`p.center {text-align:center;}`  



属性选择器，根据属性选择元素，符号是 []  

分组选择器  

包含选择器  

子元素选择器  

:first-line 选择器  

:first-letter 选择器  

:before 和 :after 选择器  

### CSS 选择器-伪类  

根元素选择器(:root)  

子元素选择器(:xx-child)  

索引选择器(nth-child)  

启用禁用某个元素 enabled、disabled  

checked  

valid、invalid  

in-range、out-of-range  

required、optional  

动态选择器：  

:link、:visited、:hover  

:active  

:focus  

### CSS 属性和属性值  

1、尺寸(宽、高、最大宽度、最大高度)  
2、边框(宽度、样式、颜色)  
3、内边距(padding)  
4、外边距(margin)  
5、字体(字体、字号、行距、字距、文字修饰、大小写等)  
6、文本(段落属性、缩进、对齐等)  
7、背景(背景色、背景图片等)  
8、定位(定位方式、定位坐标)  
9、列表(列表样式、图像样式、显示位置)  
10、表格  


#### CSS 背景  

background-color  
background-image  
background-repeat  
background-attachment  
background-position  

`body {background-color:#b0c4de;}`  
`body {background-image:url('paper.gif');}`  
```css
body {
background-image:url('img_tree.png');
background-repeat:no-repeat;
background-position:right top;
}
```

#### CSS 文本格式  

```css 
body {color:red;}
h1 {color:#00ff00;}
h2 {color:rgb(255,0,0);}
```

文本的对齐方式  
```css
h1 {text-align:center;}
p.date {text-align:right;}
p.main {text-align:justify;}
```

文本修饰

text-decoration 属性用来设置或删除文本的装饰。text-decoration 属性主要是用来删除链接的下划线：`a {text-decoration:none;}`    

line-height 设置行高  


#### CSS 字体  

字体样式  
```css
p.normal {font-style:normal;}
p.italic {font-style:italic;}
p.oblique {font-style:oblique;}
```

字体大小  
font-size 属性设置文本的大小。

管理文字的大小，在网页设计中是非常重要的。
```css
h1 {font-size:40px;}
h2 {font-size:30px;}
p {font-size:14px;}
```

#### CSS 链接  

```css
a:link {color:#000000;}      /* 未访问链接*/
a:visited {color:#00FF00;}  /* 已访问链接 */
a:hover {color:#FF00FF;}  /* 鼠标移动到链接上 */
a:active {color:#0000FF;}  /* 鼠标点击时 */
```

text-decoration 属性主要用于删除链接中的下划线：  
```css
a:link {text-decoration:none;}
a:visited {text-decoration:none;}
a:hover {text-decoration:underline;}
a:active {text-decoration:underline;}
```

背景颜色  
```css
a:link {background-color:#B2FF99;}
a:visited {background-color:#FFFF85;}
a:hover {background-color:#FF704D;}
a:active {background-color:#FF704D;}
```







position: fixed 是说固定在窗口的某个地方，是相对于浏览器的定位，位置是 left、right、bottom、top 等所指定的  
  
opacity：透明度  
  
z-index：层级，上下优先级，相当于加了一个 z 轴    

  
颜色属性值  

长度单位，绝对长度单位(in, cm, nn, pt 用得不多)；相对长度单位(px像素, em, ex)  

url、关键字(none， inherit)  

使用边框和背景  

盒子阴影  

盒子模型  

文本样式  



获取颜色：先用 QQ 截图，鼠标悬停会显示 RGB 值，取 https://tool.css-js.com/rgba.php 把 RGB 替换成 16 进制，写到 CSS 里就可以了  


