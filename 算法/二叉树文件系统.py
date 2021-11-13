class Node:  # 创建系统目录或文件节点
    def __init__(self, name, type="dir"):
        self.name = name
        self.type = type
        self.children = []
        self.parent = None
        # 链式存储方式

    def __repr__(self):
        return self.name


class FileSystem:
    def __init__(self):
        self.root = Node("/")  # 根目录/
        self.now = self.root  # 现节点（目录）

    def mkdir(self, name):
        # 目录以/结尾
        if name[-1] != "/":
            name += "/"
        node = Node(name)  # 创建子目录节点
        self.now.children.append(node)  # 添加到当前目录的子目录列表中
        node.parent = self.now  # 子目录的父节点为当前目录

    def ls(self):
        return self.now.children

    def cd(self, name):
        if name[-1] != "/":
            name += "/"
        if name == "../":
            self.now = self.now.parent  # 返回上级目录
            return
        for child in self.now.children:  # 查找子目录
            if child.name == name:
                self.now = child
                return  # 如果有，返回子目录

        raise ValueError("invalid dir")  # 没有抛出异常


tree = FileSystem()
tree.mkdir("var/")
tree.mkdir("bin/")
tree.mkdir("usr/")
tree.cd("bin/")
tree.mkdir("python/")
tree.cd("python/")
tree.cd("../")
print(tree.now)