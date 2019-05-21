    # 2.写一个函数myfac(n) 来计算n!(n的阶乘)
    # n! = 1*2*3*4*.....n
    # 如:
    #     print(myfac(5))  #120

#recursion
def myfac(n):
    if n == 0:
        return 1
    else:
        return n * myfac(n-1) #n! = n * (n-1)!
print(myfac(5))
        