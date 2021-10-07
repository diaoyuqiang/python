from io import StringIO
from io import BytesIO


# 字符IO: StringIO 读取 --write():写入内存  getvalue()：获取内存
with StringIO() as src:
    _len = src.write("hello world")  # 将内容写入内存，返回写入长度,并用变量接收
    # print(_len)
    data = src.getvalue()  # 从内存获取数据
    print(data)

# 字节IO: ByteIO(file like Object)  二进制写入
with BytesIO() as bio:
    len1 = bio.write("hello 中国".encode("utf-8"))  # 将内容写入内存，返回写入长度,并用变量接收
    # print(len1)
    data = bio.getvalue() # 从内存获取数据
    print(data.decode("utf-8"))

# 读取文件内容到内存，从内存写入到文件
with open(r"E:\pythonjob\pythonProject\learn\函数\text", "r", encoding="utf-8") as src, StringIO() as sio:
    size = 10
    while True:
        data = src.read(size)  # 读取文件内容
        if not data:
            break
        len2 = sio.write(data)  # 写入内存
    sda = sio.getvalue()  # 获取内存中的数据
    print(sda)

with open(r"E:\pythonjob\pythonProject\learn\函数\text_copy", "w", encoding="utf-8") as wri, StringIO(sda) as sio1:
    while True:
        data = sio1.read(size)  # 读取内存中的数据
        if not data:
            break
        wri.write(data)  # 将内存中读取的数据写入文件中



