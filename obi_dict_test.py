class AttrDict(dict):  # 对象属性字典

    def __setattr__(self, key, value):
        self.__setitem__(key, value)

    def __getattribute__(self, item):
        return self.__getitem__(item)

    def __delattr__(self, item):
        self.__delitem__(item)