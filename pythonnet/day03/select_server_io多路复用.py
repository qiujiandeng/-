from select import select
from socket import *

#创建套接字做为关注的IO
s = socket()
s.setsockopt(SOL_SOCKET,SO_REUSEADDR,1)
s.bind(('0.0.0.0',8888))
s.listen(5)

#添加到关注列表
rlist = [s] #存放关注的等待处理的IO事件
wlist = [] #存放监听的要主动处理的IO事件
xlist = [] #存放如果发生异常需要我们出来的IO时间

while True:
    #监控关注的IO
    #select阻塞IO在这里,等三个列表中有任意一个IO准备就绪就返回值给对应的变量
    rs,ws,xs = select(rlist,wlist,xlist)#循环监控,处理完一个在回来等
    for r in rs:
        #s就绪, 有客户端请求链接
        if r is s:
            c,addr = s.accept()
            print('Connect from',addr)  #一直有客户端链接
            #将客户端连接套接字加入关注
            rlist.append(c)
        #表示某个客户端发消息则c就绪,s就是等待连接的套接字
        else:
            data = r.recv(1024)
            if not data:#如果客户端退出,等于空消息
                rlist.remove(r)#删除遍历的客户端r
                r.close()#关闭遍历的r客户端
                continue#退出,让程序继续运行
            print('Receive:',data.decode())
            # r.send(b"OK,Thanks")
            #当r放入wlist表示希望主动操作r这个IO
            wlist.append(r)

    for w in ws:
        w.send(b'OK,Thanks')
        wlist.remove(w)#处理完删掉,否者陷入死循环
        #当又有人给我们发消息还会重复以上步骤
        #用来主动处理准备好的IO让rlist可以在继续去监控准备就绪的IO

    for s in xs:
        pass

