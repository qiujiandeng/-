from socket import *

#创建套接字
sockfd = socket()

#发起连接
server_addr = ('127.0.0.1',8889)
sockfd.connect(server_addr)

#收发消息
while True:
    data = input('>>')
    sockfd.send(data.encode())
    if data == 'close':
        break
    data = sockfd.recv(1024)
    print("From server:",data.decode())
    

#关闭套接字
sockfd.close()
print("退出连接")