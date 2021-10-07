"""
reversal 函数接受一个字典类型的 src 参数，
表示 长链接 到 短链接 的映射关系表。在函数体中编写代码，
实现 src 字典的 key 和 value 的调换，并返回新的字典。
"""

dict1 = {'https://lintcode.com/problems/design-tinyurl': 'http://tinyurl.com/4e9iAk', 'baidu': 'set'}


def reversal(src):
    res = dict()
    data = src.items()
    print(data)
    for i in data:
        x, y = i
        res.setdefault(y, x)
    return res


result = reversal(dict1)
print(result)

