import greenlet

def test1():
    print("执行test1")
    gr2.switch()
    print("结束test1")


def test2():
    print("执行test2")
    gr1.switch()
    print("结束test2")

#讲函数变为协程函数
gr1 = greenlet.greenlet(test1)
gr2 = greenlet.greenlet(test2)

gr1.switch()#执行协程1