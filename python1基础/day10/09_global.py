
# 3.不能先声明局部的变量,在用flobal声明为全局变量,此做法不符合规则


#变量,此做法不符合规则
# def f1():
#     x = 100
#     global x

def f1():
    #x = 100 #此处会警告
    global x
    x = 100
f1()
print(x)


# 4. global 变量列表里的变量不能出现在此作用域内的形参列表里
v =100
#def f2(v):#v不能即是参数又是全局变量必然会出错
def f2(v):
    #global v   #此处必然会出错
    v = 300

f2(200)
print(v)