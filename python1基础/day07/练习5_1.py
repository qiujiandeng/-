    # 1.思考下面的程序的执行结果是什么?为什么?
    #     L = list(range(10))
    #     for x in L:
    #         L.remove(x)
    #     print("L=",L)  #请问是空列表吗?

L = list(range(10))
for x in range(len(L)):   #x 遍历L
    # print(len(L))
    print(x)
    L.remove(x) #在L中,第一次找到x就删除掉,
#遍历id 0 id 0 = 0的时候,此时x = 0 L.remove(x)删除掉
#此时候id 0 = 1  遍历到 id 1 = 2 ,此时x = 2
#此时候id 0 = 1  1 = 3  2 = 4 遍历到id 2 时 x = 4 
#...
print("L=空",L)
    