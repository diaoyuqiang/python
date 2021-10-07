"""
给定一个正整数 n，判断它是否是 2 的幂次方。
如果是，则返回 It's a power of two；否则，则返回 It's not a power of two。
"""
n = int(input())

flag = False
for i in range(0, n+1):

    if pow(2, i) == n:
        flag = True
        print('It\'s a power of two')
        break

if not flag:
    print('It\'s not a power of two')
