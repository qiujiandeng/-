#  ２．写程序，任意给出三个数，打印出三个数中最大的一个数



#laoshi
a = int(input("请输入第一个数："))
b = int(input("请输入第一个数："))
c = int(input("请输入第一个数："))

#改进算法：
#先假设第一个最大，用变量绑定
#进了西瓜地，看到第一个西瓜拿起来，看到第二个西瓜比第一个大，把第一个扔掉拿第二个，...第三个
zuida = a             #ｚｕｉｄａ等于手，a等于第一个西瓜
if b >zuida:          #第二个比手里的大，扔掉手里的，把第二个拿到手里，手上等于第二个西瓜
    zuida = b
if c >zuida:
    zuida = c
print("最大数式：",zuida)





# if a > b:
#     #a 和 c　在比
#     if a > c:
#         print("最大数是",a)
#     # if a > d:
#     #     ........
#     # else:
#     #     ..... 下面也是
#     else:
#         print("最大数是",c)
# else:
#     # b 和　c　再比
#     if b > c:
#         print("最大数是",b)
#     else:
#         print("最大数是",c) 