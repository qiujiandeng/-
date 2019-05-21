from multiprocessing import Process
import time
#自定义进程类
class ClockProcess(Process):
    def __init__(self,value):
        self.value = value
        super().__init__()
    
    #重写run方法
    def run(self):
        for i in range(5):#遍历5次
            print("The time is %s"%time.ctime())#打印当前时间
            time.sleep(self.value)#等待self值这么多秒

#创建进程对象
p = ClockProcess(2)
#启动新的进程
p.start()
#阻塞等待回收进程
p.join()