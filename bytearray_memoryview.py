import time


for n in (100000, 200000, 300000):
    da = "x" * n
    start = time.time()
    b = da
    while b:
        b = b[1:]
    print("bytes", n, time.time()-start)

for n in (100000, 200000, 300000):
    da = "x" * n
    start = time.time()
    # memoryview: 返回给定obj的内存操作对象
    b = memoryview(bytearray(da, "utf8"))  # bytearray: 返回str的字节序列,(参数为整数返回对应长度的初始化数组)
    while b:
        b = b[1:]
    print("bytes", n, time.time()-start)