from socket import *
s = socket()#创建套接字对象
#对套接字设置为可以立即重用端口,不用等
s.setsockopt(SOL_SOCKET,SO_REUSEADDR,1)
print(s.getsockopt(SOL_SOCKET,SO_REUSEADDR))
print(s.family)#地址类型
print(s.type)#套接字类型
s.bind(('176.128.16.20 ',8898))
print(s.getsockname())
print(s.fileno())  #获取文件描述符
s.listen(3)
c,addr = s.accept()
print(c.getpeername())#获取c对应的客户端地址