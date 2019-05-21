# closure.py

#用全局变量来保存压岁钱

def give_yasuiqian(money):
    def child_buy(obj,m):
        nonlocal money
        if money > m :
            money -= m
            print('买',obj,'花了',m,'元,剩余',money,'元')
        else:
            print("买",obj,"失败")
    return child_buy  #返回内嵌函数的引用关系
cb = give_yasuiqian(1000)  #给压岁钱1000
cb("变形金刚",200)
cb("漫画三国",100)