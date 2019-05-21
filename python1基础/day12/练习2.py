# 练习2:
#     写一个程序,输入你的出生日期(年月日)
#         1.算出你已经出生了多少天?
#         2.算出你出生那天是星期几?
import time
n = int(input("请输入出生的年:"))
y = int(input("请输入出生的月:"))
r = int(input("请输入出生的日:"))

t = (n,y,r,0,0,0,0,0,0)
#先得到出生时,计算机时秒数,得到当前时间秒数
tt = time.mktime(t)
huo = time.time() - tt #活了多少秒
huotian = huo /60/60//24
print(huotian)
chus = time.localtime(tt)
weeks = {
    0:'星期一',1:'星期二',2:'星期三',3:'星期四',4:'星期五',5:'星期六',6:'星期日'}
print(weeks[chus[6]])