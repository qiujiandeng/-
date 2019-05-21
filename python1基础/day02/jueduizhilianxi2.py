# 练习５：
#     １．写一个程序，输入一个数，用ｉｆ语句计算这个数的绝对值，并打印此绝对值
#     ２．写一个程序，输入一个数，用条件表达式计算这个数的绝对值，并打印此绝对值


 #反思错误           # y = float(input("请输入一个数："))
                    # y = y if y>0 else y
                    # print("绝对值是:",int(y))
                    # y = y if y==0 else y
                    # print("绝对值是:",int(y))
                    # y = y if y < 0 else y
                    # print("绝对是:",abs(y))


x = int(input("请输入一个数："))
result = -x if x < 0 else x
print(x,'的绝对值是:',result)
