'''
ftp 文件服务器
fork server训练
'''

from socket import *
import os,sys
import signal
import time
#全局变量
HOST = '0.0.0.0'
PORT = 8889
ADDR = (HOST,PORT)
FILE_PATH = '/home/tarena/qiu/kehoulianxi/'

class FtpServer(object):
    def __init__(self,c):
        self.c = c

    #查看文件列表函数
    def do_list(self):
        #获取文件列表
        file_list = os.listdir(FILE_PATH)
        if not file_list:
            self.c.send("文件库为空".encode())
            return
        else:
            self.c.send("OK".encode())
            time.sleep(0.1)
        
        files = ""
        for file in file_list:
            if file[0] != '.' and os.path.isfile(FILE_PATH+file):
                files = files + file + ','
        #讲拼接好的字符串传给客户端
        self.c.send(files.encode())
       

    #下载文件列表函数
    def do_get(self,filename):
        try:
            fd = open(FILE_PATH+filename,'rb')
        except IOError:
            print(filename)
            self.c.send("文件不存在".encode())
            return
        else:
            self.c.send(b'OK')
            time.sleep(0.1)
        #发送内容
        while True:
            data = fd.read(1024)
            if not data:
                time.sleep(0.1)
                self.c.send(b'##')
                break
            self.c.send(data)

    #上传文件
    def do_put(self,filename):
        #判断文件是否存在
        if os.path.exists(FILE_PATH + filename):
            self.c.send("该文件已存在".encode())
            return
        fd = open(FILE_PATH + filename,'wb')
        self.c.send("OK".encode())
        while True:
            data = self.c.recv(1024)
            if data == b'##':
                break
            fd.write(data)
        fd.close()
        print(filename,",文件已上传完成")

        
        


def do_request(c):
    ftp =FtpServer(c)
    print("客户端:",c.getpeername())
    while True:
        data = c.recv(1024).decode()
        if not data or data[0] == 'Q':
            c.close()
            return
        if data[0] == 'L':
            ftp.do_list()
        elif data[0] == 'G':
            filename = data.split(' ')[-1]
            ftp.do_get(filename)
        elif data[0] =='P':
            filename = data.split(' ')[-1]
            ftp.do_put(filename)

#网络搭建
def main():
    s = socket()
    s.setsockopt(SOL_SOCKET,SO_REUSEADDR,1)
    # global ADDR
    s.bind(ADDR)
    s.listen(5)

    #处理僵尸进程
    signal.signal(signal.SIGCHLD,signal.SIG_IGN)
    print("Listen to the port 8888....")
    #循环等待客户端连接
    # print("客户端:",c.getpeername())
    while True:
        try:
            c,addr = s.accept()
        except KeyboardInterrupt:
            sys.exit("服务器退出")
        except Exception as e:
            print("Error:",e)
            continue
        #创建子进程处理客户端请求
        pid = os.fork()
        if pid == 0:
            s.close()
            #此函数执行操作
            do_request(c)
            os._exit(0)
        #无论是父进程或者创建失败都是循环接收新的连接
        else:
            c.close()
        







if __name__ == '__main__':
    main()