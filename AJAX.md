
#### AJAX 简介  
异步请求，局部刷新。  

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


