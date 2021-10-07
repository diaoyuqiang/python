import xml.sax

# 2.创建一个解析xml的类，继承自xml.sax.ContentHandler
class MyHandler(xml.sax.ContentHandler):

    # 初始化对象属性
    def __init__(self):
        self.name = None
        self.age = 0
        self.current_tag = None  # 当前标签节点

    # 开始解析xml元素的方法
    def startElement(self, tag_name, tag_attrs):
        # 处理tag_name标签节点
        if tag_name == "name":
            self.current_tag = tag_name  # 当前节点为相应的标签

        if tag_name == "age":
            self.current_tag = tag_name

    # 结束解析xml元素的方法
    def endElement(self, tag_name):
        # 处理tag_name标签节点
        if tag_name == "name":
            print("person_nm:", self.name)

        if tag_name == "age":
            print("person_age:", self.age)

    # 获取xml内容的方法
    def characters(self, content):

        if self.current_tag == "name":
            self.name = content

        if self.current_tag == "age":
            self.age = content
            

if __name__ == "__main__":
    # 1.创建一个XML解析器: parser = xml.sax.make_parser()
    parser = xml.sax.make_parser()
    # 关闭命名空间解析
    parser.setFeature(xml.sax.handler.feature_namespaces, 0)  # 0 为关闭
    # 3.实例化解析对象
    handler = MyHandler()
    parser.setContentHandler(handler)  # 把xml实例对象放入内容控制器中
    # 4.解析的xml文档
    parser.parse("stu.xml")  # xml文件路径

