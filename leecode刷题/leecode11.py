"""
统计字符 a 在字符串中出现的次数；
统计字符 a 在字符串0到15索引范围内出现的次数。
"""


str1 = 'Fasten your seatbelts. It is going to be a bumpy night.'


def count(_str):
    return _str.count('a'), _str.count('a', 0, 15)  # str.count() 返回字符在源串中出现的次数


data = count(str1)
print(data)