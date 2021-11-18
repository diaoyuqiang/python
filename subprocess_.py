import subprocess

a = subprocess.getoutput('dir')  # 执行命令行参数，获取返回的字符串数据
print(a, type(a))
