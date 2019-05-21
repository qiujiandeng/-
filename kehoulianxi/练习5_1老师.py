# 练习5:
#     1.思考下面的程序的执行结果是什么?为什么?
#         L = list(range(10))
#         for x in L:
#             L.remove(x)
#         print("L=",L)  #请问是空列表吗?
L = list(range(10))
while L:
    L.remove(L[0])
print("L=",L)