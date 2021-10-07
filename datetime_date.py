from datetime import date
# 构建日期对象
d = date(2021, 10, 15)
print(d)
# 获取当前日期
today = date.today()
print(today)
print(today.replace(2020, 10, 14))  # 替换当前日期

# 获取日期的星期几（1-7）
d = today.isoweekday()
print("今天是星期：%d" % d)
# 格式化日期，返回字符串
ds = today.isoformat()
print(ds, type(ds))

# 返回当前日期的元祖
time_tuple = today.timetuple()
print(time_tuple)