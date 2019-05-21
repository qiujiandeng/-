
# 练习：
#     １，输入一个整数，代表树干的高度，打印如下一个树“圣诞树”
#     如：
#         请输入：２
#     打印：　
#      *
#     ***
#      *
#      *
#      如：
#         请输入：3
#     打印
#       *
#      ***
#     *****
#       *
#       *
#       *



# print("输入一个整数，代表树干的高度")
# sg = int(input("请输入一个整数："))#树干高度

# sp = 1  #地面高度

# kg = sg - 1

# xx = 1

# sgkg = sg -1

# sggd = 1

# while sp <= sg:
#     print(' '*kg,'*'*xx)
#     sp += 1
#     kg -= 1
#     xx += 2
# while sggd <= sg:
#     print(' '*sgkg,'*')
#     sggd += 1


h = int(input("请输入树干的高度："))

#打印树冠部分
w = 2 * h -1 #w 代表树冠最大下层叶子的星号个数
for line in range(1,h+1):#line代表行号
    stars = 2 * line -1 #算出星号个数
    s = '*' * stars
    print(s.center(w))

#打印树干部分
for _ in range(h):
    print(' ' * (h-1) + '*')