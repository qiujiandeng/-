from multiprocessing import Pool
from time import sleep,ctime

#进程事件
def worker(msg):
    sleep(2)
    print(msg)
    return ctime()

#创建进程池
pool = Pool()


result=[]#存放函数事件对象
#向进程池添加事件
for i in range(10):
    msg = "hello %d"%i
    r = pool.apply_async(func=worker,args=(msg,)) #msg加逗号是元组
    result.append(r) #存储函数事件对象

#关闭进程池
pool.close()
#回收进程池
pool.join()
# print(result)
for i in result:
    print(i.get())  #通过对象get()可以获取事件函数返回值
    