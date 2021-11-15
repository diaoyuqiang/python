import ast

# 利用了ast的抽象语法树技术, 判断用户的字符串是否合法, 不合法就不让运行, 保障安全
da = '[1, 2, 3]'
res = ast.literal_eval(da)  # 目前只能做类型转化
print(res)


