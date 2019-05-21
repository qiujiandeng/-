# exercize2:
#     已知有列表:
#         L = [2,3,5,7]
#     1.写一个生成器函数,让此函数能够动态提供数据,数据为原列表的数字的平方加1
#     2.写一个生成器表达式,让此表达式能够动态提供数据,数据为原列表的数据的平方加1
#     3.写一个列表,此列表的数据为原列表L的数字的平方加1

L = [2,3,5,7]
def myscq(a):
    for x in a:
        yield x**2+1

for x in myscq(L):
    print(x)

L1 = (x**2+1 for x in L)
for x in L1:
    print(x)
#老师的
for x in (a ** 2 + 1 for a in L):
    print(x)

L2=[x**2+1 for x in L]
print(L2)
