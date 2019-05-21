# try_except.py
# 此示例示意try_except语句的语法和用啊
def div_apple(n):
    print(n,'个苹果你想分给几个人')
    s = input("请输入人数:")
    cnt = int(s)     #<---可能出发ValueError错误
    result = n / cnt #<----可能触发ZeroDivisionError错误
    print("每个人分了",result,'个苹果')
try:
    div_apple(10)
    print("分苹果成功!")
except ValueError as err:
    print("分苹果失败!苹果被收回")
    print("err=",err)
except ZeroDivisionError:
    print('没有人来,苹果自己吃了')
# div_apple(10)
print("程序正常退出")
