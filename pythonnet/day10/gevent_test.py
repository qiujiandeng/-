import gevent

def foo():
    print("Running  foo")
    gevent.sleep(3)
    print("Foo again")


def bar():
    print("Running bar")
    gevent.sleep(2)
    print("Bar again")


f = gevent.spawn(foo)
b = gevent.spawn(bar)
#如果没有joinall 两个函数都不执行
#阻塞到f,b两个函数执行完毕
gevent.joinall([f,b])