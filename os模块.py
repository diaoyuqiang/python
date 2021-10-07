import os
from os import getenv

# 获取系统环境变量
# e = os.environ
# print(e.get("path"))

# 查看、创建、删除目录
print(os.listdir(r"E:\pythonjob\pythonProject"))  # 查看指定目录下的文件,返回文件列表
# os.mkdir(r"E:\pythonjob\pythonProject\test")  # 创建目录
# if os.path.exists(r"E:\pythonjob\pythonProject\test"):
#     os.rmdir(r"E:\pythonjob\pythonProject\test")  # 删除指定的目录

# 查看文件路径
print(os.path.split(r"E:\pythonjob\pythonProject\learn\函数\_open.py"))  # 获取路径和文件的元祖
print(os.path.abspath(__file__))  # 查看此文件的绝对路径

# 重命名文件
# os.rename("list.txt", "_list.py")
# 删除文件
# os.remove("_list.py")

# 复制文件
os.system("copy _list.py list1.py")  # 给出复制提示
