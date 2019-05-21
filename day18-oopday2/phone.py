# 课堂练习:
# 编写一个手机类(Phone)
# 属性:name,price,CPU,screen_size
# 方法:开机(startup),关机(shutdown)
#     打电话(call),发信息(send_msg)
# 并编写测试代码
import time
class Phone:
    def __init__(self,name,price=None,CPU=None,screen_size=None):
        self.name = name                #名称
        self.price = price              #价格
        self.CPU = CPU                  #cpu
        self.screen_size = screen_size  #屏幕尺寸
    
    def startup(self):                  #开机
        print("正在开机")
        time.sleep(2)
        print("开机成功")

    def shutdown(self):                 #关机
        print("正在关机")
        time.sleep(2)
        print("关机成功")
    
    def call(self,Phone_no):                     #打电话
        print("正在拨号")
        time.sleep(1)
        print("正在和%s通话" % Phone_no)
        
    def send_msg(self,phone_no,msg):                 #发短信
        print("正在向%s发送短信..." % phone_no)
        time.sleep(2)
        print("[%s]发送成功" % msg) 

    def __del__(self):  #析构方法
        print("__del__方法被调用")    

def fun():  #全局函数
    phone =Phone('华为',1999.99,'双核2G',5.5)
    print("fun()函数退出")

def myfun():
    phone =Phone('华为',1999.99,'双核2G',5.5)
    print("fun()函数退出")

if __name__ == '__main__':
    myphone = Phone('华为',1999.99,"双核2G",5.5)
    myphone.startup()
    myphone.call("13512345678")
    myphone.send_msg("13512345678","你好")
    myphone.shutdown()
    fun()
    myfun()
    print("程序退出")
    #myphone 程序退出时被销毁