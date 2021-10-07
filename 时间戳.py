import time   # 时间戳模块 获取时间戳 time.time()
import datetime   # 获取当前日期 datetime.datetime.now()

curr_time = datetime.datetime.now()
print(curr_time)

time_str = curr_time.strftime('%Y-%m-%d %H:%M:%S')  # 日期格式化字符串输出
print(time_str)

time_stamp = time.time()  # 获取时间戳
print(time_stamp)

# now_time = time_stamp / (24*60*60*365) + 1970
# print(now_time)

curr_time_p = datetime.datetime.fromtimestamp(time.time())  # 把时间戳转换为日期格式
print(curr_time_p)

CUR_TIME = curr_time_p.strftime('%Y-%m-%d %H:%M:%S')  # %H:%M:%S = %X
print(CUR_TIME, type(CUR_TIME))