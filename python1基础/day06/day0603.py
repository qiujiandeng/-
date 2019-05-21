    # ２，写一个程序，让用户输入两个或以上的正整数，当输入小于零的数时结束输入（不允许输入重复的数）
    #     １，打印这些数的和
    #     ２，打印这些书的最大数
    #     ３，打印这些数的第二大的数
    #     ４，删除最小的一个数,并打印原来的列表
L = []
while True:
    x = int(input("请输入数（小于零结束）："))
    if x > 0 and x not in L:
        L +=[x]
    if x < 0 and len(L) < 2:
        print("输入错误，您需要输入两个以上的数")
    if x < 0 and len(L) >= 2:
        break
print("这些数的和是：",sum(L))
L2 = sorted(L)   #把Ｌ序列内的整数从小到大排序好
print("这些数的最大数是：",L2[-1])
print("这些数第二大数是：",L2[-2])
del L2[0]
print("删除最小值是：",L2)

#l3 = min(L)   #用来观看调试时候值的变化
for ch in range(len(L)):
    # lch=L[ch]　#用来观看Ｌ[ch]值的变化
    if L[ch] == min(L):# 也可以＝＝ｌ３来观看调试时候的变化

        del L[ch]
        break
    
print(L)