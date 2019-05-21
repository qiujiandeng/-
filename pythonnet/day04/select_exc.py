#将终端输入和服务端的消息写入文件里
from select import select#导入select监控IO时间方法
from socket import *     #导入套接字方法
import sys               #导入系统终端模块
from time import ctime   #导入时间模块中的当前时间

s = socket()
s.bind(('0.0.0.0',8800))
s.listen(3)
#日志文件
f = open('log.txt','a')#a追加

#终端输入
rlist = [s,sys.stdin]#等待处理的准备好的IO事件
wlost = []#主动处理的IO时间
xlist = []#发生异常需要处理的IO时间

while True:
    rs,ws,xs = select(rlist,wlost,xlist)
    for r in rs:#循环rs对象里面有没有准备好的对象
        if r is s:#如果r里面有s(服务器)对象就处理:
            c,addr = r.accept()#接收客户端,地址
            rlist.append(c)#把客户端添加到rs中
        elif r is sys.stdin:#如果r等于终端输入
            f.write('%s   %s  '%(ctime(),r.readline()))#readline包含有\n
            f.flush()#刷新文件缓冲
        else:
            data = c.recv(1024)#否者用data来接收c客户端的数据,每次1024字节
            if not data:#如果data等于空
                rlist.remove(c)#删除c这个客户端
                r.close()#关闭r这个变量
                continue #继续运行
            f.write('%s    %s   \n'%(ctime(),data.decode()))#把消息写入文件
            f.flush()#刷新文件缓冲
