    # 3.写一个函数计算:
    # 1+2**2+3**3+....+n** 的和
    # (n给个小点的数来进行测试)

def myxxxx(n):
    i = 1
    for ch in range(2,n+1):
        i += ch ** ch
        print(i)
    return i
print(myxxxx(4))