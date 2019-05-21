#此py存储mysql命令中经常使用的语句,作为方法

from pymysql import *

class MysqlPython:
    def __init__(self,host,port,db,user,passwd,charset='utf8'):
        self.host = host
        self.port = port
        self.db = db
        self.user = user
        self.passwd = passwd
        self.charset = charset

    #定义一个打开的方法
    def open(self):
        self.con = connect(host=self.host, \
                            port = self.port, \
                            db = self.db,user=self.user,passwd=self.passwd,\
                            charset=self.charset)
                            
        self.cursor = self.con.cursor()
    
    #定义一个关闭
    def close(self):
        self.cursor.close()
        self.con.close

    #execute执行
    def zhixing(self,sql):
        self.open()
        self.cursor.execute(sql)
        self.con.commit()
        self.close()
    
    def all(self,sql):
        try:
            self.open()
            self.cursor.execute(sql)
            data = self.cursor.fetchall()
            self.close()
            return data
        except Exception as e:
            print(e)