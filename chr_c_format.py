import os.path

print(chr(65))
print('字符:%c' % 65)  # %c: 相当于chr()
print("uu%s" %("who %s" % "bbb"))

import glob

sr = os.path.join('./', '_li*.py')
print(sr, type(sr))
# glob.glob(): 返回所有匹配的文件路径列表（list）
print(glob.glob(os.path.join('./', '_li*.py')))  # os.path.join()函数用于路径拼接文件路径