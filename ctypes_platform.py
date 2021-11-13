import platform  # 访问平台属性
from ctypes import *

# print(platform.machine())  # 平台架构，不确定返回空字符串
# print(platform.system())  # 系统名称
# print(platform.platform(terse=True))  # 系统版本，terse=True: 最短识别信息
# print(platform.processor())  # 处理器名称


cdll_names = {
    'Darwin': 'libc.dylib',
    'Linux': 'libc.so.6',
    'Windows': 'msvcrt.dll'
}

# strcat:将'b'字符串追加到'a'，返回指向'a'的指针
clib = cdll.LoadLibrary(cdll_names[platform.system()])
s3 = clib.strcat('a', 'b')
print(s3)

# 指定类型
clib.strcat.restype = c_char_p
s4 = clib.strcat('c', 'd')
print(s4)


