# 1.用filter 生成能提供偶数的可迭代对象,生成1 ~ 20 的偶数,
    # 将这些偶数存与列表中,在打印这个列表(不包含20)

L = list(filter(lambda x:x % 2 == 0,range(1,20)))
print('L',L)

flt = filter(lambda x : x % 2 == 0,range(1,20))
L1 = list(flt)
print('L1',L1)

L2 = [x for x in filter(lambda x:x % 2 == 0,range(1,20))]
print('L2',L2) 
