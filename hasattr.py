# hasattr():  查看类的实例对象中是否包含某属性或方法。


class Change():

    def __init__(self):
        self.name = 'dyq'
        self.age = '18'

    def say(self):
        print('hello world')


che = Change()
# 查看是否有name属性
if hasattr(che, 'name'):
    print(hasattr(che.name, '__call__'))  # name属性是否为可调用的对象
    
# 查看是否有say属性
if hasattr(che, 'say'):
    print(hasattr(che.say, '__call__'))  # say方法为可调用对象

