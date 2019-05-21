#fethmany和fetchall一起用
import pymysql
db = pymysql.connect('localhost','root','123456','python',charset='utf8')
cur = db.cursor()
sql_select = "select * from t1;"
cur.execute(sql_select)
print("select语句查出的记录个数为:",cur.rowcount)

# sql_update = "update t1 set score = 100 where name='张飞'"
# data = cur.fetchmany(2)
# print("fetchmany(2)的结果:",data)
# for i in data:
#     print(i)

# data2 = cur.fetchall()
# print("fetchall()的结果为:",data2)
# for i in data2:
#     print(i)


db.commit()
cur.close()
db.close()
