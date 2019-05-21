
# 练习：

#     ３．计算1+3+5+7+.......+99的和
#         分别用ｆｏｒ循环语句和ｗｈｉｌｅ循环语句实现


# s = 0   
# for  x in range(1,100,2):
#     # if x % ==1:
#     s += x
# print(s)


# d = 0
# c = range(1,100,2)
# bc = 0
# bb = len(c)
# while bc < bb:
#     d += c
# print(d)

s = 0
x = 1
while x < 100:
    s += x  #累加
    x += 2 #向后移2
print(s)