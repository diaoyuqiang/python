# 二进制形式拷贝文件 (边读边写)

def copy(src_ph, end_ph):
    # 读取流，写出流
    with open(src_path, "rb") as src, open(end_path, "wb") as end:
        # 边写边读
        size = 1024
        while True:
            data = src.read(size)
            if not data:
                break
            end.write(data)


# r: 保留原格式
src_path = r"E:\pythonjob\pythonProject\learn\函数\text"
end_path = r"E:\pythonjob\pythonProject\learn\函数\text_copy"

# 调用函数，复制文件
copy(src_path, end_path)