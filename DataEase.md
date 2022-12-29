

可以快速实现简单的常见的需求。      

客户可以自己创建图表，不过还是有点儿难度。        

```python 
1. 添加 competitive_oid 列
SELECT ts.objectid, ts.name, ts.date, ts.all_count, uo.competitive_oid FROM tongyong_sentiment as ts JOIN user_obj as uo ON ts.objectid = uo.objectid


2. 子查询  
SELECT objectid, name, all_count FROM (SELECT ts.objectid, ts.name, ts.date, ts.all_count, uo.competitive_oid FROM tongyong_sentiment as ts JOIN user_obj as uo ON ts.objectid = uo.objectid) AS tsuo WHERE objectid = 303326 


3 子查询添加 competitive_oid  
SELECT objectid, name, all_count, competitive_oid FROM (SELECT ts.objectid, ts.name, ts.date, ts.all_count, uo.competitive_oid FROM tongyong_sentiment as ts JOIN user_obj as uo ON ts.objectid = uo.objectid) AS tsuo WHERE objectid = 303326


4. 参数设置  
SELECT * FROM tongyong_sentiment WHERE name = '${name}'


5. 添加 CASE 语句
SELECT objectid, name, all_count, CASE WHEN competitive_oid = 0 THEN "yes" ELSE "no" END FROM (
  SELECT ts.objectid, ts.name, ts.date, ts.all_count, uo.competitive_oid FROM tongyong_sentiment as ts JOIN user_obj as uo ON ts.objectid = uo.objectid
) AS tsuo 
WHERE objectid = 303326


6. CASE 语句字段重命名 
SELECT objectid, name, CASE WHEN competitive_oid = 0 THEN objectid ELSE objectid || competitive_oid END as cop_id FROM (
  SELECT ts.objectid, ts.name, uo.competitive_oid FROM tongyong_sentiment as ts JOIN user_obj as uo ON ts.objectid = uo.objectid
) AS tsuo 
WHERE objectid IN (303326,303361) 


7. 在 WHERE 语句中使用 CASE 
SELECT objectid, name, all_count, competitive_oid FROM (
    SELECT ts.objectid, ts.name, ts.all_count, uo.competitive_oid FROM tongyong_sentiment AS ts JOIN user_obj AS uo ON ts.objectid = uo.objectid
) AS tsuo
WHERE objectid = CASE WHEN tsuo.competitive_oid = 0 THEN objectid ELSE competitive_oid END


8. if 语句 
SELECT objectid, if(objectid = 303306, "道朗格","不是道朗格") mod_name FROM user_obj
``` 


