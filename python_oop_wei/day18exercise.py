# 1.写一个类Bictcle(自行车)类,
#   有run方法,调用时显示骑行历程km
#     class Bictcle:
#         def run(self,km):
#             print("自行车骑行了",km,'公里')

# 2.在写一个类EBicycle(电动自行车)类,在Bicycle类的自出上添加电池点亮volume属性,
#   有两个方法:
#         1.file_charge(self,vol) 用来充电,vol为电量,
#         2.run(km) 方法每骑行10km消耗电量1度
#           同时显示当前电量,当当电量耗尽时,则调用Bicycle的run方法骑行

class Bictcle:
    def __init__(self,vol=0):#需要初始化电量
        self.vol = vol  #self.vol用来记录电量

    def fill_charge(self,vol):#充电和电量
        self.vol += vol

    def run(self,km):
        print("自行车骑行了",km,'公里')




class EBicycle(Bictcle):
    def __init__(self,vol):
        self.vol = vol
        print("当前电量为%s,可以行驶%s公里"%(self.vol,self.vol*10))

    def run(self,km):
        e_km = min(self.vol * 10 , km)#电动总数,和KM取最小值

        if e_km > km:#如果电池电量够行驶km公里
            print("电动骑行了",e_km,'公里')
            self.vol -= e_km / 10
        else:
            self.vol -= e_km / 10
            if self.vol == 0 and e_km == 0:
                print("电动骑行了",e_km,'公里')
            
            if km-e_km > 0:
                print("电动骑行了",e_km,'公里',end=',')
                super().run(km - e_km)
            
        print("本次剩余电量是",self.vol)




        # self.km = km
        # if self.vol > 0:
        #     if self.km >= self.vol*10:
        #         print('电动骑行了%s公里'%self.km)
        
        
        


    
b = Bictcle()
b.run(10) #自行车骑行了10公里

e = EBicycle(5)
# e.run(100)
e.run(51)