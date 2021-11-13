import sys, importlib

# print(sys.argv)  # 命令行参数列表，第一个元素为程序路径
print(sys.getdefaultencoding())  # 获取当前解释器的默认编码方式

importlib.reload(sys)  # python3中重载模块