# 练习：
#     输入一个字符串，从尾向头输出这个字符串的字符
#     如：
#         请输入：hello
#     打印：
#     o
#     l
#     l
#     e
#     h
s = input("请输入一个字符串：")

# s2 = s[::-1] #反转字符串
# for c in s2:
#     print(c)

#while循环
i = len(s)-1
while i >= 0:
    print(s[i])
    i -= 1
