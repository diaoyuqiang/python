# 注解(形参类型、返回值类型)
def demo(num:int, sr:str, n:'int>9'=10)->bool:
    print(num, sr, n)
    return True

demo(1, "dyq")

# TODO admin:dyq 高亮注释，可在project中查询
# 打印函数注解
print(demo.__annotations__)