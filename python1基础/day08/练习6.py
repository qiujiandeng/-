# 练习6:
#     3.写一个函数 input_number
#     def input_number():
#         ....
#     此函数用来获取用户循环输往返整数,当用户输入负数时结束输入
#     将用户输入的数字一列表的形式返回,在用內建函数max,min,
#     sum求出用户输入的最大值,最小值及和

#     L = input_number()
#     print("用户输入的最大数是:",max(L))
#     print("用户输入的最下属是:",max(L))
#     print("用户输入的全部数的和是:",sum(L))


def input_number():
    myl = []
    while True:
        a = int(input("请输入整数:"))
        if a < 0:
            break
        myl.append(a)
    return myl
L = input_number()
print("用户输入的最大数是:",max(L))
print("用户输入的最小数是:",min(L))
print("用户输入的全部数的和是:",sum(L))
