"""
描述
实现删除字符串中出现次数最少的字符，若多个字符出现次数一样，则都删除。输出删除这些单词后的字符串，字符串中其它字符保持原来的顺序。
注意每个输入文件有多组输入，即多个字符串用回车隔开
输入描述：
字符串只包含小写英文字母, 不考虑非法输入，输入的字符串长度小于等于20个字节。

输出描述：
删除字符串中出现次数最少的字符后的字符串。
"""
import sys
"""
'abfdbag'
"""


def del_min_sr(sr):
    # 字符对应出现次数的字典
    dic_sr = {}
    # sys.maxsize: py中数据类型变量的最大值
    minsr = sys.maxsize
    # 出现次数最少的字符列表
    lsr = []
    for i in sr:
        if dic_sr.get(i) != None:
            dic_sr[i] += 1
        else:
            dic_sr[i] = 1

    for a in dic_sr.keys():
        minsr = min(minsr, dic_sr.get(a))

    for vo in dic_sr.keys():
        if dic_sr[vo] == minsr:
            lsr.append(vo)
    for re in lsr:
        sr = sr.replace(re, '')
        if sr == '':
            print("字符串中所有字符出现的次数相同，删除全部")
    return sr


while True:
    try:
        _sr = input("请输入字符串: ").split(r'\r')
        print(_sr)
        for i in _sr:
            print(del_min_sr(i))

    except EOFError as e:
        print(e)  # ctrl+D:退出指令错误

        break
