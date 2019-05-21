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
except ValueError:
    print("分苹果失败!苹果被收回")
except:   #用来捕获除ValueError之外的全部类型的异常错误
    print("其他类型的错误发生,苹果被收回!!!")  
print("程序正常退出")
