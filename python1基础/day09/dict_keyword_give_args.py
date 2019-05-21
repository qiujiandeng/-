# 此示例示意字典传参
def myfun1(a,b,c):
    '''这个是字典传参的示例'''
    print("a的值是:",a)
    print("b的值是:",b)
    print("c的值是:",c)

d1 = {'c':33,'a':11,'b':22}
myfun1(c=d1['c'],a=d1['a'],b=d1['b'])
myfun1(**d1) #拆解字典,在按关键字传参方式传递