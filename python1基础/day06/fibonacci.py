    # ３．生成前４０个斐波那契数列（Fibonacci)
    #     1 1 2 3 5 8 13 21
    #     要求：　将这些书保存在列表中，最后打印这些书
    #     注：斐波那契数的前２个数为１和１，从第二数起为前两个数相加之和

# #方法

# L = []
# a = 0 #a 表示第一个数的前一个数
# b = 1 #b表示第一个数

# while len(L) < 40:
#     #每次把b加入到列表中
#     L.append(b)
#     #在计算出下一个fibonacci数,存于b中
#     c = a + b #算出下一个数
#     a = b #把当前作为前一个数
#     b = c #把新算出来的c赋值(交给)给b
# print("L=",L)



# #方法

# L = []
# a = 0 #a 表示第一个数的前一个数
# b = 1 #b表示第一个数

# while len(L) < 40:
#     #每次把b加入到列表中
#     L.append(b)
#     #在计算出下一个fibonacci数,存于b中
#     a,b = b,a + b

# print("L=",L)


L = [1,1]

while len(L) < 40:
    L.append(L[-1] + L[-2])
    #在计算出下一个fibonacci数,存于b中
    

print("L=",L)