import zipfile  # 压缩解压zip文件

# 解压zip文件
def unzip_file(zip_file, base_path):
    try:
        zfile = zipfile.ZipFile(zip_file, 'r')  # 创建zipfile对象
        print("zip文档中的文件列表:", zfile.namelist())  # 获取zip文档内所有文件的名称列表
        for filename in zfile.namelist():
            data = zfile.read(filename)  # 取zip文档内指定文件的二进制数据
            final_file_path = base_path + '/' + filename
            print('保存路径:{}'.format(final_file_path))
            with open(final_file_path, "wb") as f:
                f.write(data)
        return True
    except Exception as e:
        print('unzip file error:{}'.format(e))
        return False

zip_file = 'ActionRequest.zip'
base_path = '.'
if unzip_file(zip_file, base_path):
    print("success")