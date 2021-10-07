import xml.dom.minidom

# 1.在内存中创建一个空的文档
doc = xml.dom.minidom.Document()
# 2.创建一个跟节点
root = doc.createElement("people")
# 设置根节点属性
root.setAttribute("id", "people")
# 3.将根节点添加到文档中
doc.appendChild(root)

"""
4.创建子节点并添加到root
# 准备数据,循环创建子节点和文本节点
"""
data = [{"name": "小明", "age": 18}, {"name": "小刚", "age": 25}]

# 循环创建子节点和文本节点
for i in data:
    n_person = doc.createElement("person")
    # 设置person节点的属性
    n_person.setAttribute("name", i["name"])
    n_person.setAttribute("age", str(i["age"]))
    # 将person添加到root节点下
    root.appendChild(n_person)

# 学出xml文档
with open("people_create2.xml", "w", encoding="utf-8") as f:
    doc.writexml(f, indent="\n", addindent="\t", encoding="utf-8")