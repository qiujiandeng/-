#此示例示意 类方法的定义方法和用法
class Car:
    count = 0#类变量
    @classmethod  #这个一个类
    def getInfo(cls):
        return cls.count

c1 = Car()   #创建一个对象
c1.count = 100
v = c1.getInfo()  #0 或者 100?
print(v)   #0