# a-z: 97-122
# A-Z: 65 90
# isalpha(): 判断字符串是否只有字母组成
# isdigit(): 判断字符串是否只有数字组成
# islower(): 检测字符串是否由小写字母组成
# isupper(): 检测字符串是否由大写字母组成

a = chr(ord('A')+1)  # ord: 返回字符对应的整数值   chr:返回整数对应的 ASCII 字符
print(a)

def run(a, *args):
    print(a)

run(1, 2, 3)
lis = {'a': 'v'}
import json
rr = json.dumps(lis, indent=4)  # 根据数据格式缩进显示
print(rr)
# print(json.loads(rr))
print(round(11.234, 2))
print(int(11.9))