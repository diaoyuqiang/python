#!/usr/bin/env python
# -*- coding: utf-8 -*-

sr = '\u5403\u9e21\u6218\u573a'  # unicode字符串
b = sr.encode('unicode-escape')  # 将unicode形式的str转成bytes类型
print(b)

c = b.decode('unicode-escape')  # 将unicode形式的bytes转成str类型
print(c)

# encode('raw_unicode_escape') 和 decode('raw_unicode_escape')  bytes形式的str转换

sr1 = '啊'
print(sr1.encode())

print(0x2e)  # 显示十进制数
print('\x2e')  # 显示对应的ascii字符