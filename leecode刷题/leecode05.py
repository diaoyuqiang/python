dc = {'name': 'dyq', 'age': 15, 'time': '2021', 'sex': 0}


def dict_del(dict_in):
    dict_in.popitem()  # 删除字典中的最后一项, py3.6以后字典有序
    return dict_in


result = dict_del(dc)
print(result)
