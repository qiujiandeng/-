from multiprocessing import Process 
import os

filename = "./test.jpg"
#获取文件大小
size = os.path.getsize(filename)

def top():
    #复制上班部分
    f = open(filename,"rb")
    n = size // 2#防止是单数
    fw = open("half_top.jpg",'wb')
    while True:
        if n < 1024:
            data = f.read(n)
            fw.write(data)
            break
        data = f.read(1024)
        fw.write(data)
        n -= 1024
    f.close()
    fw.close()


def boot():
    #复制下班部分
    f = open(filename,'rb')
    fw = open('half_bottom.jpg','wb')
    f.seek(size//2,0)

    while True:
        data = f.read(1024)
        if not data:
            break
        fw.write(data)
    f.close()
    fw.close()

t = Process(target=top)
b = Process(target=boot)
t.start()
b.start()
t.join()
b.join()
