# 练习:
#     写一个程序,输入一个字符串,写程序统计出这个字符串的字符个数的字符种类
#     如:
#         请输入:ABCDABCABA
#     输出结果为:
#         字符 A:4次
#         字符 B:3次
#         字符 C:1次
#         字符 D:2次
#     (不要求输出的顺序)

s = input("请输入:")
#统计字符的个数:
#如果第一次出现这个字符:
#    用这个字符创建字典的键,值为1
#如果第二次或之后出现这个字符,直接将键对应的值加1

d = {}
for ch in s:
        if ch not in d :
                d[ch] = 1 
        else:
                d[ch] += 1
# print(d)
for k in d :
        print("字符",k,':',d[k],'次')
        






# t ={} #空字典
# L = []
# x = input("输入一个字符串")
# for ch in x:

#         if ch not in t:
#                 t[ch] = 1

#         else:


#                 t[ch] += 1

# print(t)
# print(L)