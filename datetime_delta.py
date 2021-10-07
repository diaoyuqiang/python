from datetime import datetime, timedelta

# 日期时间差获取
dt1 = datetime.strptime("2020-04-04 9:20:05", "%Y-%m-%d %H:%M:%S")
dt2 = datetime.strptime("2020-05-05 19:30:05", "%Y-%m-%d %H:%M:%S")
diff = dt2 - dt1

print("相差天数：{}, 相差小时：{:.2f}".format(diff.days, diff.seconds/(60*60)))

# 日期加减操作timedelta
dt = datetime.now()
n = 10.0
red = timedelta(days=n)
new_dt = dt + red
print(new_dt, type(new_dt))