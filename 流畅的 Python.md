
### 第1章 Python数据模型  

访问属性，调用方法的时候，就会调用 \_\_getitem__ ,   

for 循环背后调用的是 iter(), 背后是 \_\_iter__    

\_\_repr__ 的作用是实现字符串现实形式  

占位符 % 和 .format() 背后用的就是 \_\_repr__  

使用 if while and or 这些的时候，会调用 bool() 进行判断  



