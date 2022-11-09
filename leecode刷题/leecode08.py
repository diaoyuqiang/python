"""
给定一个只由大写字母组成的字符串 s，
按照字母表的中第 i 个字母变成第 (26 - i + 1) 个字母（如 A 变 Z），
变换字符串中的所有字母，通过 print 语句输出变换后的字符串到标准输出流（控制台）。
"""
"""
A-Z: 65-90
a-z: 97-122
"""
s = input('字母串:')

result = ''
for i in range(len(s)):
    # 得到 s[i] 的序号
    idx = ord(s[i]) - ord('a')  # ord()返回给定字符对应的ASCII值
    # 实现转换
    result += chr(25 - idx + ord('a'))  # chr() 返回当前整数对应的 ASCII 字符

print(result)