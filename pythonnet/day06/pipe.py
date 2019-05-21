from multiprocessing import Process,Pipe
import os,time

#创建管道对象,默认是True双向都可读写
fd1,fd2 = Pipe()

#创建几个进程
def fun(name):
    time.sleep(3)
    #向管道写入内容
    fd1.send({name:os.getpid()})
    # fd1.send(name)

jobs = []
for i in range(5):
    p = Process(target=fun,args=(i,))
    jobs.append(p)
    p.start()

for i in range(5):
    #从管道读取内容
    data = fd2.recv()
    print(data)
for i in jobs:
    i.join()
