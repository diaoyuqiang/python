import shutil  # 文件操作模块

# 文件复制
# shutil.copyfile(r'text',r'text_shutil')  # 复制文件
# shutil.copy('text', 'text_shutil1')  # 复制文件到文件或目录，改变元信息
# shutil.treecopy('','')  # 拷贝目录

# 复制文件对象
src = open('text', 'r', encoding='utf-8', errors='ignore')
des = open('text_shutil1', 'w', encoding='utf-8', errors='ignore')
shutil.copyfileobj(src, des)

# 移动文件
# shutil.move('text_shutil1', r'E:\pythonjob\pythonProject')

# 删除文件或目录
# shutil.rmtree('text_shutil')

# 压缩解压缩
# shutil.make_archive('压缩文件名', 'zip', r'E:\pythonjob\pythonProject\plane')  # 压缩
# shutil.unpack_archive(r'E:\pythonjob\pythonProject\plane\压缩文件名.zip')  # 解压缩
