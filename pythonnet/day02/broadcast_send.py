from socket import *
from time import sleep
#目标地址
dest = ('176.128.16.255',9998)
#创建套接字
s = socket(AF_INET,SOCK_DGRAM)
#设置可以发送接收广播
s.setsockopt(SOL_SOCKET,SO_BROADCAST,1)
#要发送的msg
data = '''
    *****************
     2.14  北京   雪
     往后余生,风雪是你
    *****************
'''

while True:
    try:
        sleep(2)
        s.sendto(data.encode(),dest)
    except KeyboardInterrupt:
        break
s.close()



