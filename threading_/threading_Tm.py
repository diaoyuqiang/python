#!/usr/bin/env python
# -*- coding: utf-8 -*-
import threading
import time

count = 0

# Time定时器任务
def show_time():
    global count
    if count < 10:
        print("time:", time.ctime())
        count += 1
        time_task()
    else:
        print("Done")


def time_task():
    t = threading.Timer(10, show_time)
    t.start()

time_task()
