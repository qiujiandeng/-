#  输入一个整数

i = int(input("请输入一个整数："))
a = 1
while a<=i:
    print("这是第",a,"行")
    a += 1
else:
    print("我是while语句中的else语句")
