
ES 应用场景：搜索、日志、可视化   


 类别 | 操作 | 备注   
---- | --- | ---  
标签云 | 存储桶 -> 重要词 -> DestCityName -> 10 | 选择时间跨度<br>修改标题
饼图  | 存储桶 -> 拆分切片 -> 重要词 -> DestCountry -> 10 | 显示图例    
指标  |  |    
目标图  | 添加筛选 -> Cancelled -> 是 -> true<br>选项 -> 取消百分比 |  
水平条形图  | 存储桶 -> X 轴 -> 重要词 -> FlightDelayType -> 10 |  
垂直条形图  | 存储桶 -> X 轴 -> 重要词 -> DestAirportID -> 20 | 可以改图例颜色  
垂直条形图  | 存储桶 -> X 轴 -> Date Histogram -> 更新<br>添加 -> 拆分序列 -> 重要序列 -> FlightDelayType -> 20 | 选中图例<br>检查聚合请求  
折线图  | 存储桶 -> X 轴 -> Date Histogram -> 更新<br>指标 -> 添加 -> Y 轴 -> 平均值 -> AvgTicketPrice<br>指标 -> 添加 -> 圆点大小 -> 平均值 -> AVGTicketPrice<br>指标和轴 Tab -> 指标 -> 计数 -> RightAxis-1 -> 面积图 -> 堆叠（作用？）<br>指标和轴 Tab -> 指标 -> AVGTicketPrice 平均值 -> 取消显示线条 |  
热图  | 存储桶 -> X 轴 -> 重要词 -> OriginCountry -> 10<br>存储桶 -> Y 轴 -> 重要词 -> DestCountry -> 10 |  
Maps  | 添加图层 -> Elasticsearch -> 集群和网格 -> 添加图层 -> Origin -> 指标 -> 平均值 -> AVGTicketPrice<br>添加图层 -> Elasticsearch -> 集群和网格 -> 添加图层 -> Dest -> 指标 -> 平均值 -> AVGTicketPrice | 修改圆圈颜色  
Discover  | 右侧可以展开<br>左侧可以看前 5 个<br>可以 Visualize：DestRegion -> Visualize -> 拖拽 -> DestCountry<br>可以在左侧点击加号，往右侧添加字段 |  
其他功能  | 可以筛选一个，其他的一起跟着变<br>可以设置刷新频率 |  
