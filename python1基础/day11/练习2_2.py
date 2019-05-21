    # 2.用filter函数,将1 ~ 100 之间所有的素数prime 放入到列表中,
    # 在打印这个列表


def is_prime(x):
    if x < 2:
        return False
    for i in range(2,x):
        if x % i == 0:
            return False
    return True
L1 = list(filter(is_prime,range(100)))
print("L1=",L1)

L2 = [x for x in filter(is_prime,range(100))]
print("L2=",L2)

L3 = [x for x in range(100) if is_prime(x)]
print("L3=",L3)






# 我的

def sushu(i):

    s = [2,3,4,5,6,7,8,9]#定一个除数的列表

    for ch in s:
        if i < 2:
            return False
        if i == ch:                         
            continue                       
        if i % ch == 0: 
            return False                                                                                     
    return True

L = list(filter(sushu,range(100)))            
print("L=",L)