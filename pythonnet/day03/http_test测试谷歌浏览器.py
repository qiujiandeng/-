from socket import *

#创建套接字
s = socket()
#绑定地址和端口
s.bind(("0.0.0.0",8000))
#监听8000的端口
s.listen(3)


c,addr = s.accept() #接收浏览器连接
print("Connect from:",addr)
data = c.recv(4096) #浏览器发送请求
print(data.decode())

#组织http响应
data = '''HTTP/1.1 200 OK
Content-Type: text/html

<h1>hello world</h1>
'''
c.send(data.encode())#发送

c.close()
s.close()