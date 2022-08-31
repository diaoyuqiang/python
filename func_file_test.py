with open('func_123.txt', 'rb') as f:
    """
    fileObject.seek(offset[, whence])
    offset – 开始的偏移量，也就是代表需要移动偏移的字节数，如果是负数表示从倒数第几位开始。
    whence：可选，默认值为 0。给 offset 定义一个参数，表示要从哪个位置开始偏移；0 代表从文件开头开始算起，1 代表从当前位置开始算起，2 代表从文件末尾算起。
    """
    f.seek(-3, 2)  # 移动文件指针到指定位置
    print(f.read(1))
