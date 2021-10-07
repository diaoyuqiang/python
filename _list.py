import time
import random
from datetime import timedelta, datetime

li = [1, 2, 3, 4]
while len(li) > 0:
    a = li.pop()
    print(a)

print(f"{80 * 10}")  # 格式化计算{}

data = random.random()  # 0-1随机浮点数
print(data)

# 获取字典中的value
dict1 = {"name": "dyq", "age": "18"}
print(dict1.get("name"))

# 获取当前日期时间字符串
time1 = datetime.now()
print(time1.strftime("%y-%m-%d %H:%M:%S"))

time2 = time1 + timedelta(minutes=10)  # timedelta() 两个时间的间隔
print(time2.strftime("%y-%m-%d %H:%M:%S"))

# %X: 时间格式化
d = time.strftime("%Y-%m-%d %X")
print(d)