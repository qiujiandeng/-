# exercise5:
#     试用自己的方法实现myenumerate,功能与enumerate完全相同
#     def myenumerate(iterable,start=0):
#         .....#此处自己实现
#     L = [3,5,8,10]
#     for i,v in myenumerate(L):
#         print('索引为',i,'的元组值为',v)

#方法1 用whlie 语句实现
# def myenumerate(iterable,start=0):
#     it = iter(iterable) #拿到迭代器
#     while True:
#         try:
#             v = next(it)  #拿到一个值
#             yield(start,v)
#             start += 1
#         except StopIteration:
#             return
# L = [3,5,8,10]
# for i,v in myenumerate(L):
#     print('索引为',i,'的元素值为',v)

#方法2 用for语句实现
def myenumerate(iterable,start=0):
    for v in iterable:
        yield(start,v)
        start +=1
L = [3,5,8,10]
for i,v in myenumerate(L):
    print('索引为',i,'的元素值为',v)