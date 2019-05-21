from socket import *
import sys
import getpass

#创建网络连接
def main():
    if len(sys.argv) < 3:
        print("argv is error")
        return
    HOST = sys.argv[1]
    PORT = int(sys.argv[2])

    #创建套接字
    s = socket()
    try:
        s.connect((HOST,PORT))
    except Exception as e:
        print(e)
        return
        
    while True:
        print('''
        ==========Welcome==========
        --1.注册    2.登录  3.退出--
        ===========================
        ''')

        #通过选项去完成请求了
        try:
            cmd = int(input("输入选项:"))
        except Exception as e:
            print("命令输入有误")
            continue
        if cmd not in [1,2,3]:
            print("请输入正确选项")
            continue
        elif cmd == 1:
            #运行注册函数
            do_register(s)


            
        elif cmd == 2:
            do_login(s)


        elif cmd == 3:
            #运行退出
            s.send(b'E')
            sys.exit("谢谢使用")

def do_register(s):
    while True:
        name = input("User:")
        passwd = getpass.getpass()
        #输入第二次密码
        passwd1 = getpass.getpass()
        if (' ' in name) or (' ' in passwd):
            print("用户名或密码不允许有空格")
            continue
        if passwd != passwd1:
            print("两次密码不一致")
            continue
        #给服务端发送我的请求了
        msg = "R %s %s"%(name,passwd)
        #发送请求
        s.send(msg.encode())
        #等待回复
        data = s.recv(1024).decode()
        #判断客户端给的结果
        if data == "OK":
            print("注册成功")
            #这里注册成功后直接进入二级界面,不写的话返回一级界面
            login(s,name)
        elif data == "EXISTS":
            print("用户已存在")
        else:
            print("注册失败")
        #无论是那个判断都要结束此函数
        return
        #返回到一级界面
        
def do_login(s):
    name = input("User:")
    passwd = getpass.getpass()
    msg = "L %s %s"%(name,passwd)
    s.send(msg.encode())
    data = s.recv(128).decode()
    if data == "OK":
        print("登录成功")
        #调用函数设计二级界面
        login(s,name)
    else:
        print("登录失败")

def login(s,name):
    while True:
        print('''
        ==========Welcome===========
        --1.查词  2.历史记录  3.注销--
        ============================
    ''')

        #通过选项去完成请求了
        try:
            cmd = int(input("输入选项:"))
        except Exception as e:
            print("命令输入有误")
            continue
        if cmd not in [1,2,3]:
            print("请输入正确选项")
            continue
        elif cmd == 1:
            #查词
            do_query(s,name)
            
        elif cmd == 2:
            #查找历史记录
            do_hist(s,name)


        elif cmd == 3:
            return

def do_query(s,name):
    while True:
        word = input("单词:")
        if word == "##":
            break
        msg = "Q %s %s"%(name,word)
        s.send(msg.encode())
        #返回可能是两种情况,可能是单词解释,或者找不到
        data = s.recv(2048).decode()
        print(data)

def do_hist(s,name):
    msg = "H %s"%name
    s.send(msg.encode())
    data = s.recv(128).decode()
    if data == 'OK':
        #在不知道服务器发回来多少条怎么办
        while True:
            data = s.recv(1024).decode()
            #如果不给我发了.给我个暗号
            if data == "##":
                break
            print(data)
            
    else:
        print("没有历史记录")

if __name__ == '__main__':
    main()