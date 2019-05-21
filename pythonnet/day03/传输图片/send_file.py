#作为客户端,发送端
from socket import *

s = socket()#创建套接字
s.connect(('127.0.0.1',8888))#绑定服务段地址和端口

f = open('/home/tarena/qiu/2019年富华里业绩表台账（新）3.28.xlsx','rb')#打开需要传输的文件,方式是读和二进制打开

while True:
    data = f.read(1024)#发送f文件,每次发送大小1024b
    if not data:#f文件完全读完,显示为空就是发送完了,关闭循环
        break
    s.send(data)#发送data的消息给服务端

f.close()#关闭文件
s.close()#关闭套接字
