import pymysql

#打开数据库链接(建立数据库链接)  connect:连接
db = pymysql.connect('localhost','root','123456',charset='utf8') #db随便取的变量名

#创建一个游标对象 cursor : 光标
cur = db.cursor()

#创建库python  execute : 执行
cur.execute("create database if not exists python;")
#创建一个库,如果不exists(存在) 就创建python库

#切换库 光标.执行  平常的sql语句
cur.execute("use python;")

#创建表 t1
cur.execute("create table if not exists t1(\
    id int primary key,\
    name varchar(20),\
        score tinyint unsigned);")

#在t1中 插入五条记录
cur.execute("insert into t1 values\
            (1,'貂蝉',88),\
            (2,'赵子龙',100),\
            (3,'诸葛亮',86),\
            (4,'张飞',60),\
            (5,'司马懿',99);")

#提交到数据库
db.commit()

#关闭游标
cur.close()

#关闭数据库
db.close()