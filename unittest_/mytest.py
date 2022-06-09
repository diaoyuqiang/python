import unittest

"""
测试类组成:setup(初始化)  testfun(测试方法)  tearDown(后置处理)
"""


# 创建测试类
class WebTest(unittest.TestCase):
    def setUp(self) -> None:  # 每个函数执行前都执行
        print("初始化1")

    @classmethod
    def setUpClass(cls) -> None:  # 整个测试类执行开始执行一次
        print("初始化2")

    def test_Myfunc1(self):
        print("运行1")

    def test_Myfunc2(self):
        print("运行2")

    def tearDown(self) -> None: # 每个函数执行后都执行
        print("结束1")

    @classmethod
    def tearDownClass(cls) -> None:  # 整个测试类结束执行一次去
        print("结束2")


if __name__ == '__main__':
    unittest.main()