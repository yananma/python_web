
#### CSS 基础  

CSS 定义了如何显示 HTML 的内容，做到了样式和内容的分离  

CSS 主要由两个部分构成：选择器，以及一条或多条声明，每条属性由一个属性和一个值构成  

h1(选择器){color:red(正两个是一条声明，color 是属性，red 是值);font-size:14px;}  

在 HTML 中使用 CSS 有 3 种方式，一种是内联样式，就是写到标签里，style=''，第二种是内部样式，写到 HTML 文件中，还有外部样式，在 HTML 中添加 link，其中 rel='stylesheet', href='style.css'  

#### CSS 选择器

通用选择器，就是选择文件所有的内容，用 \*  

类型选择器，比如 a 标签，li 等等  

类选择器，用 class 选择，用的符号是一个点 .  

id 选择器，用的是 id 属性，符号是 \#  

属性选择器，根据属性选择元素，符号是 []  

分组选择器  

包含选择器  

子元素选择器  

:first-line 选择器  

:first-letter 选择器  

:before 和 :after 选择器  

#### CSS 选择器-伪类  

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

#### CSS 属性和属性值  

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


颜色属性值  

长度单位，绝对长度单位(in, cm, nn, pt 用得不多)；相对长度单位(px像素, em, ex)  

url、关键字(none， inherit)  

使用边框和背景  

盒子阴影  

盒子模型  

文本样式  
