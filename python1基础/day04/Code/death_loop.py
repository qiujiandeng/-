# 任意输入一些整数，当输入负数时结束输入，当输入完成后，打印您输入这些数的和
# 如：
#     请输入：１
#     请输入：２
#     请输入：３
#     请输入：４
#     请输入：-１
#     打印：
#     您刚擦输入的这些数的和是：１０

s = 0 #此变量来记录累加和

while True:
    x = int(input("请输入:"))
    if x < 0:
        break
    s += x
print("您刚才输入数的和式:",s)

