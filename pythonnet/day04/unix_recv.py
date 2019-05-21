#服务端
from socket import *
import os

#确定套接字文件
sock_file = './sock'#当前目录下sock为套接字文件,名字可以随便取

if os.path.exists(sock_file):#判断sock_这个文件是否存在
    os.remove(sock_file)#删除sock_文件
#创建本地套接字
sockfd = socket(AF_UNIX,SOCK_STREAM)

#绑定套接字文件
sockfd.bind(sock_file)

#监听,链接
sockfd.listen(3)
while True:
    c,addr = sockfd.accept()
    while True:
        data = c.recv(1024)
        if not data:
            break
        print(data.decode())
    c.close()
sockfd.close()

