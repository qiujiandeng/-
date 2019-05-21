# 1，输入一个整数，代表正方形的宽和高，打印相应的正方形用ｆｏｒ语句实现
#     如：
#         请输入：５
#     打印：
#         1　2　3　4　5　
#         1　2　3　4　5　
#         1　2　3　4　5　
#         1　2　3　4　5　
#         1　2　3　4　5　


# s = int(input("请输入一个整数："))
# ss = s + 1
# cs = 1
# s1 = 1
# while cs <= s:

#     for ch in range(s1,ss):
#         print(ch,end=' ')
#     print()
#     cs += 1
#     s1 += 1
#     ss += 1


w = int(input("请输入："))
for line in range(w): #外重循环控制行数
    #内重循环打印一行
    for i in range(1,w+1):
        print(i,end=' ')
    print()  #换行