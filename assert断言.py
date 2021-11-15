def foo(s):
    n = int(s)
    assert n != 0, 'n is zero!'  # 断言:条件为真程序执行，条件为假抛出AssertionError: n is zero!
    return 10 / n


foo('0')
