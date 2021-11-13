"""
描述
输入一个int型整数，按照从右向左的阅读顺序，返回一个不含重复数字的新的整数。
保证输入的整数最后一位不是0。
输入描述：
输入一个int型整数

输出描述：
按照从右向左的阅读顺序，返回一个不含重复数字的新的整数
"""
n = input()
a = list(n[::-1])
data = list({}.fromkeys(lis).keys())
c = int(''.join(data))
print(c)
