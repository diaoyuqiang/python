def test(a: int = 5, b: int = 7) -> pow(2, 3):  # : 定义参数格式 | ->: 定义返回值，或者类型
    z = lambda x, y: x * x if x > y else y * y
    return z(a, b)


print(test.__annotations__)  # 打印变量、类属性、函数的形参或返回值指定预期的类型。
print(test())


def test1(a: int = 5, b: str = "default") -> str:  # : 定义参数格式 | ->: 定义返回值，或者类型
    return str(a) + b


print(test1.__annotations__)  # 打印变量、类属性、函数的形参或返回值指定预期的类型。
print(test1(123, "test"))
print(test1())
