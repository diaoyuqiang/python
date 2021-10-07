from datetime import time
# 构建时间对象
t = time(17, 20, 30, 23456)  # 时，分，秒，微妙
print(t)
# 替换时间
print(t.replace(20, 30, 10))

# 标准格式化时间 返回str
t = time(9, 10, 30, 123456).isoformat(timespec="hours")
print(t)

# 时间对象格式化字符串
t = time(8, 20, 30).strftime("%H:%M:%S")
print(t, type(t))