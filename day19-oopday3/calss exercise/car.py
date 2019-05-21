    # Car类: 汽车
    #     属性:
    #         car_id   车辆id号
    #         name     车辆名称
    #         is_lend  是否出租(状态)
    #         price    每天单价
    #         start_date  起租日期
    #         end_date    租赁终止日期
    #     方法:
    #         __str__()

#创建字典

class Car:
    #构造
    def __init__(self,car_id,name,is_lend,price,start_date,end_date):
        self.car_id = car_id   #车辆id号
        self.name = name     #车辆名称
        self.is_lend = is_lend  #是否出租(状态)
        self.price = price    #每天单价
        self.start = start_date # 起租日期
        self.end_date = end_date    #租赁终止日期
    
    def __str__(self):
        ret = ''
        ret += '车辆id号:'
        ret += str(self.car_id)
        ret += ' '
        ret += '车辆名称:'
        ret += str(self.name)
        ret += ' '
        ret += '是否出租状态:'
        ret += str(self.is_lend)
        ret += ' '
        ret += '每天单价:'
        ret += str(self.price)
        ret += ' '
        ret += '起租日期:'
        ret += str(self.start)
        ret += ' '
        ret += '租赁终止日期:'
        ret += str(self.end_date)
        ret += ' '
        return ret
if __name__ == "__main__":
    L = Car('0001','丰田','否',88,'0','0')
    L1 = Car('0002','长安','是',56,'2018-02-05','2018-02-07')
    print(L)
    # S.append(L)
    # S.append(L1)
    # print(L)
    # print(L1)
    # for x in Car.:
    #     print(x)
                