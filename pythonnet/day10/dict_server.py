'''
dict project for AID
'''

from socket import *
import pymysql
import os,sys
import time
import signal

#定义全局变量,给别人用,又不想别人修改源代码
# python3 server.py  192.169....  8888
if len(sys.argv) < 3:
    print('''Start as:
    python3 dict_server.py 0.0.0.0  8000
    ''')
    sys.exit(0)

HOST = sys.argv[1]
PORT = int(sys.argv[2])
ADDR = (HOST,PORT)
#定义单词本位置
DICR_TEXT = "./dict.txt"


#搭建网络连接
def main():
    #连接数据库
    db = pymysql.connect('localhost','root','123456','dict')
    #创建套接字
    s = socket()
    #可以不设置端口重启,因为在终端输入了,sys.args
    # s.setsockopt(SOL_SOCKET,SO_REUSEADDR,1)
    s.bind(ADDR)
    s.listen(5)
    #处理僵尸进程
    signal.signal(signal.SIGCHLD,signal.SIG_IGN)

    #循环等待客户端连接
    while True:
        try:
            c,addr = s.accept()
            print("Connect from",addr)
        except KeyboardInterrupt:
            s.close()
            sys.exit("服务器退出")
        except Exception as e:
            print(e)
            continue

        #创建子进程
        pid = os.fork()
        if pid == 0:
            s.close()
            #传客户端和数据库给do_child处理
            # print('运行到这里')
            do_child(c,db)
            sys.exit()
        else:
            c.close()  

#处理客户端请求
def do_child(c,db):
    while True:
        #接收客户端请求
        data = c.recv(1024).decode()
        #打印一下在哪个终端收到什么请求
        print(c.getpeername(),':',data)
        #防止客户端异常退出
        if not data or data[0] == 'E':
            c.close()
            sys.exit()
        #切割或者直接data[0] 判断一下请求类型
        elif data[0]  == 'R':
            #要判断
            do_register(c,db,data)
        elif data[0] == 'L':
            do_login(c,db,data)
        elif data[0] == 'Q':
            #查词
            do_query(c,db,data)
        elif data[0] == 'H':
            #查词
            do_hist(c,db,data)


def do_register(c,db,data):
    #先判断是否允许插入数据库
    #提取姓名
    l = data.split(' ')
    name = l[1]
    passwd = l[2]
    #游标
    cursor = db.cursor()

    sql = "select * from user where name='%s'"%name
    cursor.execute(sql)
    #查找取得结果集的第一条记录为元组,没有就是null(空)
    r = cursor.fetchone()
    #直接判断r的返回值不等于空,就是用户存在了
    if r != None:
        c.send(b'EXISTS')
    
        return
    #如果等于空
    #插入用户
    sql = "insert into user(name,passwd) values ('%s','%s')"%(name,passwd)
    
    try:
        cursor.execute(sql)
        db.commit()
        c.send(b"OK")
        
    except:
       
        db.rollback()
        c.send(b"FAIL")

        
def do_login(c,db,data):
    l = data.split(' ')
    name = l[1]
    passwd = l[2]
    cursor = db.cursor()

    sql = "select * from user where name='%s' and passwd='%s'"%(name,passwd)

    #查询用户
    cursor.execute(sql)
    r = cursor.fetchone()
    if r == None:
        c.send(b'FAIL')
    else:
        c.send(b'OK')

def do_query(c,db,data):
    l = data.split(' ')
    name = l[1]
    word = l[2]

    #插入历史记录
    cursor = db.cursor()
    tm = time.ctime()
    sql = "insert into hist (name,word,time) values\
        ('%s','%s','%s')"%(name,word,tm)
    try:
        cursor.execute(sql)
        db.commit()
    except:
        db.rollback()


    #单词本查找一下(数据库好,但是练下这个)
    f = open(DICR_TEXT)

    for line in f:
        tmp = line.split(' ')[0]  #提取单词
        if tmp > word:
            break
        elif tmp == word:
            c.send(line.encode())
            f.close()
            return
    c.send("没有找到该单词".encode())
    f.close()

def do_hist(c,db,data):
    name = data.split(' ')[1]
    cursor = db.cursor()
    #查找name 在id倒序 limit显示前十条
    sql = "select * from hist where name = '%s' \
        order by id desc limit 10"%name
    cursor.execute(sql)
    r = cursor.fetchall()
    if not r:
        c.send(b"FAIL")
        return
    else:
        c.send(b'OK')
        time.sleep(0.1)
    for i in r:
        msg = "%s  %s  %s"%(i[1],i[2],i[3])
        c.send(msg.encode())
        time.sleep(0.01)
    c.send(b"##")

    


if __name__ == '__main__':
    #启动程序
    main()
