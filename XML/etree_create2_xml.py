import xml.etree.cElementTree as et
# 创建root根节点
root = et.Element("people")
# 创建root下的子节点
person_ele = et.SubElement(root, "person")
person_ele2 = et.SubElement(root, "person")

# 给子节点添加属性，一次性添加所有属性
person_ele.attrib = {"name": "小王", "age": "25"}
person_ele2.attrib = dict(name="小刚", age="30")  # 字典函数格式
# person_ele2.attrib = {"name": "小刚", "age": "30"}

# 创建root的xml树
tree = et.ElementTree(root)
# 写出xml文档
tree.write("etree_create2.xml", encoding="utf-8", xml_declaration=True)