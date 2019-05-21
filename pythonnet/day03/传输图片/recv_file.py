from socket import *

s = socket() #创建套接字
s.bind(('127.0.0.1',8888)) #绑定地址和端口
s.listen(3)#监听3个大小

c,addr = s.accept()#接收到的文档,对方地址 接收
print('Connect from',addr)#打印连接到来至哪个地址

f = open('new_表格.xlsx','wb')#打开文件,方式是二进制byset写入文件

while True:
    data = c.recv(1024)#不知道图片和视频多大,最好一部分一部分接收
    if not data:#如果data消息为空
        break#结束循环
    f.write(data)#f 文件写入data

f.close()#关闭文件
c.close()#关闭接收
s.close()#关闭套接字