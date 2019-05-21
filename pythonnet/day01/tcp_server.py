import socket

#创建套接字
sockfd = socket.socket(socket.AF_INET,socket.SOCK_STREAM)

#绑定地址
sockfd.bind(('127.0.0.1',8889))

#设置监听
sockfd.listen(5)

#等待处理客户端连接
print('Waitting for connect....')
connfd,addr = sockfd.accept()
print("Connect from",addr)   #客户端地址

#收发消息
while True:
    data = connfd.recv(1024)
    aa =data.decode()
    if aa == 'close':
                #等待处理客户端连接
        print('Waitting for connect....')
        connfd,addr = sockfd.accept()
        print("Connect from",addr)   #客户端地址
        data = connfd.recv(1024)
        aa =data.decode()

    print('Receive message:',data.decode())
    n = connfd.send(b"Receive yout message!!")  #b只能是英文,中文的话要用decode()
    print("Send %d bytes"%n)
    

#关闭套接字
connfd.close()
sockfd.close()
print('断开连接')



