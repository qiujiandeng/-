# for 语句语法:
#     for 变量列表 in 可迭代对象 :
#           语句块1
#     else:
#            语句块2

# s = "ABCDE"

# for ch in s :
#     print("ch绑定----->",ch)
# else:
#     print("for语句迭代访问结束")

# print("程序退出")

# 练习：
#     任意输入一段字符串
#     １）计算出这个字符串中空格的个数，并打印这个个数
#         （要求使用ｆｏｒ语句，　不允许使用s.count方法）
#     ２）计算出字符串中全部英文字母（a~z和Ａ～Ｚ）的个数，
#         并打印这个个数：
#     完成上题后思考：
#         能否用ｗｈｉｌｅ语句实现上述功能

s = input("请输入一段字符串：")

shu = 0
zm = 0
i = 0  #i代表字符串的索引
while i <len(s):#索引不允许大于等于ｌｅｎ（ｓ）
    ch = s[i]   #ch绑定每次遍历的字符
    #统计个数
    if ch == ' ':
        shu += 1
    if 'A' <= ch <= 'Z' or 'a' <= ch <= 'z':
        zm += 1
    i +=1

print("空格的个数",shu)
print("您输入的英文字母共有：",zm)






#遍历输入的字符串，当有字符为‘　’时，将ｓｈｕ做加１操作
# for ch in s:
#     if ch == " ":
#         shu += 1
# else:
#     print("空格的个数有:",shu)


# dzimu = 0
# xzimu = 0
# zgs = 0
# for ch in s:
#     if 65 <= ord(ch) <= 65+26:
#         dzimu += 1
#         zgs += 1
#     if 97 <= ord(ch) <= 97+26:
#         xzimu += 1
#         zgs += 1
# print("您输入的大写字母有:",dzimu,"个")
# print("您输入的小写字母有:",xzimu,"个")
# print("您输入的英文字母共有：",zgs,"个")
