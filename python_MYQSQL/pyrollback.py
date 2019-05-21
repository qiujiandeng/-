import pymysql

db = pymysql.connect('localhost','root','123456','db3',charset='utf8')

cur = db.cursor()

try:
    cur.execute("update CCB set money=95000 \
                where name='转钱';")
    cur.execute("update ICBC set money=7000 \
                where name='借钱'")
    db.commit()
    print("转账成功")
except Exception as e:
    print(e)
    db.rollback

# db.commit()
cur.close()
db.close()