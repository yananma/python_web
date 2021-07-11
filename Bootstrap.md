
看图复制  

bootstrap 不要记，知道有这么个样式，用的时候去复制就行了  

可以去[菜鸟教程](https://www.runoob.com/bootstrap/bootstrap-forms.html)上去找  

[bootstrap 视频教程](https://www.bilibili.com/video/BV1TU4y1p7zU?p=1)  

### Bootsrap 介绍

自己用 CSS 和 JavaScript 很难写出好看的页面，Bootstrap 就是一个包含了 CSS 和 JS 的类库，别人已经都写好了，非常漂亮，直接拿来用就行了  

工作的时候用百度的 cdn，减轻自己服务器的负担，而且别人的更快  

样式 CSS、组件、JavaScript  

响应式，可以兼容各种分辨率的设备，可以根据移动端自动改变样式，@media，本质上就是 if 判断    

不用记样式，记住网址就行了  

下载包，添加到 static 中，在模板中引入  

最重要的就是 bootstrap.min.css 和 bootstrap.min.js 这两个文件    

下载 jQuery，bootstrap 所有的 js 代码都是基于 jQuery 的，所以必须要下载 jQuery，而且要放到前面  
```js
<link href="css/bootstrap.min.css" rel="stylesheet">
<script src="js/jquery-3.4.1.js"></stript>
<script src="js/bootstrap.min.js"></stript>
```

然后去官网找 CSS 全局样式，改变样式，或选择组件，来添加组件  

复制图标，就打开检查，选  

图标可以去 fontawsome 找  


### 布局容器

布局是网页的骨架，一般都是用 div 完成布局  

为了确保适当的绘制和触屏缩放，需要在 <head> 之中添加 viewport 元数据标签。

```html
<meta name="viewport" content="width=device-width, initial-scale=1">
```

Bootstrap 需要为页面内容和栅格系统包裹一个 .container 容器。我们提供了两个作此用处的类。注意，由于 padding 等属性的原因，这两种 容器类不能互相嵌套。  

\.container 类用于固定宽度并支持响应式布局的容器。  

页面两侧会留有一些空白，默认选项，一般都要加这个选项   
```html
<div class="container">
  ...
</div>
```

.container-fluid 类用于 100% 宽度，占据全部视口（viewport）的容器。没有空白  

### 栅格网格系统  

Bootstrap 提供了一套响应式、移动设备优先的流式栅格系统，随着屏幕或视口（viewport）尺寸的增加，系统会自动分为最多12列。  

“行（row）”必须包含在 .container （固定宽度）或 .container-fluid （100% 宽度）中  

container、row、xs(xsmall phones)、sm(small tables)、md(middle desktops)、lg(larger desktops)  

div 一般自己就占一行  

列组合  

列的总数不超过 12，超过了会换行到下面来  
  
```html
<div class="row">
  <div class="col-md-4">.col-md-4</div>
  <div class="col-md-4">.col-md-4</div>
  <div class="col-md-4">.col-md-4</div>
</div>
```

使用列偏移实现移动效果，总数也不要超过 12，超过 12 就会换行  

使用 .col-md-offset-* 类可以将列向右侧偏移。  
```html
<div class="col-md-4 col-md-offset-4">.col-md-4 .col-md-offset-4</div>  
```

列排序  

通过使用 .col-md-push-* 和 .col-md-pull-* 类就可以很容易的改变列（column）的顺序。  

后面的元素会覆盖前面的元素  
```html
<div class="row">
  <div class="col-md-9 col-md-push-3">.col-md-9 .col-md-push-3</div>
  <div class="col-md-3 col-md-pull-9">.col-md-3 .col-md-pull-9</div>
</div>
```

列嵌套  

已经分了的，内部还可以再分  

### 常用样式  

#### 排版  

标题  
bootstrap 会覆盖原来标题样式，bootstrap 样式会有略微调整  
后面加 <small> 或 添加 class='small' 来添加副标题  
```html
<h1>h1. Bootstrap heading</h1>  
<h1>h1. Bootstrap heading <small>Secondary text</small></h1>
```

段落  
p 标签  
<small>:小号
\<b>\<strong>:加粗  
\<em>:斜体

强调  
有一些类，比如 :text-primary 等，一共有 6 个  

对齐  
```html
<p class="text-left">Left aligned text.</p>
<p class="text-center">Center aligned text.</p>
<p class="text-right">Right aligned text.</p>
<p class="text-justify">Justified text.</p>
<p class="text-nowrap">No wrap text.</p>
```

列表  
无序 ul  
有序 ol  

#### 代码  
通过 \<code> 标签包裹内联样式的代码片段。单行代码  
通过 \<kbd> 标签标记用户通过键盘输入的内容。快捷键效果  
多行代码可以使用 \<pre> 标签。为了正确的展示代码，注意将尖括号做转义处理。可以添加滚动条  
通过 \<var> 标签标记变量。  
通过 \<samp> 标签来标记程序输出的内容。  

#### 表格  

bootstrap 的表格样式非常漂亮，用的很多  

```html
<table class="table">
  ...
</table>
```
通过 .table-striped 类可以给 <tbody> 之内的每一行增加斑马条纹样式。  
添加 .table-bordered 类为表格和其中的每个单元格增加边框。  
通过添加 .table-hover 类可以让 <tbody> 中的每一行对鼠标悬停状态作出响应。  
通过添加 .table-condensed 类可以让表格更加紧凑，单元格中的内补（padding）均会减半。  
通过状态类可以为行或单元格设置颜色。    
将任何 .table 元素包裹在 .table-responsive 元素内，即可创建响应式表格，其会在小屏幕设备上（小于768px）水平滚动。当屏幕大于 768px 宽度时，水平滚动条消失。  

#### 表单  

.form-control  
默认显示 100%，可以通过栅格来控制宽度  

文本框 input  
下拉框 select  
文本域 textarea

单选框 radio  
复选框 checkbox  

表单布局  
水平表单用的最多  
.form-horizontal  


#### 按钮  

为 <a>、<button> 或 <input> 元素添加按钮类（button class）即可使用 Bootstrap 提供的样式。  
```html
<a class="btn btn-default" href="#" role="button">Link</a>
<button class="btn btn-default" type="submit">Button</button>
<input class="btn btn-default" type="button" value="Input">
<input class="btn btn-default" type="submit" value="Submit">
```
可以预定义样式的按钮。    
  
```html
<!-- Standard button -->
<button type="button" class="btn btn-default">（默认样式）Default</button>

<!-- Provides extra visual weight and identifies the primary action in a set of buttons -->
<button type="button" class="btn btn-primary">（首选项）Primary</button>

<!-- Indicates a successful or positive action -->
<button type="button" class="btn btn-success">（成功）Success</button>

<!-- Contextual button for informational alert messages -->
<button type="button" class="btn btn-info">（一般信息）Info</button>

<!-- Indicates caution should be taken with this action -->
<button type="button" class="btn btn-warning">（警告）Warning</button>

<!-- Indicates a dangerous or potentially negative action -->
<button type="button" class="btn btn-danger">（危险）Danger</button>

<!-- Deemphasize a button by making it look like a link while maintaining button behavior -->
<button type="button" class="btn btn-link">（链接）Link</button>
```
使用 .btn-lg、.btn-sm 或 .btn-xs 就可以获得不同尺寸的按钮。  

为 <button> 元素添加 disabled 属性，使其表现出禁用状态。  

#### 缩略图 

.tumbnail  

图标直接去菜鸟教程上的 bootstrap 教程上找图标复制粘贴就可以了  

#### 面板 

.panel  

### 组件  

标签式导航  

```html
<ul class="nav nav-tabs">
  <li role="presentation" class="active"><a href="#">Home</a></li>
  <li role="presentation"><a href="#">Profile</a></li>
  <li role="presentation"><a href="#">Messages</a></li>
</ul>
```

胶囊式导航  

```html
<ul class="nav nav-pills">
  <li role="presentation" class="active"><a href="#">Home</a></li>
  <li role="presentation"><a href="#">Profile</a></li>
  <li role="presentation"><a href="#">Messages</a></li>
</ul>
```

#### 分页  

```html
<nav aria-label="Page navigation">
  <ul class="pagination">
    <li>
      <a href="#" aria-label="Previous">
        <span aria-hidden="true">&laquo;</span>
      </a>
    </li>
    <li><a href="#">1</a></li>
    <li><a href="#">2</a></li>
    <li><a href="#">3</a></li>
    <li><a href="#">4</a></li>
    <li><a href="#">5</a></li>
    <li>
      <a href="#" aria-label="Next">
        <span aria-hidden="true">&raquo;</span>
      </a>
    </li>
  </ul>
</nav>
```
翻页  
```html
<nav aria-label="...">
  <ul class="pager">
    <li><a href="#">上一页</a></li>
    <li><a href="#">下一页</a></li>
  </ul>
</nav>
```

#### 下拉菜单  

需要使用 jQuery  

.dropdown  


模态框  


