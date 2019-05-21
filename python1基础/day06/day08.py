# 练习：
#     生成一个列表，此列表为ｘ的平方加１不能被５整除的数的列表条件：((x**2 + 1) % 5 != 0
#     x的取值范围是 0 <= x <100


# L = []
# for x in range(100):
#     if (x**2-1)%5!=0:
#         L.append(x)
    
# print(L)

L = [x for x in range(100) if (x**2+1)%5!=0   ]
print(L)