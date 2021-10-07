"""
1.判断 str_in 是否以 Moon 作为开头
2.判断 str_in 从下标为 4 的字符开始是否以 light 开头
3.判断 str_in 下标从 10 到 12 的字符片段中是否以 in 开头(左闭右开)
"""

_str = 'Moonlight in front of the bed'


def check_str(da):
    return 'yes' if da.startswith('in', 10, 12) else 'no'


result = check_str(_str)
print(result)
