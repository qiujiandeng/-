# mydeco3.py

#此示例示意函数装饰器的使用
#以银行存取款业务为例,来为存取款业务添加新的功能


#------以下是小钱写的装饰器---
def privileged_check(fn):
    def fx(n,x):
        print('正咋检查权限.....')
        fn(n,x)
    return fx

def send_message(fn):
    def fy(n,x):
        fn(n,x)
        print('正在发短信给:',n)
    return fy

#--------一下是老师写的程序
@privileged_check
def savemoney(name,x):
    print(name,'存钱',x,'元')

@send_message
@privileged_check
def withdraw(name,x):
    print(name,'取钱',x,'元')

#------以下是调用者小张写的程序后炒老板鱿鱼了-----
savemoney('小王',200)
savemoney('小赵',400)

withdraw("小李",500)
