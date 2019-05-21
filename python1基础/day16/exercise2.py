
# 练习2:
#     print()  函数是如何实现的?
#       能否自己实现一个myprint函数与內建功能相同
#     如:
#         print(*args,sep=' ',end='\n',file=sys.stdout,
#                flush=False

import sys

def myprint(*args,sep=' ',end='\n',file=sys.stdout,flush=False):
    flag = False #当第一次循环时候,将此变量置为True
    for x in args:
        if flag: #判断是否是第二次或之后打印
            file.write(sep) #如果是第二次打印,则执行此语句
        file.write(str(x))#要将所有数据转为字符串
        flag = True
        #打印最终的end
    file.write(end)

myprint("hello world!")
myprint(1,2,3,4)
myprint(5,6,7,8,sep='#')    
myprint(1,2,3,4,sep=',',end='\n')