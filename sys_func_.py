import sys, math

a = 10
# 返回对象的大小(字节数)
print(sys.getsizeof(a))

# 长度不区分中文
print(len("hell 中国"))

n = math.fmod(-3, 2)  # 获取正负数的余数
print(n)

m = -3 % 2  # 在为负数时候，远离0的方向, 取正余数
print(m)
