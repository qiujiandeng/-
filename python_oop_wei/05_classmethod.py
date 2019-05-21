#此示例示意 类方法的定义方法和用法
class Car:
    count = 0#类变量
    @classmethod
    def getTotalCount(cls): #cls绑定的是Car
        '''此方法为类方法,
        第一个参数为cls,
        代表调用此方法的类'''
        return cls.count

    @classmethod    
    def updeteCount(cls,number):
        cls.count += number

print(Car.getTotalCount())  #用类来调用类方法
# Car.count += 1  #面向对象思想不提倡直接操作属性
Car.updeteCount(1) 

print(Car.getTotalCount())

c1 = Car()   #创建一个对象
c1.updeteCount(100)  #Car类的示例也可以调用类方法
print(c1.getTotalCount()) #101