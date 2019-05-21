
#面向对象方式
class Ellipse:  #定义椭圆类
    #class中的函数,称之为方法
    def __init__(self,a,b): #构造方法,创建对象会自动调用这个方法,self不用传(自动绑定e)
        self.a = a #属性:短半径
        self.b = b #属性:长半径
    
    def calc_len(self): #计算周长
        return 2 * 3.14 * self.a + 4 * (self.b-self.a)
    
    def calc_area(self):#计算面积
        return 3.14 * self.a * self.b

e = Ellipse(2.0,3.0)  #实例化的过程:创建椭圆对象
len = e.calc_len()   #获得椭圆的周长
area = e.calc_area()   #获得椭圆的面积
print("短半径=%f,长半径=%f,周长=%f,面积=%f"%(e.a,e.b,len,area))

q = Ellipse(3.0,4.0)
qlen = q.calc_len()
print('qlen',qlen)