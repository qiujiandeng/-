# exercise6:
#     1.写一个生成器函数myxrange(start,stop,step)来生成一系列整数:
#     要求:
#         myxrange的功能与range功能完全相同
#         不允许调用range函数和列表
#     用自己写的myxrange结合生成器表达式求1~10内的奇数和平方和
#         print(sum(x for x in myxrange(1,10)if x % 2))
def myxrange(start=0,stop=0,step=1):
    x = []
    while True:
        if start < stop and step < 2:
            x.append(start)
            start += step
        if start < stop and step >= 2:
            x.append(start)
            start += step
        if stop == 0 :
            s = 0
            while True:
                if s < start:
                    x.append(s)
                    s += step
                else:
                    break
        if start >= stop:
            return x
# print(myxrange(1,10,2))
# for x in myxrange(10):
#     print(x)



print(sum(x ** 2 for x in myxrange(1,10) if x % 2 ))