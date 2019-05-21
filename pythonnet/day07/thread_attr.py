from threading import Thread
from time import sleep


def fun():
    sleep(3)
    print("线程属性测试")

t = Thread(target=fun,name="Tarena")#也可以在这里设置线程名称

#线程名称
print("Thread name :",t.name)
print("Thread name :",t.getName())
t.setName('aaaa')
print("Thread name :",t.getName())


t.start()


#查看线程是否在生命周期
print("alive:",t.is_alive())
# t.join()
