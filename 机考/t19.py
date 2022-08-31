"""
当内容是英文字母时则用该英文字母的后一个字母替换，同时字母变换大小写,如字母a时则替换为B；字母Z时则替换为a；
当内容是数字时则把该数字加1，如0替换1，1替换2，9替换0；
其他字符不做变化。
3、解密方法为加密的逆过程。
本题含有多组样例输入。
输入描述：
输入说明
输入一串要加密的密码
输入一串加过密的密码

输出描述：
输出说明
输出加密后的字符
输出解密后的字符
"""

import sys

inttab = "abcdefghijklmnopqrstuvwxyzABCDEFGHIJKLMNOPQRSTUVWXYZ0123456789"
outtab = "BCDEFGHIJKLMNOPQRSTUVWXYZAbcdefghijklmnopqrstuvwxyza1234567890"
number = 1

for line in sys.stdin:
    # print(line)
    lis = line.split()
    for da in lis:
        s1 = ""
        s2 = ""
    # print(int(a[0]) + int(a[1]))
        if number % 2 == 1:
            for i in lis[0]:
                if i in inttab:
                    s1 += outtab[inttab.index(i)]
            print(s1)
        else:
            for i in lis[1]:
                if i in outtab:
                    s2 += inttab[outtab.index(i)]
            print(s2)
        number = number + 1