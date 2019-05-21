# 练习1:
#     1.猜数字游戏:
#         随机生成一个0~100之间的整数,用变量x绑定
#         让用户循环输入一个整数没用变量y绑定,输出猜数字的结果
#             如果y等于x则提示'恭喜你猜对了',并结束才数字
#             如果y大于x,则提示:'您猜大了'
#             如果y小于x,则提示:'您猜小了'
#         直到猜对位置,显示用户猜数字的次数后退出程序
import random

x = random.randint(0, 100)
#x = random.randrange(101)
s = 0 #猜的次数

while True:
    i = int(input("请输入一个整数:"))
    
    
    if i > x:
        print("您猜大了!")
        s += 1
    if i < x:
        print("您猜小了!")
        s += 1
    if i == x :
        print('恭喜你猜对了')
        s += 1
        print('您一共猜了%d次'%s)
        break