# 192.0.12.253 ip:4个8位二进制数组成(0-255)
def ip_int(ip_str):  # ip地址串转换为整数
    ip_long = 0
    for idx, val in enumerate(reversed([int(x) for x in ip_str.split('.')])):
        ip_long += val << (8*idx)
    return ip_long


a = ip_int('192.0.12.253')
print(a)


def ip(ip_long):  # 整数串转换为ip地址串
    lis = []
    l1 = ip_long >> 24
    l2 = (ip_long & 0X00FFFFFF) >> 16  # 0X00FFFFFF: 前8位为0，后24位为1
    l3 = (ip_long & 0X0000FFFF) >> 8
    l4 = (ip_long & 0X000000FF)
    lis.extend((l1, l2, l3, l4))
    return '.'.join(map(str, lis))


s = ip(3221228797)
print(s)