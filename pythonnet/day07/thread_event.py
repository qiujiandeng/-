from threading import Thread,Event
from time import sleep

#用全局变量进行通信
s = None #全局变量,用于通信
e = Event()
def foo():
    #我要给主线程发一条消息
    print("Foo 前来拜山头")
    global s
    sleep(1)
    s = "天王盖地虎"
    e.set()#设置e.使wait结束阻塞

#把他变成分支线程
f = Thread(target=foo)
f.start()

#主线程验证口令
print("说对口令就是自己人")
e.wait()#添加阻塞.保证线程先运行
if s == "天王盖地虎":
    print("确认过眼神,你是对的人")
else:
    print("打死他")

f.join()