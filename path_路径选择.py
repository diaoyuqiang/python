import os
import sys

print(sys.path)  # python搜索模块的路径列表

fp = os.path.dirname(os.path.dirname(os.path.abspath(__file__))) # 当前文件上级目录
print(fp)