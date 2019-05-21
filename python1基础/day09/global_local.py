#此示例示意全局变量的定义
a = 100
b = 200

def fx(c):
    d = 400
    print(a,b,c,d)#ab里面没有就在外面找,里面有就在里面找

fx(300)
print('a=',a)
print('b=',b)
# print('c=',c)#外面没有报错