
## 爱鲜蜂项目  

先设计表，表的字段，表的关系  

先完成主要功能，走通流程，再优化细节  

版本迭代，不要一次增加太多功能  

接口就是路由  

#### 设计分析  

主页面显示：最简单，数据查询显示  

商品数据展示：级联查询，排序  

用户系统：是业务的核心系统，只要有用户，别的都好说；腾讯做事容易做成，并不是产品做得好，而是用户来的快。  

购物车系统：商品和用户的关系；订单系统，购物车数据转换成订单；支付系统，很简单就是接口调用。  

扩展：地址管理系统，积分系统，会员级别系统，评价系统，优惠券系统，数据安全，过滤器，反爬，权限  

部署：动静分离部署  


#### 项目搭建 

开发流程：基本工程搭建，前端静态页面搭建，Model to DB，业务逻辑开发，前后端协同开发    

在应用中创建 urls.py 

创建静态文件夹 static，添加文件，css、js、fonts、img、uploads  

创建 base.html，title 设置变量，引入 CSS 和 JS，

前端配置，推荐百分比而不是固定尺寸，因为屏幕各种尺寸都有  

适配单位  
* px  
* em，默认相对于父级元素，默认大小 1em=16px  
* rem，默认相对于根元素，r 代表 root，默认大小 1rem=16px  

先创建 4 个 HTML 页面，配置 4 个路由  

切换页面的时候，底部不发生变化  

用 swiper 实现轮播图，用法看官网  

安装 django-debug-toolbar，按照官网教程说明配置  

django-debug-toolbar 拥有极强的调试功能，提供了各种信息的获取  

首页就是页面展示  


#### 闪购页面  

闪购，也就是 filter、exclude，还有 order_by  

商品应该有商品 id，数字排序更方便  

先创建表，迁移到数据库，插入数据  

要创建两个 model，一个是 category 表，一个是 product 表，product 表中添加 category_id 字段，设置 ForeignKey 关联 category  

然后在 views.py 中查询数据  

查询数据的时候，视图函数中传输 category 的 id  
```python
def product(request, cid):
    product_list = Product.objects.filter(category_id=cid)  
```    

前端在 a 链接中添加标签。  
`<a href="{% url 'axf:product' category_id=category.id %}"</a>`  

左侧是大类型，右侧上方为小类型，大类型和小类型之间是一对多的关系。   

二级查询的时候，先进行一级查询，然后再在一级查询的基础上进行一次查询。SQL 语句就是先根据一级分类 id 查询，然后再 AND 二级分类 id 查询。    

一级查询： `category_list = Category.objects.all()` `category = Category.get(category_id=cid)`  
二级查询：`second_category = category.second_category_names`，然后先按照 \# 进行 split，得到一个列表，再按照 : 进行 split，得到二级分类的名称和 id，然后把列表共享到前端，前端就可以取到二级分类的名字了。
而查询，则是因为在数据表中，有一个字段就是二级分类的 id，根据这个 id 就可以进行查询。  

函数参数要再传入一个二级查询 second_category 的 id，sid，前端的 a 链接查询的时候，后面也是要跟两个 id  
```python
def product(request, cid, sid):
    product_list = Product.objects.filter(category_id=cid).filter(second_category_id=sid)    
```    

上面这种做法，查询子类是可以的，但是在查询全部分类的时候，就会什么都查不到，所以还要进行一个判断，如果是全部分类的查询，就不进行二级查询。  

```python
def product(request, cid, sid):
    ALL_TYPE = '0'
    if sid == ALL_TYPE:
        product_list = Product.objects.filter(category_id=cid) 
    else:
        product_list = Product.objects.filter(category_id=cid).filter(second_category_id=sid)    
```    

前端查询的时候，点击全部分类，把向下的箭头改成向上的箭头，用 jQuery 实现。  
`$span.removeClass("glyphicon-chevron-down").addClass("glyphicon-chevron-up")`  

前端应该做一个判断，在全部分类点开以后，应该是选中的才是 active，没选中的就是平常的颜色，办法就是根据 id 判断，如果等于 id 就 active  

综合排序，里面是有多种选择条件的，办法就是在视图函数中做多次判断，视图函数中要传入一个 order_id，oid，然后把排序情况赋值为数字，如果 oid 等于某一个条件的 id，就按某一种方式 order_by。  








