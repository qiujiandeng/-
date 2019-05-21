from socket import *
from threading import Thread

HOST = '0.0.0.0'
PORT = 8888
ADDR = (HOST,PORT)

def handle(c):
    print("Connect from",c.getpeername())
    while True:
        data = c.recv(1024)
        if not data:
            break
        print(data.decode())
        c.send(b"OK")
    c.close()

#创建监听套接字
s = socket()
#设置套接字类型,可端口重用
s.setsockopt(SOL_SOCKET,SO_REUSEADDR,1)
#绑定服务器地址
s.bind(ADDR)
#监听套接字
s.listen(3)

#循环等待客户端连接
while True:
    try:
        #客户端名字,地址  =  s套接字连接的客户端
        c,addr = s.accept()
    except KeyboardInterrupt:
        s.close()
        break
    except Exception as e:
        print(e)
        continue
    
    #创建线程处理客户端请求,args把客户端传给handle函数处理
    t = Thread(target=handle,args=(c,))
    t.setDaemon(True)  #让分支线程随住线程退出
    t.start()
