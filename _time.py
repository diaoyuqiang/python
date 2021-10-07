import time
# 获取时间戳
t = time.time()
print(t)
# 获取时间元组
tl = time.localtime(1632289586.2269928)
print(tl)


# 获取UTC世界标准时间元祖
print(time.gmtime())

# 让线程挂起(沉睡)几秒
time.sleep(2)
print("执行结束")

