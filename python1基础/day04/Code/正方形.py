# 练习：
#     输入一个数，打印指定宽度的正方形
#     如：
#         请输入：５
#     打印：
#         1　2　3　4　5
#         1　2　3　4　5　
#         1　2　3　4　5　
#         1　2　3　4　5
#         1　2　3　4　5

i = int(input("请输入一个数："))
h = 1
while h <= i:
    s = 1
    while s <= i:
        print(s, end=' ',flush=True)
        s += 1
    print()
    h += 1