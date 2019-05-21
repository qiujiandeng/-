from socket import *
import struct #标准卡模块

#创建套节奏

s = socket(AF_INET,SOCK_DGRAM)#数据报套接字
s.bind(('0.0.0.0',8888))

#确定数据结构
st = struct.Struct('i16sf')

while True:
    data,addr = s.recvfrom(1024)
    #解析数据
    data = st.unpack(data)
    print(data)

s.close()
