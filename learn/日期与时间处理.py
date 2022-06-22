import datetime

# h获取当前日期和时间
nowtime = datetime.datetime.now()
print(nowtime)
# 当前天
print(nowtime.day)
# 当前月
print(nowtime.month)
# 当前年
print(nowtime.year)
# 当前时间
print(nowtime.time())
# 将时间转成时间戳
print(nowtime.timestamp())
# 将字符串转成datetime实例
s = "2022-06-15 14:55:53"
s1 = datetime.datetime.strptime("2022-06-15 14:55:53", "%Y-%m-%d %H:%M:%S")
print(s1)
#将时间转成字符串
s2 = s1.strftime("%a-%b-%d %H:%M:%S")
print(s2)
#将时间戳转成时间
mtimestamp = 1655279155.460497
print(datetime.datetime.fromtimestamp(mtimestamp))



