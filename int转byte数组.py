import struct

# int 转byte数组，有可能是4个字节，也可能是2个字节，或者一个字节
def intToBytes(value, length):
    byteList = struct.pack('>i', value)
    # print("byteList:", byteList)  # 字节字符串
    # python2 中使用
    # byteList_ord = [ord(t) for t in byteList]  # ord(i): 根据字节字符串, 返回对应的ascii数值
    # byteList_ord.reverse()  # 字节数组
    # result = [byteList_ord[i] for i in range(length)]
    # result.reverse()
    # return result

a = intToBytes(2, 4)
print(a)  # 16进制字节frame