import datetime
now = datetime.datetime.now()
stamp = [0x00] * 10  # 0x00: 16进制表示0

# 右移运算符: 把">>"左边的运算数的各二进位全部右移若干位，>> 右边的数字指定了移动的位数,补0, 再跟255与运算。
stamp[0] = now.year >> 8 & 0xff  # 0xff: 255, 11111111
print(now.year, stamp[0])

# &: 按位与运算(两个相应位都为1,则该位的结果为1,否则为0)
b = 5 & 1  # 5: 0000 0101  1: 0000 0001
print(b)
