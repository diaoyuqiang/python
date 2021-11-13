"""
描述
密码要求:
1.长度超过8位
2.包括大小写字母.数字.其它符号,以上四种至少三种
3.不能有相同长度大于2的子串重复

输入描述：
一组或多组长度超过2的字符串。每组占一行
输出描述：
如果符合要求输出：OK，否则输出NG
"""
import re


def check(sr):
    if len(sr) <= 8:
        return False
    else:
        sub = []
        for i in range(len(sr)-2):
            sub.append(sr[i:i+3])
        if len(set(sub)) < len(sub):
            return False
        ty = 0
        upper = '[A-Z]'
        lower = '[a-z]'
        num = '\\d'
        chars = '[^A-Za-z0-9]'
        lis = [upper, lower, num, chars]
        for vo in lis:
            tru = re.search(vo, sr)
            if tru:
                ty += 1
        return True if ty >= 3 else False


while True:
    try:
        sr1 = input()

        print('OK' if check(sr1) else 'NG')

    except (EOFError, KeyboardInterrupt):
        break


