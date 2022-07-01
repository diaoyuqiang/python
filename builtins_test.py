import builtins

def test():
    print('--test--')

builtins.__dict__['new_test'] = test  # 向内置模块添加自定义函数，供其他模块使用

test()

if __name__ == "__main__":
    print(type(__builtins__))
    print('---------------分割线---------------------')
