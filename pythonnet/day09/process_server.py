from socket import *
from multiprocessing import Process
import sys
import signal

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
    sys.exit(0)


#创建监听套接字
s = socket()
#设置套接字类型,可端口重用
s.setsockopt(SOL_SOCKET,SO_REUSEADDR,1)
#绑定服务器地址
s.bind(ADDR)
#监听套接字
s.listen(3)

#处理僵尸进程
signal.signal(signal.SIGCHLD,signal.SIG_IGN)

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
    
    #创建进程处理客户端请求,args把客户端传给handle函数处理
    p = Process(target=handle,args=(c,))
    p.daemon = True  #让子进程随主进程退出
    p.start()
