    # 2. 分解质因数,输入一个正整数,分解质因数
    #   如:
    #     输入:90
    #   打印:
    #     90 = 2*3*3*5
    # (质因数是指最小能被原数整数的素数(不包括1))
def get_zhiyin_lies(x):
    '''此函数返回x的质因数的列表
    如 x =90
    返回[2,3,3,5]
    '''
    L = []#准备存储质因数
    while x > 1:
        #每次求取一个质因数,然后放在L中
        for i in range(2,x + 1):
            if x % i == 0:#i一定是质因数
                L.append(i)
                x = int(x/i)
                break #进入下一次循环
    return L
x = int(input('请输入正整数:'))
L = get_zhiyin_lies(x)
L2 = (str(x) for x in L)
print(x,'=','*'.join(L2))

# x = int(input('请输入一个整数:'))
# xx = x
# ss = []
# zs = 2
# while x != 1:
#     if x % zs ==0:
#         ss.append(zs)
#         x = x // zs
#         zs = 2
#     else:
#         zs += 1
# # print(ss)
# print(xx,'= ',end='')
# b = 1
# for ch in ss:
#     if b < len(ss):
#         print(ch,end='*')
#         b += 1
#     else:
#         print(ch)
# # print()

