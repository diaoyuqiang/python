def block_read(f_ph):

    block_size = 1024

    with open(f_ph, "r") as f:
        while True:
            block = f.read(block_size)

            if block:
                yield block  # 返回生成器对象
            else:
                break


data = block_read("text")

for i in data:  # 遍历读取的内容
    print(i)