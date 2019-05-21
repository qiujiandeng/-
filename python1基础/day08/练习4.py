
# 练习4:
#     1.写一个函数mymax,实现返回两个数的最大值:
#     如:
#         def mymax(a,b):
#             .....#此处自己实现
#         print(mymax(100,200))    #200
#         print(mymax("ABC",'ABCD'))  #ABCD

def mymax(a,b):
    # if a > b :
    #     return a
    # else:
    #     return b 
    zuida = a
    if b > zuida:
        zuida = b 
    return zuida

print(mymax(100,200))
print(mymax("ABC",'ABCD'))