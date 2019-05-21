import pymysql
#db变量绑定pymysql
db = pymysql.connect('localhost','root','123456','python',charset='utf8')
#cur对象名绑定pymysql中的cursor 光标
cur = db.cursor()
sql_select = 'select * from t1;'
cur.execute(sql_select) #查询的数据都放到cur.execute的对象里了
#取出来的话需要用到fetchone用对象data绑定
data = cur.fetchone()
print('fetchone的结果为:',data)
#数据提交
db.commit()
#关闭光标
cur.close()
#关闭数据库
db.close()

