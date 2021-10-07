from datetime import datetime
# 构建日期时间对象
dt = datetime(2021, 10, 14, 8, 30, 59, 123456)
print(dt)
# 获取当前时间
dt = datetime.today()
print(dt)
dt = datetime.now()  # 可加时区
print(dt)
# 获取标准时区的时间（0时区）
dt = datetime.utcnow()
print(dt)

# 日期时间转时间戳
dt = datetime(2021, 10, 14, 8, 30, 59, 123456)
tm_sp = dt.timestamp()
print(tm_sp)
# 时间戳转日期
rq = datetime.fromtimestamp(tm_sp)
print(rq)

# 日期时间格式化str
dt = datetime.today().strftime("%Y-%m-%d %H:%M:%S")
print(dt, type(dt))
# 字符串转日期
dt = datetime.strptime("2021-10-08 10:34:38", "%Y-%m-%d %H:%M:%S")
print(dt)

# 分别获取日期和时间
dt = datetime.today().date()
print(dt)
dt = datetime.today().time()
print(dt)