from z3 import *  # 逆向运算

# 整数解单个、多个
a = Int("a")
b, c = Ints("b c")
# 有理数解单个、多个
t = Real("t")
f, g = Reals("f g")
# 位运算的bit类型
b1 = BitVec("b1", 8)
b2, b3= BitVecs("b2 b3", 16)

# 添加方程约束
s = Solver()
# 约束条件
equs = [a+b==10, a-b==2]
s.add(equs)
print(s.check())  # sat有解 unsat无解
print(s.model())  # 使方程成立的某个解