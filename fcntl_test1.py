#!/usr/bin/env python
# -*- coding: utf-8 -*-
# import fcntl  # linux系统下排他锁fcntl.LOCK_EX 共享锁fcntl.LOCK_SH 非阻塞锁fcntl.LOCK_NB 模块

file = r'E:\time.txt'
f = open(file, 'w')
# fcntl.flock(f.fileno(), fcntl.LOCK_EX|fcntl.LOCK_NB)  # 排它锁 | 非阻塞锁: 未获取到锁直接退出函数， 不会阻塞
print(f.name, '-', f.fileno())  # 文件名称 文件描述符
f.write('somthing')
# fcntl.flock(f.fileno(), fcntl.LOCK_UN)  # 解锁
f.close()