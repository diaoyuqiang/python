score = 60
# python实现switch字典
switch = {
    90: lambda : print("x"),
    60: lambda : print("r")  # lambda不带参数的匿名打印函数
}

switch[score]()

# python实现switch
class Switch(object):
    def __init__(self, value):
        self.value = value
        self.fall = False

    def __iter__(self):
        yield self.match
        try:
            raise StopIteration
        except StopIteration:
            return

    def match(self, *args):  # 匹配函数
        if self.fall or not args:
            return True
        elif self.value in args:
            return True
        else:
            return False

v = "ten"
for case in Switch(v):
    if case("one"):
        print("1")
        break

    if case("ten1"):
        print("10")
        break

    if case():
        print("something else")
        # break

# python *arg:将参数打包成元祖 **kwargs:打包成dict
def run(*args):
    a = False
    b = "ten"
    if a or b in args:
        print(args)
        return True

print(run("ten"))