"""
IO :数据流读写操作
input/output stream

open(file,mode='r',buffering=1,encoding="GBK")
file:文件路径 r"/c/desktop/" --r保留路径格式
mode:操作方式 r w a rb wb ab
w:文件不存在，创建写入，存在会覆盖
a：文件不存在，创建写入，存在追加
二进制写入wb/ab："人生苦短，我学python".encode("utf-8") # 指定编码方式

buffering:读取大小
encoding:指定字符集

read() 默认全部读取
seek() 指定读取游标位置
tell() 获取当前游标位置
close() 先打开后关闭

序列化反序列化 rb:读取二进制
字符转字节，字节转字符
.decode("GBK", errors="ignore")
"""

data_list = []
SRC = open(r"C:\Users\19485\Desktop\learn\python\文件.txt", "r", encoding="utf-8")
print(type(SRC))  # IO包装的text
# while True:
#     DATA = SRC.read(2)
#     if not DATA:
#         break
#     data_list.append(DATA)
# print(data_list)
# SRC.close()

data = SRC.read()
for i in data:
    print(i.rstrip(), end="")  # 去除行末换行符

# readline() 一次读取一行
# readlines() 一次读取所有行,返回内容列表
