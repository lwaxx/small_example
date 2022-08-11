import datetime

# 字符类型日期时间转%Y%m%d%H%M%S
# 2020-03-01 15:12:12 => 20200301151212
import time
a = time.strptime("2020-03-01 15:12:12", "%Y-%m-%d %H:%M:%S")
b = time.strftime("%Y%m%d%H%M%S", a)
print(b)


# 当前时间30分钟后时间日期，35分钟后时间日期
start_time1 = (datetime.datetime.now()+datetime.timedelta(minutes=30)).strftime("%Y-%m-%d %H:%M:%S")
end_time1 = (datetime.datetime.now()+datetime.timedelta(minutes=30)+datetime.timedelta(minutes=5)).strftime("%Y-%m-%d %H:%M:%S")
print(start_time1)
print(end_time1)


# 下周一零点
today = datetime.datetime.today()
wd = today.weekday()    # 周几，从0开始算
next_monday = datetime.datetime(today.year, today.month, today.day) + datetime.timedelta(days=7-wd)
print(today)
print(wd)
print(next_monday)


# 24小时之后的时间
expire = today + datetime.timedelta(hours=24)
print(expire)


