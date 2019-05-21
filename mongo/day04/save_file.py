from pymongo import MongoClient
import bson.binary

conn = MongoClient('localhost',27017)
db = conn.image
myset = db.mm

# ****************存储**********************
#读取图片内容
# with open('timg.jpeg','rb') as f:
    # data = f.read()

# #做格式转换
# content = bson.binary.Binary(data)
# #插入数据库
# myset.insert_one({'filename':'mm.jpg','data':content})


# **************提取**********************
img = myset.find_one({'filename':'mm.jpg'})

#写入本地
with open('test.jpg','wb') as f:
    f.write(img['data'])
    



conn.close()