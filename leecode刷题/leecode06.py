"""
('Chinese', 'English', 'Math')
100
根据给定的序列和固定值生成新序列
"""

data = ('Chinese', 'English', 'Math')
val = 100


def create_dict(key, value):
    new_dc = dict.fromkeys(data, val)  # dict.fromkeys(iterable, value)  创建新字典
    return new_dc


_dict = create_dict(data, val)
print(_dict)
