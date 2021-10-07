import xml.sax


class Peision(object):

    def __init__(self, name, age):
        self.name = name
        self.age = age

    def __str__(self):
        return "persion name {s.name} persion age {s.age}".format(s=self)  # 重写str方法，返回对象属性的字符串


class MyXml(xml.sax.ContentHandler):

    def __init__(self):
        self.persion = []

    def startElement(self, tag, attrs):  # attrs为标签属性
        # 获取persion标签的属性
        if tag == "persion":
            # print(tag, attrs["name"], attrs["age"])
            self.persion.append(Peision(attrs["name"], attrs["age"]))


if __name__ == "__main__":

    parser = xml.sax.make_parser()
    parser.setFeature(xml.sax.handler.feature_namespaces, 0)  # 关闭命名空间解析
    handler = MyXml()
    parser.setContentHandler(handler)
    parser.parse("stu1.xml")

    for i in handler.persion:  # 遍历persion属性列表
        print(i)