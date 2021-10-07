import xml.dom.minidom
# 获取xml文档树
dom_tree = xml.dom.minidom.parse("move.xml")
# 获取xml所有节点
root = dom_tree.documentElement
# 获取sitcom节点
sitcom = root.getElementsByTagName("sitcom")
for s in sitcom:
    title = s.getElementsByTagName("title")[0]  # 返回Nodelist 所以取索引
    print("电视剧名称是：", title.childNodes[0].data)  # 获取title标签的文本子节点的数据
    print("电视剧的导演是：", title.getAttribute("director"))  # 获取title标签的属性

    players = s.getElementsByTagName("players")[0]  # 返回Nodelist 所以取索引
    for p in players.childNodes:
        if isinstance(p, xml.dom.minidom.Element):  # 判断是否为元素标签
            print("演员是：", p.childNodes[0].data)  # 打印元素标签的子节点(文本标签)的数据
    print("*" * 30)

    desc = s.getElementsByTagName("desc")
    if desc:  # 判断是否有desc标签
        print(desc[0].childNodes[0].data)  # 获取desc的文本子节点的数据 .data 为对象的属性，取值
