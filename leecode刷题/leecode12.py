"""
遍历打印字典的key value
"""

dict1 = {'Name': 'Make', 'Age': 77, 'Class': 'First'}


def access_dict(dc):
    for key, value in dc.items():
        print(f'{key}: {value}')  # 格式化字符串，{}变量引用


access_dict(dict1)