from socket import *
#创建数据报套接字
sockfd = socket(AF_INET,SOCK_DGRAM)

#绑定地址
server_addr = ('0.0.0.0',8888)  #创建一个元组,保存地址和端口
sockfd.bind(server_addr)

#消息收发
while True:
    data,addr = sockfd.recvfrom(1024) 
    #addr 消息发送方的地址
    #data 接收到的内容
    print('Receive from %s : %s' % (addr,data.decode()))
    #收到消息后回发一条
    sockfd.sendto(b'Thanks for your msg',addr)

#关闭套接字
sockfd.close()



