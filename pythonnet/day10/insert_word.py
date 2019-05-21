import pymysql

f = open("dict.txt")

db = pymysql.connect('localhost','root','123456','dict')
cursor = db.cursor()

for line in f:
    #先切割
    tmp = line.split(' ')
    word = tmp[0]
    #用空格拼接,去除两边空格
    mean = ' '.join(tmp[1:]).strip()

    sql = 'insert into words (word,mean)\
        values("%s","%s")'%(word,mean)
    try:
        cursor.execute(sql)
        db.commit()
    except:
        db.rollback()
f.close()