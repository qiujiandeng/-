from pymongo import MongoClient

conn = MongoClient('localhost',27017)
db = conn.stu
myset = db.class0

#索引聚合

# *****************索引****************

# index_name = myset.create_index([('name',1)])
#添加索引选项,创建不同类型索引
# index_age = myset.create_index('age',name='Age',sparse=True)
# myset.drop_index([('name',1)])e
# myset.drop_index('Age')  #删除Age索引
# myset.drop_indexes() #删除所有索引

# **********************聚合操作*****************
# l = [{'$group':{'_id':'$gender','num':{'$sum':1}}}]
# cursor = myset.aggregate(l)
# for i in cursor:
#     print(i)



#查看索引
# for i in myset.list_indexes():
#     print(i)



conn.close()