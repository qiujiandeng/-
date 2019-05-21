    # ２，写一个程序，让用户输入两个或以上的正整数，当输入小于零的数时结束输入（不允许输入重复的数）
    #     １，打印这些数的和
    #     ２，打印这些书的最大数
    #     ３，打印这些数的第二大的数
    #     ４，删除最小的一个数



numbers = []
while True:
    x = int(input("请输入正整数："))
    if x < 0:
        if len(numbers) < 2:
            print("您输入的数字太少")
            continue
        break
    if x not in numbers:
        numbers += [x]
print("这些数的和是：",sum(numbers))
L = sorted(numbers)
print("最大数是：",L[-1])
print("最小数是：",min(L))
print("第二大数是:",L[-2])
min_numer = L[0]
for i in range(len(numbers)):
    if numbers[i] == min_numer:
        del numbers[i]
        break
print("删除最小数后的列表是：",numbers)
# L = []
# while True:
#     x = int(input("请输入数（小于零结束）："))
#     if x > 0:
#         L +=[x]
#     if x < 0 and len(L) < 2:
#         print("输入错误，您需要输入两个以上的数")
#     if x < 0 and len(L) >= 2:
#         break
# print("这些数的和是：",sum(L))
# L2 = sorted(L)   #把Ｌ序列内的整数从小到大排序好
# print("这些数的最大数是：",L2[-1])
# print("这些数第二大数是：",L2[-2])
# del L2[0]
# print("删除最小值是：",L2)
