# 练习5:
#     1.写一个函数mysum(n) , 此函数用来计算
#     1+2+3+4+5+6+7+8+9.......+n 的和
#     (要求:不允许调用sum)
#     如:
#         print(mysum(100))   #5050
#         print(mysum(4))     #4

# def mysum(n):
#     i = 0
#     for ch in range(n+1):
#         i += ch
#     return i

def mysum(n):
    return sum(range(1,n+1))


print(mysum(100))   #5050
print(sum(range(1,101)))
print(mysum(4))     #10

