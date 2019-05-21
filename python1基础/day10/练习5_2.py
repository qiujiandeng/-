    # 2.写一个函数myfac(n) 来计算n!(n的阶乘)
    # n! = 1*2*3*4*.....n
    # 如:
    #     print(myfac(5))  #120

def myfac(n):
    i = 1
    for ch in range(2,n+1):
        i = i*ch
    return i
print(myfac(5))