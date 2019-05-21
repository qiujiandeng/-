#truck.py
#卡车类,演示运算符的重载
class Truck:
    def __init__(self,load):
        self.load = load #载重属性
    
    def __add__(self,value):
        print("__add__()被调用")
        return Truck(self.load + value)

    def __str__(self):
        # print("__str__()被调用")
        return "strload:%d" % self.load
    
    def __mul__(self,rhs):  #重载乘号运算符
        # print("__mul__调用.乘法")
        return Truck(self.load * rhs)
    
    #反向+运算符重载, 支持 3 + truck操作
    def __radd__(self,value):
        print("__radd__方法被调用")
        return Truck(self.load + value)
    
    def __iadd__(self,value):#复合+=运算符
        return Truck(self.load + value)

    def __gt__(self,other): #重载 > 运算符
        return (self.load > other.load)

    def __lt__(self,other): #重载 < 运算符
        if self.load < other.load:
            return True
        else:
            return False

if __name__ == "__main__":
    t1 = Truck(20)
    t2 = Truck(25)
    print(t1 > t2)  #调用__gt__()
    print(t1 < t2)  #调用__lt__()





    # t = Truck(20)
    # print(t)
    # t2 = t + 1  #没有重写就会报错
    # t2 = 1 + t  #调用__radd__方法,反向+运算
    # t3 = t * 4
    # t += 1
    # print(t)
    # print(t2)
    # print(t3)
    # print(str(t))