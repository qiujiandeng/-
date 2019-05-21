# 3.编写一个闹钟程序,启动时设置定时时间,到时间后打印一句"时间到!" 然后退出程序

def alarm(hour,minute):
    import time
    while True:
        t = time.localtime() #获取当前时间
        print("%02d:%02d:%02d"%t[3:6],end='\r')
        time.sleep(0.1)
        if t [3] == hour and t[4] == minute:
        #if t[3:5] == (hour,minute)
            print("时间到!!!")
            return

h = int(input("请输入小时:"))
m = int(input("请输入分钟:"))
alarm(h,m)