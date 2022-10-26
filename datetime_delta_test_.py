#!/usr/bin/env python
# -*- coding: utf-8 -*-
import datetime

diff_tm = datetime.timedelta(seconds=60)  # 两个日期或者时间的差值
print(diff_tm, type(diff_tm))
# print(str(diff_tm).split(':', 1)[0])