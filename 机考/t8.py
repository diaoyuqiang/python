"""
输入描述：
先输入键值对的个数n（1 <= n <= 500）
然后输入成对的index和value值，以空格隔开

输出描述：
输出合并后的键值对（多行）
"""

n = int(input())
dic = {}
for i in range(n):
    sr = input().split()
    a, b = int(sr[0]), int(sr[1])
    dic[a] = dic.get(a, 0) + b

lis2 = sorted(dic.items(), key=lambda x: x[0])
for i in lis2:
    print(i[0], i[1])