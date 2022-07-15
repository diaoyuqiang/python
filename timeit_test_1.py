# import timeit
#
#
# def run(a):
#     if a == "a":
#         print "ok"
#     if a == "b":
#         print "ok"
#     if a == "c":
#         print "ok"
#
# def test(a):
#     if a == "a":
#         print "ok"
#     elif a == "b":
#         print "ok"
#     elif a == "c":
#         print "ok"
#
#
# t1 = timeit.timeit("run('d')", "from __main__ import run", number=10000)
# print t1
# t2 = timeit.timeit("test('d')", "from __main__ import test", number=10000)
# print t2