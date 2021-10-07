"""
将 str_1 中的所有 * 替换成 ^；
将 str_2 中的第一个 * 替换成 $。
"""

str1 = 'his * is teacher and her * is doctor, my * is basketball player'
str2 = 'No matter what * you do * in the future, you must be responsible for your *'


def redo(s1, s2):
    data1 = s1.replace('*', '^')
    data2 = s2.replace('*', "$", 1)  # 第三个参数为替换次数
    print(data1)
    print(data2)


redo(str1, str2)
