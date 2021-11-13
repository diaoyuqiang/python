class Point:
    def __init__(self, x=0, y=0):
        self.x = x
        self.y = y
        
    # 析构函数 __del__ ，__del__在对象销毁的时候被调用
    def __del__(self):
        # 实例方法中调用类名
        class_name = self.__class__.__name__
        print(class_name, "销毁")


pt1 = Point()
pt2 = pt1
pt3 = pt1
print(id(pt1), id(pt2), id(pt3) )

# 删除对象的引用
del pt1
del pt2
del pt3