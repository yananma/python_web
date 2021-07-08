
[视频教程](https://www.bilibili.com/video/BV12J411m7MG?p=1)

### Vue 基础  

Vue 是一套 JavaScript 框架  
简化 DOM 操作  
响应式数据驱动  

入门一个框架或库的使用，没有比读官方文档更好的选择了  

创建文件，引入 Vue  

Vue.js 的核心是一个允许采用简洁的模板语法来声明式地将数据渲染进 DOM 的系统：  

一般默认选择器使用 id 选择器，因为一般而言，id 是唯一的，而类选择器和标签选择器是有很多同名的  

```js
<div id="app">
  {{ message }}
</div>
```
```js
var app = new Vue({
  el: '#app',
  data: {
    message: 'Hello Vue!'
  }
})
```
el 挂载点  
Vue 实例的作用范围是 el 选项命中的元素及其内部的后代元素  
也可以使用其他选择器，建议使用 id 选择器  

data：数据对象   
Vue 中用到的数据定义在 data 中  
data 中可以写复杂类型的数据  
渲染复杂类型数据时，遵守 js 的语法就行   

### Vue 本地应用  

Vue 指令  

#### v-text 指令  

设置标签的文本值(textContent)  

默认写法会替换全部内容，使用差值表达式 {{ }} 可以替换指定内容  
```js
<body>
    <div id="app">
        <h2 v-text="message+'!'">深圳</h2>
        <h2 v-text="info+'!'">深圳</h2>
        <h2>{{ message +'!'}}深圳</h2>
    </div>
    <!-- 开发环境版本，包含了有帮助的命令行警告 -->
    <script src="https://cdn.jsdelivr.net/npm/vue/dist/vue.js"></script>
    <script>
        var app = new Vue({
            el:"#app",
            data:{
                message:"hello!!!",
                info:"world "
            }
        })
    </script>
</body>
```

#### v-html  

设置标签的 innerHTML  
里面的 HTML 结构会被解析出来，就是会有超链接等效果  
```js
<body>
    <div id="app">
        <p v-html=content></p>
        <p v-text=content></p>
    </div>
    <!-- 开发环境版本，包含了有帮助的命令行警告 -->
    <script src="https://cdn.jsdelivr.net/npm/vue/dist/vue.js"></script>
    <script>
        var app = new Vue({
            el:"#app",
            data:{
                # content:"百度"  
                content:"<a href='www.baidu.com'>百度</a>
            }
        })
    </script>
</body>
```

#### v-on 绑定事件  

可以简写成 @  
方法写在 methods 中  
通过 this 关键字，获取 data 中的数据  

```js
<body>
    <div id="app">
        <input type="button" value="点击" v-on:click="doIt">
        <input type="button" value="点击" @click="doIt">
        <h2 @click="changeFood">{{ food }}</h2>
    </div>
    <!-- 1.开发环境版本，包含了有帮助的命令行警告 -->
    <script src="https://cdn.jsdelivr.net/npm/vue/dist/vue.js"></script>
    <script>
        var app = new Vue({
            el:"#app",
            data = {
                food:"西蓝花炒蛋"
            }
            methods: {
                doIt:function(){
                    alert("做IT");
                },
                changeFood:function(){
                    this.food += "好吃！"
                }
            },
        })
    </script>
</body>
```

#### v-show 指令  

原理是修改元素的 display，实现隐藏显示  

```js
<body>
<div id="app">
    <input type="button" value="切换显示状态" @click="changeIsShow">
    <input type="button" value="累加年龄" @click="addAge">
    <img v-show="isShow" src="./img/monkey.gif" alt="">
    <img v-show="age>=18" src="./img/monkey.gif" alt="">
</div>
<!-- 1.开发环境版本，包含了有帮助的命令行警告 -->
<script src="https://cdn.jsdelivr.net/npm/vue/dist/vue.js"></script>
<script>
    var app = new Vue({
        el: "#app",
        data: {
            isShow: false,
            age: 17
        },
        methods: {
            changeIsShow: function () {
                this.isShow = !this.isShow;
            },
            addAge: function () {
                this.age++;
            }
        },
    })
</script>
</body>
```

#### v-if 指令  

v-if 的本质是通过操作 DOM 元素来切换状态  

```js
<body>
    <div id="app">
        <input type="button" value="切换显示" @click="toggleIsShow">
        <p v-if="isShow">world </p>
        <p v-show="isShow">hello - v-show修饰</p>
        <h2 v-if="temperature>=35">高温预警</h2>
    </div>
    <!-- 开发环境版本，包含了有帮助的命令行警告 -->
    <script src="https://cdn.jsdelivr.net/npm/vue/dist/vue.js"></script>
    <script>
        var app = new Vue({
            el:"#app",
            data:{
                isShow:false,
                temperature:20
            },
            methods: {
                toggleIsShow:function(){
                    this.isShow = !this.isShow;
                }
            },
        })
    </script>
</body>
```

#### v-bind 指令 

v-bind 为元素绑定属性  
可以省略 v-bind，直接使用冒号  

```js
<body>
    <div id="app">
        <img v-bind:src="imgSrc" alt="">
        <br>
        <img :src="imgSrc" alt="" :title="imgTitle+'!!!'" :class="isActive?'active':''" @click="toggleActive">
        <br>
        <img :src="imgSrc" alt="" :title="imgTitle+'!!!'" :class="{active:isActive}" @click="toggleActive">
    </div>
    <!-- 开发环境版本，包含了有帮助的命令行警告 -->
    <script src="https://cdn.jsdelivr.net/npm/vue/dist/vue.js"></script>
    <script>
        var app = new Vue({
            el:"#app",
            data:{
                imgSrc:"https://www.baidu.com/img/PCtm_d9c8750bed0b3c7d089fa7d55720d6cf.png",
                imgTitle:"百度 logo",
                isActive:false
            },
            methods: {
                toggleActive:function(){
                    this.isActive = !this.isActive;
                }
            },
        })
    </script>
</body>
```

#### v-for 指令  

```js
<body>
    <div id="app">
        <input type="button" value="添加数据" @click="add">
        <input type="button" value="移除数据" @click="remove">

        <ul>
            <li v-for="(it,index) in arr">
                {{ index+1 }}校区:{{ it }}
            </li>
        </ul>
        <h2 v-for="item in vegetables" v-bind:title="item.name">
            {{ item.name }}
        </h2>
    </div>
    <!-- 1.开发环境版本，包含了有帮助的命令行警告 -->
    <script src="https://cdn.jsdelivr.net/npm/vue/dist/vue.js"></script>
    <script>
        var app = new Vue({
            el:"#app",
            data:{
                arr:["北京","上海","广州","深圳"],
                vegetables:[
                    {name:"西兰花炒蛋"},
                    {name:"蛋炒西蓝花"}
                ]
            },
            methods: {
                add:function(){
                    this.vegetables.push({ name:"花菜炒蛋" });
                },
                remove:function(){
                    this.vegetables.shift();
                }
            },
        })
    </script>
</body>

```
#### v-on 补充  

可以传参  
```js
<body>
    <div id="app">
        <input type="button" value="点击" @click="doIt(666,'老铁')">
        <input type="text" @keyup.enter="sayHi">
    </div>
    <!-- 1.开发环境版本，包含了有帮助的命令行警告 -->
    <script src="https://cdn.jsdelivr.net/npm/vue/dist/vue.js"></script>
    <script>
        var app = new Vue({
            el:"#app",
            methods: {
                doIt:function(p1,p2){
                    console.log("做it");
                    console.log(p1);
                    console.log(p2);
                },
                sayHi:function(){
                    alert("吃了没");
                }
            },
        })
    </script>
</body>
```

#### v-model 指令  

获取和设置表单元素的值(双向数据绑定)  
```js
<body>
    <div id="app">
        <input type="button" value="修改message" @click="setM">
        <input type="text" v-model="message" @keyup.enter="getM">
        <h2>{{ message }}</h2>
    </div>
    <!-- 开发环境版本，包含了有帮助的命令行警告 -->
    <script src="https://cdn.jsdelivr.net/npm/vue/dist/vue.js"></script>
    <script>
        var app = new Vue({
            el:"#app",
            data:{
                message:"程序员"
            },
            methods: {
                getM:function(){
                    alert(this.message);
                },
                setM:function(){
                    this.message ="酷丁鱼";
                }
            },
        })
    </script>
</body>
```

### 网络应用  

#### axios  

axios 是功能强大的网络请求库  

```js
<body>
    <input type="button" value="get请求" class="get">
    <input type="button" value="post请求" class="post">
    <!-- 官网提供的 axios 在线地址 -->
    <script src="https://unpkg.com/axios/dist/axios.min.js"></script>
    <script>
        /*
            接口1:随机笑话
            请求地址:https://autumnfish.cn/api/joke/list
            请求方法:get
            请求参数:num(笑话条数,数字)
            响应内容:随机笑话
        */
        document.querySelector(".get").onclick = function () {
            axios.get("https://autumnfish.cn/api/joke/list?num=6")
            // axios.get("https://autumnfish.cn/api/joke/list1234?num=6")
            .then(function (response) {
                console.log(response);
              },function(err){
                  console.log(err);
              })
        }
        /*
             接口2:用户注册
             请求地址:https://autumnfish.cn/api/user/reg
             请求方法:post
             请求参数:username(用户名,字符串)
             响应内容:注册成功或失败
         */
        document.querySelector(".post").onclick = function () {
            axios.post("https://autumnfish.cn/api/user/reg",{username:"盐焗西兰花"})
            .then(function(response){
                console.log(response);
                console.log(this.skill);
            },function (err) {
                console.log(err);
              })
          }

    </script>
</body>
```

#### axios + Vue  

```js
<body>
    <div id="app">
        <input type="button" value="获取笑话" @click="getJoke">
        <p> {{ joke }}</p>
    </div>
    <!-- 官网提供的 axios 在线地址 -->
    <script src="https://unpkg.com/axios/dist/axios.min.js"></script>
    <!-- 开发环境版本，包含了有帮助的命令行警告 -->
    <script src="https://cdn.jsdelivr.net/npm/vue/dist/vue.js"></script>
    <script>
        /*
            接口:随机获取一条笑话
            请求地址:https://autumnfish.cn/api/joke
            请求方法:get
            请求参数:无
            响应内容:随机笑话
        */
        var app = new Vue({
            el:"#app",
            data:{
                joke:"很好笑的笑话"
            },
            methods: {
                getJoke:function(){
                    // console.log(this.joke);
                    var that = this;
                    axios.get("https://autumnfish.cn/api/joke").then(function(response){
                        // console.log(response)
                        console.log(response.data);
                        // console.log(this.joke);
                        that.joke = response.data;
                    },function (err) {  })
                }
            },
        })

    </script>
</body>
```

