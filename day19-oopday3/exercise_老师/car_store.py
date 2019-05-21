class Car: #车辆类
    def __init__(self,car_id,name,price,is_lend):
        self.car_id = car_id   #车辆id号
        self.name = name     #车辆名称
        self.is_lend = is_lend  #是否出租(状态)
        self.price = price   #每天单价
        self.start_date = '' # 起租日期
        self.end_date = ''   #租赁终止日期
        self.cust_id = ''    #租车客户编号
    def __str__(self):
        ret = '车辆编号:%s,名称:%s,单价:%.2f,是否出租:%s'%(self.car_id,self.name,self.price,self.is_lend)
        return ret

class Customer:#客户类
    def __init__(self,cust_id,cust_name,tel_no):
        self.cust_id = cust_id
        self.cust_name = cust_name
        self.tel_no = tel_no
    
    def __str__(self):
        ret = '客户编号:%s,客户名称:%s,电话:%s'%(self.cust_id, self.cust_name, self.tel_no)
        return ret


class CarStore:#租车店
    def __init__(self):
        self.cars = [] #车辆列表
        self.customers = [] 
        self.__load_cars()  #加载车辆列表 创建对象的时候就加载此函数
        self.__load_customers() #加载客户信息 创建对象的时候就加载此函数

    def __load_cars(self):
        car1 = Car('1','GOLF',400.00,'否')
        car2 = Car('2','凯越',350.00,'否')
        car3 = Car('3','奥迪',1200.00,'否')
        car4 = Car('4','凯美瑞',800.00,'否')
        car5 = Car('5','宝来',450.00,'否')


        self.cars.append(car1)
        self.cars.append(car2)
        self.cars.append(car3)
        self.cars.append(car4)
        self.cars.append(car5)
    
    def __load_customers(self):
        cust1 = Customer('C0001','张大大','15811223344')
        cust2 = Customer('C0002','李小小','13232223344')
        cust3 = Customer('C0003','赵四','13923233344')
        self.customers.append(cust1)
        self.customers.append(cust2)
        self.customers.append(cust3)

    def print_cars_info(self): #打印车辆信息
        for x in self.cars:#遍历车辆列表
            print(x)

    def print_customers_info(self):#打印客户信息
        for x in self.customers:#遍历客户列表
            print(x)

    def find_car(self,car_id):#根据车辆编号查询
        for car in self.cars:#遍历车辆列表
            print(car.car_id)
            if car.car_id == car_id: #编号相等
                print(car)
                return
        print("未找到车辆信息")
        return #就是给程序员看的
    
    def add_car(self,car): #添加车辆,car为Car的对象
        if isinstance(car, Car):#car是Car类的实例
            self.cars.append(car)
        else:
            print('对象类型有误')
        #可以增加id号是否存在的逻辑判断
        return

    def del_car(self, car_id):#根据车辆编号删除
        for car in self.cars:
            if car.car_id == car_id:
                self.cars.remove(car) #删除对象
        return
    
    def lend(self,car_id, cust_id, start_date, end_date):#租车
        for car in self.cars:
            if car.car_id == car_id:
                if car.is_lend == '是':
                    print('改车辆已经出租')
                    return
                else:#为出租
                    #car.is_lend == '是'
                    setattr(car,'is_lend','是')#改出租状态
                    setattr(car,"cust_id",cust_id)  #租车客户编号
                    setattr(car,"start_date", start_date) #起租日期
                    setattr(car,"end_date",end_date)    #租赁终止日期
                    print("车辆出租完成")
                    return
        print("未找到车辆信息")
        return

    def back(self,car_id):#换车
        for x in self.cars:
            if x.car_id == car_id:
                if x.is_lend == '是':
                    setattr(x,'is_lend','否')
                    setattr(car,"cust_id",'')  #清空租车客户编号
                    setattr(car,"start_date", '') #清空起租日期
                    setattr(car,"end_date",'')    #清空租赁终止日期
                    print("换车成功")
                else:
                    print('该车还未出租,操作失败')

if __name__ == '__main__':
    car_store = CarStore() #实例化租车店对象 创建对象
    car_store.print_cars_info() #打印车辆信息
    # car_store.print_customers_info()
    print('')
    car_store.lend('3','Z0001','2018-08-08','2018-08-10')
    car_store.print_cars_info() #打印车辆信息

    car_store.back('3')
    car_store.print_cars_info() #打印车辆信息






    # car_store.find_car("5")
    # car = Car('6','宝马',1800,'否')
    # car_store.add_car(car)  #将car对象添加到列表中
    # car_store.print_cars_info()





    # print("")
    # car_store.del_car('5')
    # car_store.print_cars_info()
