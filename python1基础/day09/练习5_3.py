    # 3.写一个myrange()函数,参数可以传1~3个,实际意义同range函数规则相同,
    # 此函数返回符合range(....) 函数规则的列表
    # 如:
    #     L = myrange(4)
    #     print(L)   #[0,1,2,3]
    #     L = myrange(4,6)
    #     print(L)  #[4,5]
    #     L = myrange(1,10,3)
    #     print(L)  #[1,4,7]

def myrange(start,stop=None,step=None):
    if stop is None:
        stop = start
        start = 0
    if step is None:
        step = 1
    #开始,结束,步长都确定
    # return [x for x in range(start,stop,step)]
    if step > 0: #正方形
        L = []
        while start < stop:
            L.append(start)
            start += step
        return L
    elif step < 0:
        L = []
        while start > stop:
            L.append(start)
            start += step
        return L
L = myrange(4)
print(L)   #[0,1,2,3]
L = myrange(4,6)
print(L)  #[4,5]
L = myrange(1,10,3)
print(L)  #[1,4,7]
L = myrange(1,-20,-1)
print(L)