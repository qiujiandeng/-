# 练习：
#     输入一个整数ｎ，打印一个宽度和高度都为ｎ个字符的长方形
#     如：请输入4
#     打印：
#     ＃＃＃＃
#     ＃　　＃
#     ＃　　＃　
#     ＃＃＃＃　

i = int(input("请输入一个数："))
kuangdu = i-2
a = 1
print("#"*i)
while a <= kuangdu:
    print("#"+" "*kuangdu+"#" )
    a += 1
if i >= 2:
    print("#"*i)