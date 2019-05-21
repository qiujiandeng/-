# 2.写一个lambda 表达式来创建九,此函数返回两个形参变量的最大值
#     daf mymax(x,y):
#         ....
#     mymax = lambda ....
#     print(mymax(100,200))  #200
#     print(mymax("100","20"))  #20 <---注意这是字符串

# def mymax(x,y):     #return x if x > y else y
#     zuida = x
#     if y > x :
#         zuida = y
#     return zuida


mymax = lambda x,y: x if x > y else y
print(mymax(100,200))  #200
print(mymax("100","20"))  #20 <---注意这是字符串