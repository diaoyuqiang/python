import gc

gc_status = gc.isenabled()  # 查看gc状态
print(gc_status)

gc.disable()  # 禁用gc
print(gc.isenabled())
gc.collect()  # 显式进⾏垃圾回收,可以输⼊参数,0代表只检查第⼀代的对象,1代表检查⼀,⼆代的对象,2代表检查⼀,⼆,三代的对象,如果不传参数,执⾏⼀个full collection,也就是等于传2