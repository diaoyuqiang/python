import collections
import copy

dic = {
        "comment": 'null',
        "description": 1,
          "en": {"name": "dyq", "root": "admin"},
          "jp": 'null',
          "cn": "rcs服务器ip",
        "value":10
        }


# dic1 = copy.deepcopy(dic)
params_dict = collections.OrderedDict()  # 有序列表

params_dict[dic.get("en", {}).get("name")] = dic.get("value")


for i in params_dict.items():
    print(i)

