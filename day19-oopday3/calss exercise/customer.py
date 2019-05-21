# Customer类:客户
#     属性:
#         cust_id    客户编号
#         cust_name  客户姓名
#         tel_no     客户电话
#     方法:
#         __str__()  

class Customer:
    def __init__(self,cust_id,cust_name,tel_no):
        self.cust_id = cust_id    #客户编号
        self.cust_name = cust_name #客户姓名
        self.tel_no = tel_no      #客户电话
    
    def __str__(self):
        ret = ''
        ret += '客户编号:'
        ret += str(self.cust_id)
        ret += ' '
        ret += '客户姓名:'
        ret += str(self.cust_name)
        ret += ' '
        ret += '客户电话:'
        ret += str(self.tel_no)
        ret += ' '
        return ret
# L = Customer('0001','小李',13512345678)
# L2 = Customer('0002','小张',1350987654)
# print(L)
# L1 = []
# L1.append(L)
# L1.append(L2)
# for x in L1:
#     print(x)