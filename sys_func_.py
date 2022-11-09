import sys, math

a = 10
# 返回对象的大小(字节数)
print(sys.getsizeof(a))

# 长度不区分中文
print(len("hell 中国"))
# 查看当前使用的python版本号
print('python:', sys.version_info)  # (major=3, minor=9, micro=12, releaselevel='final', serial=0)
                                    # 主版本号 次要版本号 微型版本号 发布级别 序列号

# 判断解释器版本号
if sys.version_info >= (3, 2):
    print('okkk')


n = math.fmod(-3, 2)  # 获取正负数的余数
print(n)

m = -3 % 2  # 在为负数时候，远离0的方向, 取正余数
print(m)

