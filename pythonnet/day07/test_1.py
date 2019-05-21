import os
import time
from multiprocessing import Process
from threading import Thread

#计算密集型函数  x,y传入1
def count(x,y):
    c = 0
    while c < 7000000:
        c += 1
        x += 1
        y += 1
#用单进程,和单线程记录执行10次后完成的所需的时间  用time.time
# aaa = time.time()
# print(aaa)
# pidd = []
# for i in range(10):
#     pid = Process(target=count,args=(1,1))
#     pidd.append(pid)

# for i in pidd:
#     i.start()
#     # pidd.append(pid)
# for i in pidd:
#     i.join()
# bbb = time.time()
# ccc = bbb - aaa
# print(bbb)
# print(ccc)

#多进程10个,每个运行一遍,    用 多线程创建10个线程,每个线程执行一遍  记录时间
# aaa = time.time()
# aa1 = time.localtime(aaa)
# # print(time.localtime(aaa))
# print(time.asctime(time.localtime(time.time())))
# xc = []
# for i in range(10):
#         t = Thread(target=count,args=(1,1))
#         xc.append(t)
#         t.start()

# for i in xc:
#         i.join()
# bbb = time.time()
# ccc = bbb - aaa
# print(bbb)
# print(ccc)

# io秘籍型程序 
def io():
    write()
    read()
    #可以将下面两个函数封装成一个里面执行
def write():
    f = open("test","w")
    for i in range(1200000):
        f.write("hello world\n")
    f.close()

def read():
    f = open("test")
    lines = f.readlines()#读出文档
    f.close()

#用单进程和单线程程序执行10遍   后记录完成时间
aaa = time.time()
# print(aaa)
#保存进程
jccx = []
for i in range(10):
        p = Process(target=io)
        jccx.append(p)
        p.start()

for i in jccx:
        i.join()

# bbb = time.time()
print(time.time()-aaa)

# #用10个线程,每个处理一遍,看看完成时间
# aaa = time.time()
# print(aaa)
# xccx = []  #保存打开的线程
# for i in range(10):
#         t = Thread(target=io)
#         xccx.append(t)
#         t.start()
# for i in xccx:
#         i.join()
# bbb = time.time()
# print(bbb-aaa)