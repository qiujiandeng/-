# 练习6:
#     2.已知有列表:
#         L = [[3,5,8],10,[[13,14],15,18],20]
#         1.写一个函数print_list(lst) 打印出所有的数字
#             如:print_list(L) #打印 3  5  8  10 ......
#             (不要求打印在一行)
#         2.写一个函数 sum_list(lst) 返回这个列表中所有的数字的和
#             如:
#                 print(sum_list(L))  #打印 106
#         注:
#             type(x)  可以返回一个变量的类型
#             如:
#             >>>type(20) is int #True
#             >>>type([1,2,3])  is list #True

L = [[3,5,8],10,[[13,14],15,18],20]

def print_list(lst):
    t = 0
    for ch in lst:
        if type(ch) is int:
            print(ch)
            t += ch
        if type(ch) is list:
            for x in ch:
                if type(x) is int:
                    print(x)
                    t += x
                if type(x) is list:
                    for xx in x:
                        print(xx)
                        t += xx
    return t
print(print_list(L)