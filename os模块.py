import os
import json
from os import getenv

# 获取系统环境变量
# e = os.environ
# print(e.get("path"))

# 查看、创建、删除目录
print(os.listdir(r"D:\python_stu\lock"))  # 查看指定目录下的文件,返回文件列表
# os.mkdir(r"E:\pythonjob\pythonProject\test")  # 创建目录
# if os.path.exists(r"E:\pythonjob\pythonProject\test"):
#     os.rmdir(r"E:\pythonjob\pythonProject\test")  # 删除指定的目录

# 查看文件路径
print(os.path.exists(r'D:\python_stu\lock\lock_test.py'))  # 判断文件是否存在
print(os.path.split(r"D:\python_stu\lock\lock_test.py"))  # 获取路径和文件的元祖
print(os.path.abspath(__file__))  # 查看此文件的绝对路径

# 重命名文件
# os.rename("list.txt", "_list.py")
# 删除文件
# os.remove("_list.py")

# 复制文件
os.system("copy 1.txt test.txt")  # 给出复制提示

dic = {'name': 'dyq', 'age': 18
       }

with open('text', 'w') as f:
    json.dump(dic, f, ensure_ascii=False, indent=4, separators=(',', ': '))  # 默认输出ascii码，False输出中文; indent: 非0按照数据格式缩进
    os.fsync(f)  # 强制将带有文件描述符的文件写入磁盘
