
#### 简介

实现动态效果  

script 里面的内容就是 js 代码，style 里面就是 css    

```javascript
function f1(){
    alert('hello world!')  
}  
```

#### 基本语法
统一编码，Unicode  

变量区分大小写，age 和 Age 是两个变量  

document.write() 就是 python 的 print  

console.log() 在控制台输出，控制台在浏览器 F12 打开  

字母下划线或 $ 开头，不能是数字开头  

写分号，表示一句话的结束  


#### 数据类型、变量、常量

js 没有 int short 这些，都是写 var  

str.length 就是 len()  

数字、字符串、布尔类型  





#### 表达式和运算符


#### 语句和流程控制  


#### 对象  


#### 数组  


#### 函数  


#### window 对象  


#### DOM 访问  


#### jQuery 简介  
jQuery 是 JavaScript 的一个类库，非常强大，write less，do more.  

可以通过选择器实现快速查询定位，而且非常简洁  

访问和操作数据元素  
修改页面样式  
事件处理  
实现动画和特效  
提供大量插件  
与 ajax 结合的很好  

官网：https://jquery.com/  

#### 下载使用 jQuery  
官网下载  
不用安装，直接放到文件中就行，script 标签 src 导入，和 Python 的 import 一模一样  

#### jQuery 的语法风格  
用的最多的就是 `$` 符号，这个符号就是 jQuery 的缩写  
通用模板就是 `$(selector).action(function)`  

比如 HTML 页面的一个 p 标签，可以在 <script> 标签中写函数    
```javascript  
$(function () {
    $("p").html("hello world");
    $("p").css("color", "red");
}) 
```
  
#### jQuery 的基本应用  
简单演示用法  

可以通过 id、class 和标签访问
```javascript  
$(function() {
    $("#title").css("color","red");
    $(".myCls").css("list-style","none");
    $("button").click(function() {
        alert("Hello jQuery");
    })
})
```

#### jQuery 选择器  
快速定位某个或某些元素  

基本选择器：id、class、标签  
层次关系选择器：空格、大于号、加号、siblings  
简单过滤选择器：:first :last :not :even :odd 等等 
内容过滤选择器：:contains(text) :empty :has(selector) :parent  
可见性过滤选择器：:hidden :visible  
属性过滤选择器：[attribute] [attribute=value] [attribute!=value] 等等  
子元素过滤选择器：:nth-child(eq|even|odd|index) :first-child :last-child :only-child  
表单选择器：:enabled :disabled :checked :select 还有 type 类型 :input :text :password :image :button 等等  


#### 操作 DOM 文档  

1. 属性操作：获取属性值 attr(name)，设置属性值 attr(key, val) 删除属性值 removeAttr(name)  
比如 `var title = $("a").attr("title")` `$("a").attr("title", "标题")` 等价于 `$("a").attr({"title":"标题"})` `$("a").removeAttr("title")`  
2. 元素内容操作：html() text()  
3. 元素样式操作：css() addClass() toggleClass() removeClass()  
4. 元素创建：$("")  
```javascript 
<script type="text/javascript">
    $(function() {
      $("button").click(function() {
        var h1 = $("<h1>网站标题</h>");
        var a1 = $("<a href='http://www.baidu.com'>百度</a>");
        $("body").append(h1);
        $("body").append(a1);
      })
    })
  </script>
</head>
<body>

  <button type="button" name="button">创建元素</button>

</body>
```



#### jQuery 事件处理  




