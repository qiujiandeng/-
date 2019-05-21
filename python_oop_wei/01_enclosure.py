#此示例示意使用私有属性的私有方法:
class A:
    def __init__(self):
        self.__P1 = 100 #__p1为私有属性,在类的外部不可访问
    def test(self):
        print(self.__P1) #可以访问
        self.__m1() #需要加上self(自己的)
    
    def __m1(self):
        '''我是私有方法,只有我自己的类中发的方法才能调用'''
        print('我是A类的m1方法!')
a = A()
# print(a.__p1)  #在类外看不到__p1属性,访问失败,AttributeError:“A”对象没有属性“_p1”
a.test() #调用A类的函数可以调用
# a.__m1()  #出错,,无法调用私有方法
