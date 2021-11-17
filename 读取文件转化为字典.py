# def dict_file(path):
#     try:
#         line = '_'
#         dic = {}
#         with open(path, 'r') as f:
#             for line in f:
#                 line = str(f.readline()).strip()
#                 if line.find('=') > 0 and not line.startswith('#'):
#                     k, v = line.split('=', 1)
#                     dic[k] = v
#         return dic
#     except Exception as e:
#         print(e)
#         return {}
#
#
# a = dict_file('config.txt')
# print(a)
dic = {}
with open('config.txt', 'r', encoding='utf8') as f:
    for line in f:
        sr = line.strip()
        if line.find('=') > 0 and not line.startswith('#'):
            k, v = sr.split('=', 1)
            dic[k] = v

print(dic)
