"""
输入描述：
输入一行没有空格的字符串。
输出描述：
输出 输入字符串 中范围在(0~127，包括0和127)字符的种数。
"""


def count_character(_str):
    string = ''.join(set(_str))  # 去重后以字符串的形式
    count = 0  # 开始计数
    for item in string:
        if 0 <= ord(item) <= 127:  # ASCII码范围要求
            count += 1  # 计数
    return count


sr = input()
print(count_character(sr))