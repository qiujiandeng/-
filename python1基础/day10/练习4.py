# 练习4:
#     写一个lambda 表达式
#         fx  = lambda n : ......
#     此表达式创建的函数判断n这个数的2次方+1能否被5整除,如果能被整除
#     返回True,否则返回False
#     如:
#         print(fx(3))  #返回True
#         print(fx(4))  #返回False

fx = lambda n : (n **2 + 1 ) % 5 == 0 
#fx = lambda n : bool(n **2 + 1 ) % 5 == 0 
print(fx(3))
print(fx(4))