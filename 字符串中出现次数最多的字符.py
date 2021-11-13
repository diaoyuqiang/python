import string
sr = 'aagggteeookkkkppaa'
# dic = {'a': '1', 'c': '2', 'dyq': '3'}
# a = dic.items()
print(max(sr, key=sr.count))


# 1.字典方法
def long_sr(sr_):
    dic = {}
    lis = []
    for i in set(sr_.lower()):
        dic[i] = sr_.count(i)
    a = max(dic.values())

    for x, v in dic.items():
        if v == a:
            lis.append(x)
    return lis

# 2.max()
# def check_sio(text):
#
#     text = text.lower()
#     # 输出第一个出现次数最多的字符
#     return max(string.ascii_lowercase, key=text.count)  # string.ascii_lowercase 输出 'a-z'
