# 内置函数compile: 将字符串、字节串、ast节点编译成代码对象(pyCodeObject)或者ast抽象语法树(compile(source, filename, mode, PyCF_ONLY_AST))
# 参数: PyCF_ONLY_AST 返回ast抽象语法树

# compile(source, filename, mode): source->创建代码对象的源  filename: 指定参考文件  mode: 指定代码执行格式exec、eval和single
# 如果源包含多个python语句，请使用exec。 如果source是单个python表达式，请使用eval。 如果源由单个交互式语句组成，则使用单个。
code_str = 'x=5\ny=10\nprint("sum =",x+y)'
code = compile(code_str, 'compile_test.py', 'exec')
print(type(code))
exec(code)