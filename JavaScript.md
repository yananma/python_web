
# jQuery 实践笔记       

## 语法   

#### for 循环   

```js 
for (let i=0; i<res.data.length; ++i) {
            
}
```

### 字符串    

#### [replace](https://www.w3school.com.cn/js/js_string_methods.asp)      

默认 replace 只替换第一个，如果替换所有就要加 g 参数。   

比如全部的单引号替换成双引号    

```js  
str.replace(/'/g, "\"")
```




#### 字符串转数字   

数字和字符串 + 的时候，会自动把数字转成字符串。      

或者使用 String(数字)     


#### 字符串转 JSON   

```js   
JSON.parse(str)   
```

#### 查看类型   

```js 
typeof obj
```

#### 判断非空，不等于 null   

```js  
obj !== "null"(双引号)
```





### 项目   

#### 执行函数    

只定义函数是不会执行的，要执行的话，就要用 $ 符号，加载完毕执行   

```js 
$(function get_detail_data() {
  $.ajax({
    type: "GET",
    url: "/true_detail",
    async: false,
    success: function (res) {
        console.log(res)
    },
    error: function (e) {
      console.log(e)
    }
  })
})
```


#### 引入 html 文件    

顺序是 url -> views 视图 -> 找到 html -> html 中引入 jQuery     

核心是通过视图函数连接各个部分。      

```python 
from django.shortcuts import render
from django.http import JsonResponse


def list_view(request):
    return render(request, 'list.html')


def detail_view(request):
    return render(request, 'detail.html')


def thumbnail_view(request):
    return render(request, 'thumbnail.html')


def login_view(request):
    return render(request, 'login.html')
```


# Ajax  

## 实践笔记    

#### 参数   

async：异步。True 的时候是异步，不等待，False 的时候是同步，同步就是等待。   
sync：同步   

dataType:'json'   
headers: {'token': localStorage.getItem("Authorization")}    


#### 用法  

GET 请求   

```javascript  
function user_info() {
  $.ajax({
    type: "GET",
    url: "/account/info/",
    async: false,
    success: function (res) {
      console.log(res)
    },
    error: function (e) {
      console.log(e)
    }
  })
}
```

#### 视图函数   

```python 
from django.http import JsonResponse   

def detail_view(request):
    """详情页面视图函数"""
    origin_img_list = RecognizeResult.objects.filter(video_id=17)
    img_list = get_img_list(origin_img_list)
    result_dict = {'data': img_list, 'status': 200}
    return JsonResponse(result_dict)
```


***     

可以通过浏览器的 Network 查看下载 jQuery 文件     

click 事件不起作用，很可能就是因为没有写在 $(fucntion) 里    

代码没有实现预期的功能，第一个要检查的问题就是，浏览器的代码有没有更新。  

在浏览器里 debug   

push 就是 append  

```js
send_list = []
[]

send_list.push(1) 
1

send_list
[1]

send_list.push(2) 
2

send_list
(2) [1, 2]

send_list.push(3) 
3

send_list
(3) [1, 2, 3]
```


简单写一点笔记，一节课一两行，遇到了不懂的再查，再补充  

#### 简介

实现动态效果  

script 里面的内容就是 js 代码，style 里面就是 css    

```js
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

读项目里的 jQuery 代码，找一些好的，作为补充例子  

jQuery 是 JavaScript 的一个类库，非常强大，write less，do more.  

可以通过选择器实现快速查询定位，而且非常简洁  

访问和操作数据元素  
修改页面样式  
事件处理  
实现动画和特效  
提供大量插件  
与 ajax 结合的很好  


#### 下载使用 jQuery  

官网下载，官网：https://jquery.com/   

点击 Download jQuery，选择 Download the uncompressed, development jQuery 3.6.0，点开以后看到的是源码，Ctrl + s 保存，然后复制到目录的 js 文件夹下，script 标签 src 导入，和 Python 的 import 一模一样  

```html
<script src="plugins/jquery/jquery.min.js"></script>
```


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

选择的时候，就是使用 html 操作内容，用 val 获取表单元素  


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
        $("body").prepend(h1);
        $("body").append(a1);
      })
    })
  </script>
</head>
<body>

  <button type="button" name="button">创建元素</button>

</body>
```
5. 内部插入：append() prepend()  
6. 外部插入：after() before() 
7. 复制元素：clone()  
8. 替换元素：replaceWith(content) replaceAll(selector)  
9. 包装元素：wrap(html) wrap(element) wrap(function)  
10. 元素的遍历：each(callback) 
11. 删除元素：remove([expr]) empty()   


#### jQuery 事件处理  

1. ready() 事件：是最常用的事件，一般都省略不写  
```javascript
$(function () {
    alert('Hello Welcome');
})
```
2. 绑定事件：bind(type, [data], fn)
3. 切换事件：hover() toggle()  
4. 解除事件：unbind()  
5. 触发事件：one() trigger()  
6. 浏览器事件：ready() resize() scroll()  
7. 鼠标事件：click() dbclick() hover() mousedown() 等等  
```javascript
$(function() {
    $("button").bind(
        {
            click:function() {console.log('click');},
            focus:function() {console.log('focus');},
            mousedown:function() {console.log('mousedown');},
            mouseup:function() {console.log('mouseup');}
        }
    )
})
```
8. 键盘事件：keydown() keypress() keyup() 

location.reload() 重新加载页面  





## 原来笔记   


Call a local script on the server /api/getWeather with the query parameter zipcode=97201 and replace the element #weather-temp's html with the returned text.
```js
$.ajax({
  url: "/api/getWeather",
  data: {
    zipcode: 97201   # 这里是 query string  
  },
  success: function( result ) {
    $( "#weather-temp" ).html( "<strong>" + result + "</strong> degrees" );
  }
});
```

引入 jQuery  
```js
$.ajax({
    url: '要提交的地址', 
    type: 'POST',  // GET 或 POST
    data: {'key1':value1, 'key2': value2}  // 要提交的数据  
    success: function(result) {
        // 当服务器处理完毕后，自动执行的回调函数  
	// result 是返回的数据  
	if (成功) {
	}else{
	} 	
    }
})
```
js 重定向：`location.href = '要跳转的地址'`  

#### AJAX 简介  
异步请求，局部刷新。  

form 表单提交，页面就会刷新，刷新，提交表单就会消失，想要不刷新，就要用 ajax  
ajax 绕过了表单  

AJAX = Asynchronous JavaScript and XML（异步的 JavaScript 和 XML）。  
AJAX 不是新的编程语言，而是一种使用现有标准的新方法。  
AJAX 最大的优点是在不重新加载整个页面的情况下，可以与服务器交换数据并更新部分网页内容。（比如添加商品，局部刷新这一项商品的总价和剩余库存）  
AJAX 不需要任何浏览器插件，但需要用户允许JavaScript在浏览器上执行。  

AJAX 是一种在无需重新加载整个网页的情况下，能够更新部分网页的技术。  

是一种用于创建快速动态网页的技术。  

通过在后台与服务器进行少量数据交换，AJAX 可以使网页实现异步更新。这意味着可以在不重新加载整个网页的情况下，对网页的某部分进行更新。  

传统的网页（不使用 AJAX）如果需要更新内容，必需重载整个网页面。  

#### AJAX 工作原理  
浏览器：发生某个事件，创建 XMLHttpRequest 对象，发送 HttpRequest  
服务器：处理 HttpRequest，创建响应，并将数据返回给浏览器  
浏览器：使用 JS 处理返回的数据，更新页面内容  

Google Suggest 使用 AJAX 创造出动态性极强的 web 界面：当在谷歌的搜索框输入关键字时，JavaScript 会把这些字符发送到服务器，然后服务器会返回一个搜索建议的列表。  


#### AJAX 实例  
```js 
<!DOCTYPE html>
<html>
<head>
<meta charset="utf-8">
<script>    # 这里是 script 脚本  
function loadXMLDoc()
{
	var xmlhttp;
	if (window.XMLHttpRequest)
	{
		xmlhttp=new XMLHttpRequest();
	}
	xmlhttp.onreadystatechange=function()
	{
		if (xmlhttp.readyState==4 && xmlhttp.status==200)
		{
			document.getElementById("myDiv").innerHTML=xmlhttp.responseText;
		}
	}
	xmlhttp.open("GET","/try/ajax/ajax_info.txt",true);
	xmlhttp.send();
}
</script>
</head>
<body>

<div id="myDiv"><h2>使用 AJAX 修改该文本内容</h2></div>
<button type="button" onclick="loadXMLDoc()">修改内容</button>

</body>
</html>
```
div 部分用于显示来自服务器的信息。  
button 负责在被点击时调用名为 loadXMLDoc() 的函数  

#### 创建 XMLHttpRequest 对象
XMLHttpRequest 是 AJAX 的基础。  

所有现代浏览器均支持 XMLHttpRequest 对象。  
XMLHttpRequest 用于在后台与服务器交换数据。这意味着可以在不重新加载整个网页的情况下，对网页的某部分进行更新。  

创建 XMLHttpRequest 对象的语法：  
`variable=new XMLHttpRequest();`  

#### 向服务器发送请求  
XMLHttpRequest 对象用于和服务器交换数据。  

如需将请求发送到服务器，我们使用 XMLHttpRequest 对象的 open() 和 send() 方法：  
`xmlhttp.open("GET","ajax_info.txt",true);`  
`xmlhttp.send();`  

open(method,url,async)   
method：请求的类型；GET 或 POST  
url：文件在服务器上的位置  
async：true（异步）或 false（同步）  

如果需要像 HTML 表单那样 POST 数据，请使用 setRequestHeader() 来添加 HTTP 头。然后在 send() 方法中写入希望发送的数据：  
```js
xmlhttp.open("POST","/try/ajax/demo_post2.php",true);
xmlhttp.setRequestHeader("Content-type","application/x-www-form-urlencoded");
xmlhttp.send("fname=Henry&lname=Ford");
```

open() 方法的 url 参数是服务器上文件的地址：  
`xmlhttp.open("GET","ajax_test.html",true);`  
该文件可以是任何类型的文件  

XMLHttpRequest 对象如果要用于 AJAX 的话，其 open() 方法的 async 参数必须设置为 true；不推荐使用 async=false  

对于 web 开发人员来说，发送异步请求是一个巨大的进步。很多在服务器执行的任务都相当费时。AJAX 出现之前，这可能会引起应用程序挂起或停止。  
通过 AJAX，JavaScript 无需等待服务器的响应，而是：  
在等待服务器响应时执行其他脚本  
当响应就绪后对响应进行处理  

#### 服务器 响应
如需获得来自服务器的响应，就需要使用 XMLHttpRequest 对象的 responseText 或 responseXML 属性。  
responseText	获得字符串形式的响应数据。  
responseXML	获得 XML 形式的响应数据。  

responseText 属性返回字符串形式的响应  
`document.getElementById("myDiv").innerHTML=xmlhttp.responseText;`  

#### onreadystatechange 事件  
当请求被发送到服务器时，我们需要执行一些基于响应的任务。  
每当 readyState 属性改变时，就会调用  onreadystatechange 函数。    
readyState 属性存有 XMLHttpRequest 的状态信息。  

readyState 存有 XMLHttpRequest 的状态。从 0 到 4 发生变化。  
0: 请求未初始化  
1: 服务器连接已建立  
2: 请求已接收  
3: 请求处理中  
4: 请求已完成，且响应已就绪  

status 就是 HTTP 的状态码 	 
200: "OK"  
404: 未找到页面  
等等  


在 onreadystatechange 事件中，我们规定当服务器响应已做好被处理的准备时所执行的任务。  
```js
xmlhttp.onreadystatechange=function()
{
    if (xmlhttp.readyState==4 && xmlhttp.status==200)
    {
        document.getElementById("myDiv").innerHTML=xmlhttp.responseText;
    }
}
```

回调函数是一种以参数形式传递给另一个函数的函数。  

#### Ajax 服务器实例  
当用户在上面的输入框中键入字符时，会执行函数 "showHint()" 。该函数由 "onkeyup" 事件触发：  
```js 
function showHint(str)
{
    var xmlhttp;
    if (str.length==0)
    { 
        document.getElementById("txtHint").innerHTML="";
        return;
    }
    if (window.XMLHttpRequest)
    {
        // IE7+, Firefox, Chrome, Opera, Safari 浏览器执行代码
        xmlhttp=new XMLHttpRequest();
    }
    xmlhttp.onreadystatechange=function()
    {
        if (xmlhttp.readyState==4 && xmlhttp.status==200)
        {
            document.getElementById("txtHint").innerHTML=xmlhttp.responseText;
        }
    }
    xmlhttp.open("GET","/try/ajax/gethint.php?q="+str,true);   # 这里是把输入内容，发送到服务器了  
    xmlhttp.send();
}
```
```html
<body>
<h3>在输入框中尝试输入字母 a:</h3>
<form action=""> 
输入姓名: <input type="text" id="txt1" onkeyup="showHint(this.value)" />
</form>
<p>提示信息: <span id="txtHint"></span></p> 
</body>
```

如果输入框为空 str.length==0，则该函数清空 txtHint 占位符的内容，并退出函数。  
如果输入框不为空，showHint() 函数执行以下任务：  
创建 XMLHttpRequest 对象  
当服务器响应就绪时执行函数  
把请求发送到服务器上的文件  
我们给 URL 添加了一个参数 q （带有输入框的内容）  


#### AJAX 数据库实例
AJAX 可用来与数据库进行动态通信。  

当用户在上面的下拉列表中选择某个客户时，会执行名为 "showCustomer()" 的函数。该函数由 "onchange" 事件触发：
```js
function showCustomer(str)
{
  var xmlhttp;    
  if (str=="")
  {
    document.getElementById("txtHint").innerHTML="";
    return;
  }
  if (window.XMLHttpRequest)
  {
    xmlhttp=new XMLHttpRequest();
  }
  xmlhttp.onreadystatechange=function()
  {
    if (xmlhttp.readyState==4 && xmlhttp.status==200)
    {
      document.getElementById("txtHint").innerHTML=xmlhttp.responseText;
    }
  }
  xmlhttp.open("GET","/try/ajax/getcustomer.php?q="+str,true);
  xmlhttp.send();
}
```
```html 
<body>

<form action=""> 
<select name="customers" onchange="showCustomer(this.value)" style="font-family:Verdana, Arial, Helvetica, sans-serif;">
<option value="APPLE">Apple Computer, Inc.</option>
<option value="BAIDU ">BAIDU, Inc</option>
<option value="Canon">Canon USA, Inc.</option>
<option value="Google">Google, Inc.</option>
<option value="Nokia">Nokia Corporation</option>
<option value="SONY">Sony Corporation of America</option>
</select>
</form>
<br>
<div id="txtHint">客户信息将显示在这...</div>

</body>
```
showCustomer() 函数执行以下任务：  
检查是否已选择某个客户  
创建 XMLHttpRequest 对象  
当服务器响应就绪时执行所创建的函数  
把请求发送到服务器上的文件  
我们给 URL 添加了一个参数 q （带有输入域中的内容）  

getcustomer.php" 中的源代码负责对数据库进行查询，然后用 HTML 表格返回结果  

#### AJAX XML 实例  
AJAX 可用来与 XML 文件进行交互式通信。  
```html
<!DOCTYPE html>
<html>
<head>
<meta charset="utf-8">
<style>
table,th,td {
  border : 1px solid black;
  border-collapse: collapse;
}
th,td {
  padding: 5px;
}
</style>
</head>
<body>

<h1>XMLHttpRequest 对象</h1>

<button type="button" onclick="loadXMLDoc()">获取我收藏的 CD</button>
<br><br>
<table id="demo"></table>

<script>
function loadXMLDoc() {
  var xhttp = new XMLHttpRequest();
  xhttp.onreadystatechange = function() {
    if (this.readyState == 4 && this.status == 200) {
      myFunction(this);
    }
  };
  xhttp.open("GET", "cd_catalog.xml", true);
  xhttp.send();
}
function myFunction(xml) {
  var i;
  var xmlDoc = xml.responseXML;
  var table="<tr><th>Artist</th><th>Title</th></tr>";
  var x = xmlDoc.getElementsByTagName("CD");
  for (i = 0; i <x.length; i++) {
    table += "<tr><td>" +
    x[i].getElementsByTagName("ARTIST")[0].childNodes[0].nodeValue +
    "</td><td>" +
    x[i].getElementsByTagName("TITLE")[0].childNodes[0].nodeValue +
    "</td></tr>";
  }
  document.getElementById("demo").innerHTML = table;
}
</script>

</body>
</html>
```
