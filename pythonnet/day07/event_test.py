from threading import Event

#创建事件对象
e = Event()

e.set()#设置e,使wait结束阻塞
e.clear()#清除set状态
print("是否阻塞状态:",e.is_set())
e.wait(3)   #默认是阻塞的  输入3是超时事件3秒

print("888888888888888")
