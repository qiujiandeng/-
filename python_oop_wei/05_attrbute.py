class Dog:
    pass

dog1 = Dog()
hasattr(dog1,'color')






# # print(dog1,color)   #会出错,没有这个颜色
# print(getattr(dog1,'color','没有颜色'))  #没有颜色 如果Dog里color有参数,就会返回Dog里的
# dog1.color = '白色'
# print(getattr(dog1,'color','没有颜色'))  #白色

# print(getattr(dog1,'kinds',None)) #如果里面没有定义返回None,有则返回该值.可以用来判断