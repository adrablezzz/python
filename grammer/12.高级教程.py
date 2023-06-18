# json
import json
# json.dumps(): 对数据进行编码。
# json.loads(): 对数据进行解码。

# 日期与事件
import time
# time.time() # 返回当前时间戳
# time.struct_time() # 返回时间元组
# print(time.strftime("%Y-%m-%d %H:%M:%S", time.localtime())) # 时间格式化

import calendar
cal = calendar.month(2023,6)
print(cal)