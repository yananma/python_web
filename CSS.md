
1. 取 bootstrap 上去复制代码  
2. 在浏览器中，复制 css 样式  


#### CSS 基础  

CSS 层叠样式表 Cascading Style Sheets   

定义了如何显示 HTML 元素，CSS 做到了样式和内容的分离  

CSS 主要由两个部分构成：**选择器，以及一条或多条声明**，每条属性由一个属性和一个值构成  

\h1(选择器)\{color:red(这两个是一条声明，color 是属性，red 是值);font-size:14px;}  

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
