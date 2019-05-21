# 此示例示意当函数的实参为可变数类型时,在函数内部可以改变容器的内容

L = [1,2,3,4]
t = (1.1,2.2,3.3,4.4)  #元组是不可变的

def append_5(x):
    # x.append(5)
    x += (5,)
    # x += (*t,)

append_5(L)
print(L)#1,2,3,4,5

append_5(t)
print(t)