# 练习５：
#     １．写一个程序，输入一个数，用ｉｆ语句计算这个数的绝对值，并打印此绝对值
#     ２．写一个程序，输入一个数，用条件表达式计算这个数的绝对值，并打印此绝对值

# x = float(input("请任意输入一个数："))

# if x > 0:
#     print(x,"的绝对值是:",int(x))
# elif x == 0:
#     print(x,"的绝对值式:",0)
# elif x < 0 :
#     print(x,"的绝对值是:",int(abs(x)))

 #反思错误           # y = float(input("请输入一个数："))
                    # y = y if y>0 else y
                    # print("绝对值是:",int(y))
                    # y = y if y==0 else y
                    # print("绝对值是:",int(y))
                    # y = y if y < 0 else y
                    # print("绝对是:",abs(y))


x = int(input("请输入一个数："))
#方法１
# if x < 0:
#     result = -x #用ｒｅｓｕｌｔ来记录结果
# else:
#     result = x
# print(x,'的绝对值是',result) 

#方法２
result = x
if result < 0:
    result = -result #符号取反
print(x,'的绝对值是:',result)
