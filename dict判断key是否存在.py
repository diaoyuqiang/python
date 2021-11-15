dic = {'name': 'admin', 'age': 18}


def run(k):
    return k in dic  # 返回bool类型


def ifo(k):
    if not run(k):
        dic[k] = k  # 不存在添加key-value


ifo('num')

print(dic)
