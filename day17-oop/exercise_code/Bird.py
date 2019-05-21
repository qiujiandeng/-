#定义一个父类

#定义鸟类
class Bird:
    #构造
    def __init__(self,name):
        self.name = name
    def eat(self):  #吃方法
        # print(self.name,"开始吃东西")
        print("%s正在吃饭"%self.name)
    
    def fly(self):  #飞行
        # print(self.name,"起飞")
        print("%s正在飞行"%self.name)

    def reproduction(self): #繁殖
        # print(self.name,"开始繁殖")
        print("%s是卵生"%self.name)

class Eagle(Bird):#创建老鹰类,继承自Bird
    def eat(self):
        print("我是%s,我喜欢吃肉"%self.name)
    
    def fly(self):
        print("我是%s,飞的又高又快"%self.name)

class Ostric(Bird):#创建鸵鸟类,继承自Bird
    def fly(self):
        print("我是%s,太重了不能飞"%self.name)
    
    def eat(self):
        print("我是%s,我是杂食动物"%self.name)

if __name__ == '__main__':
    eagle = Eagle("老鹰")
    eagle.eat()
    eagle.fly()
    eagle.reproduction()
    print("------------------------------")
    ostric = Ostric("鸵鸟")
    ostric.eat()
    ostric.fly()
    ostric.reproduction()