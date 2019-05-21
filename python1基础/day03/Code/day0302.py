# 练习：
# 	写一个程序，输入一段字符串，如果字符串不能为空，则把字符串的第一个字符的编码值打印出来！

# zfc = input("请输入一段字符串（不能为空）：")
# if zfc==' ':
#     print("您输入有误")
# else:
#     print("您输入的字符串第一个字符是：",min(zfc))



#老师：
s = input("请输入一段字符串：")
if s:
    print("字符串不为空")
    print(s[0],'的编码值是:',ord(s[0]))
    print(min(s),'dezhi:',ord(min(s)))#我的想法