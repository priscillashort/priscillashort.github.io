import timeit

"""
    Timing the del operator for lists and dictionaries and comparing
"""

def testListDel():
    for i in range(len(l)):
        del l[len(l)-1]

def testDictDel():
    for i in range(len(d)):
        del d[len(d)-1]

print("          list             dict")
t1 = timeit.Timer("testListDel()", "from __main__ import testListDel")
t2 = timeit.Timer("testDictDel()", "from __main__ import testDictDel")
for i in range(100000,2000001,100000):
    l = list(range(1000))
    time1 = t1.timeit(number=i)
    d = {}
    for i in range(1000):
        d[i] = i
    time2 = t2.timeit(number=i)
    print("%15.5f, %15.5f" %(time1,time2))


    
