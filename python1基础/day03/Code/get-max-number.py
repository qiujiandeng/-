#  ２．写程序，任意给出三个数，打印出三个数中最大的一个数

a = int(input("请输入第一个数："))
b = int(input("请输入第一个数："))
c = int(input("请输入第一个数："))
if a > b > c:
    print(a,"max")

elif b > a > c:
    print(b,"max")

else:
    print(c,"max")

#laoshi
a = int(input("请输入第一个数："))
b = int(input("请输入第一个数："))
c = int(input("请输入第一个数："))
if a > b:
    #a 和 c　在比
    if a > c:
        print("最大数是",a)
    # if a > d:
    #     ........
    # else:
    #     ..... 下面也是
    else:
        print("最大数是",c)
else:
    # b 和　c　再比
    if b > c:
        print("最大数是",b)
    else:
        print("最大数是",c) 