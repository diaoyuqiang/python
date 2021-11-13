"""
•连续输入字符串，请按长度为8拆分每个输入字符串并进行输出；
•长度不是8整数倍的字符串请在后面补数字0，空字符串不处理。

输入描述：
连续输入字符串(输入多次,每个字符串长度小于等于100)

输出描述：
依次输出所有分割后的长度为8的新字符串
"""


# 递归方法
def deal(sr):
    if len(sr) > 8:
        print(sr[0:8])
        deal(sr[8: len(sr)])
    if len(sr) <= 8:
        a = '{:0<8}'.format(sr)
        print(a)


while True:
    try:
        _sr = input('')
        deal(_sr)
    except (EOFError, KeyboardInterrupt):
        break