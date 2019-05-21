#此示例示意filter函数

def is_odd(x):
    '''此函数判断x是否是奇数,是奇数返回True,否则返回False'''
    return x % 2 == 1
#打印1~20 的奇数:
for x in filter(is_odd,range(20)):
    print(x)
print('----------------')
for x in filter(lambda x: x %2==1,range(20)):
    print(x)

#生成20以内的全部偶数(不包含20)的列表
L = list(filter(lambda x:x % 2 == 0,range(20)))
print(L)
L2 = [x for x in filter(lambda x:x % 2 == 0,range(20))]
print('L2=',L2)