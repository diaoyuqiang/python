import glob  # 文件名模式匹配


# 匹配D:\python_job\目录下的所有文件(*通配符)
for name in glob.glob(r'D:\python_job\*'):
    print(name)

# ?: 匹配单个字符
for name in glob.glob(r'D\file?.txt'):
    print (name)

# [0-9]匹配
for name in glob.glob(r'D\*[0-9].*'):
    print(name)