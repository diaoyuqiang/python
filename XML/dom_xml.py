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
    # 创建节点person
    n_person = doc.createElement("person")
    # 创建节点name
    n_name = doc.createElement("name")
    # 创建name的文本节点
    n_name.appendChild(doc.createTextNode(i["name"]))
    # 创建节点age
    n_age = doc.createElement("age")
    # 创建age的文本节点
    n_age.appendChild(doc.createTextNode(str(i["age"])))

    # 将name,age节点添加到person节点
    n_person.appendChild(n_name)
    n_person.appendChild(n_age)
    # 将person节点添加到root
    root.appendChild(n_person)

# 5.写出xml文档
with open("people_create.xml", "w", encoding="utf-8") as f:
    doc.writexml(f, indent="\n", addindent="\t", encoding="utf-8")
