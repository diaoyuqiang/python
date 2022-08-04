class Tree():
    def __init__(self, name):
        self.name = name

    def __str__(self):
        return "obj:{}".format(self.name)


def run(n):
    return Tree(n)


lis = ["a", "b", "c"]

d = {run(i): i for i in lis}

for tex in d.keys():
    print(tex)