'''
遇到问题没人解答？小编创建了一个Python学习交流QQ群：531509025
寻找有志同道合的小伙伴，互帮互助,群里还有不错的视频学习教程和PDF电子书！
'''
class FatFather(object):
    def __init__(self, name):
        print('FatFather的init开始被调用')
        self.name = name
        print('调用FatFather类的name是%s' % self.name)

#胖子老板类 继承 FatFather 类
class FatBoss(FatFather):
    def __init__(self, name, hobby):
        self.hobby = hobby
        FatFather.__init__(self, name)   #直接调用父类的构造方法
        print("%s 的爱好是 %s" % (self.name, self.hobby))

def test():
    f_boss = FatBoss("胖子老板", "打斗地主")

if __name__ == '__main__':

    test()
