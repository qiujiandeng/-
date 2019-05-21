
#创建账户类
class Accout:
    #创建构造函数
    def __init__(self,acct_no,acct_name,reg_date,
    acct_tpe,acct_status,balance):
        '''账号,户名,开户日期,类型,状态,余额'''
        self.acct_no = acct_no  #账号
        self.acct_name = acct_name  #户名
        self.reg_date = reg_date   #开户日期 
        self.acct_tpe = acct_tpe  #类型
        self.acct_status = acct_status #状态
        self.balance = balance      #余额

    #开始创建行为方法
    #存款
    def diposite(self,cunmoney):
        if self.acct_status == '正常':
            if self.acct_tpe == '储蓄卡':
                self.balance += cunmoney
                print("存了%s元,总余额是%s元"%(cunmoney,self.balance))
        else:
            print("您的账户已被%s,请解除%s后在试"%(self.acct_status,self.acct_status))

    #取款
    def draw(self,qukuan):
        if self.acct_status == '正常':
            if self.acct_tpe == '储蓄卡':
                if qukuan <= self.balance:
                    self.balance -= qukuan 
                    print("取了%s元,总余额是%s元"%(qukuan,self.balance))
                else:
                    print("您的余额不足")
            if self.acct_tpe == '贷记卡':
                print("您的是贷记卡,您贷了%s元"%qukuan)
                
        else:
            print("您的账户已被%s,无法取款%s元,请解除%s后在试"%(self.acct_status,qukuan,self.acct_status))
    #冻结账户
    def freeze(self):
        self.acct_status = '冻结'
        print("账户已冻结")
    #解除冻结
    def unfreeze(self):
        self.acct_status = '正常'
        print("账户已解除冻结")
    #挂失
    def report_loss(self):
        self.acct_status = '挂失'
        print("账号已挂失")
    #解除
    def relieve_loss(self):
        self.acct_status = '正常'
        print("账号解除挂失")
    #修改账户信息
    def modify_acct_info(self,acct_no,acct_name,reg_date,
    acct_tpe,acct_status):
        self.acct_no = acct_no  #账号
        self.acct_name = acct_name  #户名
        self.reg_date = reg_date   #开户日期 
        self.acct_tpe = acct_tpe  #类型
        self.acct_status = acct_status #状态
        # self.balance = balance      #余额
        print("账号:%s,户名:%s,开户日期:%s,类型:%s,状态:%s"%
        (self.acct_no,self.acct_name,self.reg_date,
        self.acct_tpe,self.acct_status))

#编写测试代码
if __name__ == '__main__':
    #创建实例,对象
    a = Accout('123','小李','2019.03.31','储蓄卡','正常',1000.00)
    a.diposite(100)
    a.freeze()
    a.draw(100)
    a.unfreeze()
    a.draw(99)
    a.report_loss()
    a.diposite(800)
    a.relieve_loss()
    a.diposite(800)
    a.modify_acct_info('456','小名','2018.8.8','储蓄卡','挂失')
    a.diposite(100)
    a.relieve_loss()
    a.diposite(0.48)
    a.draw(3300)
    a.draw(1800)



