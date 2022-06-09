class X(object):
	def __init__(self, a, b, range):
		self.a = a
		self.b = b
		self.range = range
	# 将实例对象向函数一样调用，可以改变对象属性
	def __call__(self, a, b):
		self.a = a
		self.b = b
		print('__call__ with （{}, {}）'.format(self.a, self.b))

xdata = X(1, 2, 3)
xdata(2, 4)