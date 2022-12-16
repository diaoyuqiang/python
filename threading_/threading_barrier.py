#!/usr/bin/env python
# -*- coding: utf-8 -*-
import threading
import time

words = ["a", "12", "你好！", "春风十里", "一起向未来", "最后一个"]
show_time_list = []


class Show_Time(threading.Thread):
    def __init__(self, barrier, word=None):
        super().__init__()
        self.barrier = barrier
        self.word = word

    def run(self):
        self.barrier.wait()
        print(time.ctime() + "==>" + self.word)


def ok():
    print("I am OK!")

# action: 线程数量达到通过数调用的函数
barrier = threading.Barrier(3, action=ok)  # 线程栅栏，每次通过的线程数

for word in words:
    t = Show_Time(barrier, word)
    show_time_list.append(t)

for thread in show_time_list:
    thread.start()

for thread in show_time_list:
    thread.join()

print(time.ctime() + " All done!")
