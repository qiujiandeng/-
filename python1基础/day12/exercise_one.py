    # 1.编写函数fun,其功能是计算并返回下列多项式的和
    #     Sn = 1 + 1/1! + 1/2! + 1/3! + ..... + 1/n!
    # (建议用数学模块中的math.factorial(x)函数)
    #     求当 n = 20时, Sn 的值
#方法1
# def fun(n):
#     from math import factorial as fac
#     sn = 0
#     for x in range(0,n + 1):
#         sn += 1 / fac(x)
#     return sn
# print(fun(20))

#方法2
# def fun(n):
#     from math import factorial as fac
#     return sum([1/fac(x) for x in range(n+1)])
# print(fun(20))

# 方法三
def fun(n):
    from math import factorial as fac
    return sum(map(lambda x : 1/fac(x),range(n+1)))
print(fun(20))