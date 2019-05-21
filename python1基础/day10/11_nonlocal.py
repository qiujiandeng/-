# 1.nonlocal 语句只能在被嵌套函数内部进行使用

# def f1():
#     nonlocal x #这是错的,因为没有外部嵌套函数
#     x = 100
# f1()

# 3.当有两层或两层以上的函数嵌套时,访问nonlocal变量的值对最近一层的变量进行操作

def f1():
    v = 100
    def f2():
        v = 200
        def f3():
            nonlocal v
            v += 1
        f3()
        print("f2最后的v=",v)
    f2()
    print('f1最后的v=',v)
f1()

# 4.nonlocal 语句的变量列表里的变量名,不能出现在此函数的参数列表中
