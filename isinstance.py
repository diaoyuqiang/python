class A:
    pass


class B(A):
    pass

# isinstance(object, type) 相当于type(),区别：isinstance考虑类的继承。 obj类型等于type 返回True，否 False
# print(isinstance(B(), A)) True


x = ('10.105.1.190', '9001')


def _ip():
    if isinstance(x, tuple) and len(x) == 2:
        host, port = x
        mode = 'HTTP'

    elif isinstance(x, tuple) and len(x) == 3:
        host, port, mode = x

    print(host, port, mode)


# 获取ip
_ip()





