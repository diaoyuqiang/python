import json

# 自定义字典类
class AttrDict(dict):
    def __setattr__(self, key, value):  #设置实例属性
        self.__setitem__(key, value)  # 键值存储
    def __getattr__(self, item):  # 实例属性查找
        return self.__getitem__(item)  # 实例对象a[key]取值法

    def __delattr__(self, item):  # 删除实例属性
        self.__delitem__(item)  # 键值删除

# 自定义异常类
class FormatterError(AssertionError):
    """消息格式不符合要求"""

    def __str__(self):
        return "消息格式不符合要求"


# 自定义枚举类
class MessageTypeEnum():
    """
    自定义枚举类...python2 中枚举类必须用value获取值
    """
    # 上线
    OnLine = "OnLine"
    # 下线
    OffLine = "OffLine"


class MessageBase():
    Message = dict(
        # 消息来源
        source=None,
        id=None,
        messageType=None,
        result=None,
        data=None,
        errorMessage=None
    )

    def formatter(self, data):
        """
        message序列化格式化器
        """
        json_data = json.loads(data)
        for key in json_data.keys():
            if key not in self.Message.keys():
                raise FormatterError()  # 抛出自定义异常
        return AttrDict(json_data)


if __name__ == "__main__":
    dic = {"name": "dyq", "age": 18}
    t = AttrDict(dic)
    print(t["name"], t.age)  # 同时支持字典取值法和对象取值法