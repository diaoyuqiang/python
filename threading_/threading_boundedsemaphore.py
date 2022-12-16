#!/usr/bin/env python
# -*- coding: utf-8 -*-
import threading
import time
t_l = []

s = threading.BoundedSemaphore(3)  # 控制最多线程并发量

def run(n):
    with s:
        print("running")
        time.sleep(n)

    # s.release()  # boundedsemaphore过多释放会报错


if __name__ == "__main__":
    for n in range(10):
        t_l.append(threading.Thread(target=run, args=(n, )))

    for i in range(10):
        t_l[i].start()
    # a = False
    # def test():
    #     assert a, "not"
    #     print("okk")
    #
    # test()