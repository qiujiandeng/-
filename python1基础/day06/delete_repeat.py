    # 2.有一些数存于列表中，如：
    #     Ｌ = [1,3,2,1,6,4,2,......,98,82]
    #     1,将列表中出现的数字存入到另一个列表Ｌ２中
    #         要就：
    #         重复出现多次的数只在Ｌ２列表中保留一份（去重复）
    #     ２，将列表中出现两次的数字存于Ｌ３列表中，在Ｌ３列表中只保留一份

L =[1,2,3,1,2,1,5,2,6,7,9,8,87,95]
L2 = []
for x in L:
    if x not in L2:
        L2.append(x)
print(L2)
L3 = []
for x in L:
    if L.count(x) >= 2 and x not in L3:
        L3.append(x)
print('L3=',L3)   