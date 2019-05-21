# 练习：
#     用列表推导式生成１～１００内所有奇数组成的列表
#     结果是：[1,3,5,7,.......99]


#不算推导式
L = []
for x in range(100):
    if x % 2 == 1 :
        L.append(x)  #L += [x]
print(L)
print()

#老师的
S = [x for x in range(1,100,2)]
print(S)
print()
B = [x for x in range(1,100) if x % 2 ==1]
print(B)