# exercize1:
#     写一个生成器函数myeven(begin,end),用来生成从begin开始到end结束的所有偶数(不包括end)
#     如:
#         def myeven(begin,end):
#             ....此处自己实现
        
#         for x in myeven(1,10):
#             print(x)  #打印2,4,6,8
#         L = [x ** 2 for x in myeven(4,9)]
#         print(L)   #[16,36,64]

# def myeven(begin,end):
#     l = []
#     for x in range(begin,end):
#         if x % 2==0:
#             l.append(x)
#     return l
# l1 = myeven(2,10)
# print(l1)

#老师的
def myeven(begin,end):
    i = begin
    while i < end:
        if i % 2 ==0:
            yield i
        i += 1
for x in myeven(1,10):
    print(x)
L = [x ** 2 for x in myeven(4,9)]
print(L)