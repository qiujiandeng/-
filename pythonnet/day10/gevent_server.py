import gevent
from gevent import monkey
monkey.patch_all()  #此时执行脚本插件,修改所有阻塞行为,一定要在IO模块之前导入
from socket import *

#创建套接字
def server():
    s = socket()
    s.bind(('0.0.0.0',8888))
    s.listen(10)
    while True:
        c,addr = s.accept()
        print("Connect from",addr)
        # handle(c)  #用handle处理客户端请求 直接用函数不能连接多个客户端
        gevent.spawn(handle,c)#吧handle变成了协程方案
    
def handle(c):
    while True:
        data = c.recv(1024)
        if not data:
            break
        print(data.decode())
        c.send(b"OK")
    c.close()
server()
