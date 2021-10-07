import xml.etree.cElementTree as et
# 通过et.Element创建一个根节点
root = et.Element("people")

# et.SubElement创建子节点
person_element = et.SubElement(root, "person")
name_element = et.SubElement(person_element, "name")

# .text属性设置标签内容
name_element.text = "小明"
# 创建person的子节点age
age_element = et.SubElement(person_element, "age")
# .text属性设置标签内容
age_element.text = "18"

# 创建xml树
tree = et.ElementTree(root)
# 写出xml文档
# xml_declaration=True 是否需要xml声明
tree.write("etree_create.xml", encoding="utf-8", xml_declaration=True)
