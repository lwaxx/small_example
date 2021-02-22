# 字符类型日期时间转%Y%m%d%H%M%S
# 2020-03-01 15:12:12 => 20200301151212
import time
a = time.strptime("2020-03-01 15:12:12", "%Y-%m-%d %H:%M:%S")
b = time.strftime("%Y%m%d%H%M%S", a)
print(b)