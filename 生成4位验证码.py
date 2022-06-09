from threading_ import Timer
import random


# 生成4位随机密码，并进行验证
class Code(object):

    def __init__(self):
        self.code_cache()  # 创建对象时，调用加载验证码的方法

    # 加载生成验证码的方法
    def code_cache(self, second=10):

        self.cache = self.code_make()  # 接收生成的验证码
        print(self.cache)
        self.data = Timer(second, self.code_cache)  # 创建定时器对象(每10s执行一次加载验证码的方法)
        self.data.start()  # 启动定时器

    # 立刻加载验证码
    def code_current(self):
        self.code = self.code_make()
        print(self.code)

    # 生成验证码的方法
    def code_make(self, n=4):

        res = ''
        for i in range(n):
            s1 = str(random.randint(0, 9))  # 生成0-9的字符
            s2 = chr(random.randint(65, 90))  # 生成A-Z的字符
            t = random.choice([s1, s2])  # 选择seq中的任意元素
            res += t

        return res

    def code_ck(self):

        while True:
            msg = input(">>:")
            if msg.upper() == self.cache:  # 如果用户输入等于验证码
                print("验证成功!")
                self.data.cancel()  # 取消定时器
                break
            else:
                self.code_current()  # 调用立刻加载验证码的方法


if __name__ == '__main__':

    code = Code()
    code.code_ck()  # 调用检验验证码的方法



