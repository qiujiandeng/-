    # CarStore类:  租车店
    #     属性:
    #         cars        所有车辆列表  
    #         customers   所有客户列表
    #     方法:
    #         __load_cars()   加载所有车辆信息
    #         __load_customers()   加载所有客户信息
    #         print_cars_info()    打印所有车辆信息
    #         find_car()           查找车辆
    #         add_car()            添加车辆
    #         del_car()            删除汽车
    #         lend()               租车
    #         back()               还车
from car import *
from customer import *
class CarSrore:
    def __init__(self):
        # cars = [x for x in Car.__str__]
        self.cars += [x for x in Customer.__str__]
        # customers = [x for x in Customer.__str__]
        self.customers += [x for x in Customer.__str__]
        
    
    def __load_cars():#加载所有车辆信息 
        
        
