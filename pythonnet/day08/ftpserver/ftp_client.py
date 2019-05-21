from socket import *
import os,sys,time

#具体功能
class FtpClient(object):
    def __init__(self,sockfd):
        self.sockfd = sockfd
    
    def do_list(self):
        self.sockfd.send(b"L")#发送请求
        #等待回复
        data = self.sockfd.recv(128).decode()
        if data == 'OK':
            data = self.sockfd.recv(4096).decode()
            files = data.split(',')
            for file in files:
                print(file)
        
        else:
            #无法完成操作
            print(data)
    
    def do_get(self,filename):
        self.sockfd.send(("G "+filename).encode())
        data = self.sockfd.recv(128).decode()
        if data == 'OK':
            fd = open(filename,'wb')
            while True:
                data = self.sockfd.recv(1024)
                if data == b"##":
                    break
                fd.write(data)
            fd.close()

        else:
            print("失败")


    def do_put(self):
        self.sockfd.send(b'P')#发送请求
        #等待回复
        data = self.sockfd.recv(128).decode()
        if data == 'mima':#设置一个服务器密码
            key = input("请输入服务器密码>>")
            self.sockfd.send(key.encode())
            #等待回复
            key1 = self.sockfd.recv(128).decode()
            if key1 == 'OK':
                wen_jian = input("请拉一个文件来>>")
                try:
                    fd = open(wen_jian.strip().split("'")[1],'rb')
                    # print(fd)
                    filename = wen_jian.strip().split("'")[1]
                    print(filename)
                    self.sockfd.send(filename.encode())
                except IOError as ii:
                    print("文件不存在",ii)
                    return
                while True:#发送文件
                    data = fd.read(1024)
                    if not data:
                        time.sleep(0.1)
                        self.sockfd.send(b"##")
                        break
                    self.sockfd.send(data)
            else:
                print("密码错误")
                return
        else:
            print(data)


    def do_quit(self):
        self.sockfd.send(b'Q')
        self.sockfd.close()
        sys.exit("谢谢使用,退出进程")

#网络连接
def main():
    sockfd = socket()
    #发起连接
    server_addr = ('127.0.0.1',8889)
    try:
        sockfd.connect(server_addr)
    except Exception as e:
        print("连接服务器失败:",e)
        return
#创建文件处理类对象
    ftp = FtpClient(sockfd)

    #收发消息
    while True:
        #接收服务器发送来的操作引导界面
        print("\n========命令选项=========")
        print("***      list       ***")
        print("***    get  file    ***")
        print("***    put  file    ***")
        print("***      quit       ***")
        print("=======================")
        #输入需要执行的代码
        cmd = input("输入命令>>")
        if cmd.strip() == 'list':
            ftp.do_list()
        elif not cmd or cmd.strip() == 'quit':
            ftp.do_quit()
        elif cmd[:3] == 'get':
            filename = cmd.strip().split(' ')[-1]
            ftp.do_get(filename)
        elif cmd[:3] == 'put':
            ftp.do_put()
        else:
            print("请输入正确命令")
 

if __name__ == '__main__':
    main()