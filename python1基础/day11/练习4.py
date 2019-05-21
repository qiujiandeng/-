# 练习4:
#     写一个递归求和函数:
#     def mysum(n):
#         ....
#         此函数求1+2+3+4+5+6+7+8+++++n的和
#     print(mysum(100))#5050

def mysum(n):
    if n == 1:
        return 1
    else:
        return n + mysum(n-1)
print(mysum(100))#5050