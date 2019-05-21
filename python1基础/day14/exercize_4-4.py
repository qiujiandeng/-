    # 4.打印杨辉三角,只打印6层
    #        1
    #       1 1
    #      1 2 1
    #     1 3 3 1
    #    1 4 6 4 1
    #  1 5 10 10 5 1 

def get_next_line(L):
    '''此函数根据上一层L,返回下一层数字列表
    如:L = [1,2,1]
    返回:[1,3,3,1]'''
    L2 = [1] #最左边的1
    #计算中间的数字
    for i in range(len(L)-1):
        L2.append(L[i] + L[i+1])
    #添加最后一个1
    L2.append(1)
    return L2
def get_yanghui_list(n):
    '''此函数返回n层的杨辉三角的列表
    如 n 等于4 则返回
    [
        [1],
        [1,1],
        [1,2,1],
        [1,3,3,1]
    ]
    '''
    L = [] #用来存放每一层的列表
    layer = [1]
    while len(L) < n :
        #每次循环放入一层
        L.append(layer)
        layer = get_next_line(layer)
    return L

def get_yanghui_string_list(L):
    '''此函数 传入一个有数字列表组成的列表,返回字符串列表
    如 
    L = [[1], [1, 1], [1, 2, 1], [1, 3, 3, 1]]
    返回['1','1 1','1 2 1']
    '''
    L2 = [] #准备存放字符串
    for layer in L:
        s = ' '.join((str(x)for x in layer))
        L2.append(s)
    return L2

def print_ranghui_triangle(L):
    max_len = len(L[-1])
    for s in L:
        print(s.center(max_len))

L = get_yanghui_list(10)
string_L = get_yanghui_string_list(L)
print_ranghui_triangle(string_L)
