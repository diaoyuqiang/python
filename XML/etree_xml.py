import xml.etree.ElementTree as et
# 获取一个xml解析树
tree = et.parse("people_create.xml")

# 获取xml树的根节点
root = tree.getroot()

# 遍历xml树root的子节点
for p in root:
    # 添加新的的子节点，并设置文本内容
    # sex = et.Element("sex")
    # sex.text = "男"
    # p.append(sex)

    # 遍历person的子节点ele
    for ele in p:
        if ele.tag == "name":
            if ele.text == "小明":
                ele.text = "张三"  # 修改name标签的文本内容
                ele.attrib["no"] = "1001"  # 添加name标签的属性

            if ele.text == "小刚":
                ele.text = "李四"
                ele.attrib["no"] = "1002"

        # 删除节点
        if ele.tag == "age":
            p.remove(ele)

# 修改并重写xml树
tree.write("people_create.xml", encoding="utf-8", xml_declaration=True, short_empty_elements=False)