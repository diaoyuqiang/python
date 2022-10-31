#!/usr/bin/env python
# -*- coding: utf-8 -*-
import datetime
import time

diff_tm = datetime.timedelta(seconds=60)  # 两个日期或者时间的差值
print(diff_tm, type(diff_tm))
print(datetime.datetime.now().replace(year=2021, microsecond=0))  # 替换datetime对象中的值
# print(type(datetime.datetime.now()))
# print(str(diff_tm).split(':', 1)[0])
now_time_float = time.time()
now_time = datetime.datetime.fromtimestamp(now_time_float)  # 根据时间戳获取时间
