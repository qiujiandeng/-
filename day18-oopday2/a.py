class A:
    def __init__(self,name):
        self.name = name

    def __repr__(self):  #重写__repr__方法
        #返回的是B('jerry','0001')
        return "B('%s','%s')" % (self.name,self.id)

    # def __str__(self):  #重写__str__函数
    #     return "name = %s" %self.name

class B(A):
    def __init__(self,name,id):
        super().__init__(name)  #B里没有name属性,需要调用调用父类构造方法
        self.id = id #B类只创建了 id属性被创建

    def __repr__(self):  #重写__repr__方法
        #返回的是B('jerry','0001')
        return "B('%s','%s')" % (self.name,self.id)

    # def __str__(self):  #重写__str__函数
    #     return "name = %s , id = %s"%(self.name,self.id)

b = B("Jerry","00001")
print(b)


# str_obj = repr(b)
# print(str_obj)
# new_obj = eval(str_obj)  #通过python解释器还原对象
# print(new_obj)



# print(b)   #在B子类中重写__str__方法,所以可以直接打印
# str_obj = str(b)  #将B对象转换成字符串
# print(str_obj)