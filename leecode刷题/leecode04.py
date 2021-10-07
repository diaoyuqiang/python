"""
请从标准输入流（控制台）中获取一个正整数 n，
要求从小到大输出区间 [1,n] 中，除了 3 的倍数以外的所有整数。你可以用 continue 语句来达到此目的。
"""

n = int(input("整数:"))

for i in range(1, n+1):
    if i % 3 == 0:
        continue
    print(i)
