
ES 应用场景：搜索、日志、可视化   


 类别 | 操作 | 备注   
---- | --- | ---  
标签云 | 存储桶 -> 标签 -> 重要词 -> DestCityName -> 10 | 选择时间跨度<br>修改标题
饼图  | 存储桶 -> 拆分切片 -> 重要词 -> DestCountry -> 10 | 显示图例    
指标  |  |    
目标图  | 选项 -> 取消百分比 -> 更新<br>添加筛选 -> Cancelled -> 是 -> true |  
水平条形图  | 存储桶 -> X 轴 -> 重要词 -> FlightDelayType -> 10 |  
垂直条形图  | 存储桶 -> X 轴 -> 重要词 -> DestAirportID -> 20 | 可以改图例颜色  
垂直条形图  | 存储桶 -> X 轴 -> Date Histogram -> 更新<br>添加 -> 拆分序列 -> 重要词 -> FlightDelayType -> 5 | 选中图例<br>检查聚合请求  
热图  | 存储桶 -> X 轴 -> 重要词 -> OriginCountry -> 10<br>存储桶 -> Y 轴 -> 重要词 -> DestCountry -> 10 |  
折线图  | 存储桶 -> X 轴 -> Date Histogram -> 更新<br>指标 -> 添加 -> Y 轴 -> 平均值 -> AvgTicketPrice<br>指标和轴 Tab -> 计数 -> 值轴 -> 新建轴<br>点击图例可以不显示<br>指标 -> 添加 -> 圆点大小 -> 平均值 -> AVGTicketPrice<br>指标和轴 Tab -> 指标 -> 计数 -> RightAxis-1 -> 面积图 -> 取消显示点线<br>指标和轴 Tab -> 指标 -> AVGTicketPrice 平均值 -> 取消显示线条 |  
Maps  | 添加图层 -> Elasticsearch -> 集群和网格 -> 添加图层 -> Origin -> 指标 -> 平均值 -> AVGTicketPrice<br>添加图层 -> Elasticsearch -> 集群和网格 -> 添加图层 -> Dest -> 指标 -> 平均值 -> AVGTicketPrice | 修改圆圈颜色  
Discover  | 右侧可以展开<br>左侧可以看前 5 个<br>可以 Visualize：DestRegion -> Visualize -> 拖拽 -> DestCountry<br>可以在左侧点击加号，往右侧添加字段<br>FlightNum -> OriginCityName -> OriginWeather -> DestCityName -> DestWeather -> AvgTicketPrice |  
其他功能  | 更多 -> 最大化面板<br>可以筛选一个，其他的一起跟着变<br>可以设置刷新频率<br>可以发预警邮件<br>可以嵌入到别的代码里 |  
