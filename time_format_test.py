#!/usr/bin/env python
# -*- coding: utf-8 -*-
# 格式化当前时间
import datetime

def nowTime(DateTimeFormat=None):
    if not DateTimeFormat:
        DateTimeFormat = "%Y-%m-%d %H:%M:%S"
    return (datetime.datetime.utcnow() + datetime.timedelta(hours=8)).strftime(DateTimeFormat)

print((datetime.datetime.utcnow() + datetime.timedelta(hours=8)).strftime("%Y-%m-%d %H:%M:%S.%f")[:-3]) # 微妙保留3位