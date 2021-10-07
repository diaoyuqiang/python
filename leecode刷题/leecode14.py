"""
出给定商品列表中最贵的商品， 并以字符串形式返回该商品的名称。
如果给定商品列表的长度为 0 ，则返回 None。
"""
item = [
    {'name': 'Strawberry', 'price': 50},
    {'name': 'Apple', 'price': 100},
    {'name': 'banana', 'price': 20},
]


def search(src):

    if len(src) == 0:  # 当列表为空列表时，返回 None
        return None
    else:
        # lambda匿名函数重写key所代表的函数,指定可迭代对象中的元素的key的取值进行排序
        src.sort(key=lambda x: x['price'], reverse=True)  # reverse: 逆序
        l1 = src[0]
        return l1['name']


result = search(item)
print(result)