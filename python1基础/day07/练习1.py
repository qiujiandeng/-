
# 练习：  
#     写程序,实现一下要求:
#     1,将如下数据形成一个字典seasons
#     '键'           '值'
#     1------------->'春季有1,2,3月'
#     2------------->'夏季有4,5,6月'
#     3------------->'秋季有7,8,9月'
#     4------------->'冬季有10,11,12月'
#     让用户输入一个整数代表这个季度,打印这个季度的信息如果用户输入的信息不在字典内,则打印"信息不存在"

t = {1:'春季有1,2,3月',2:'夏季有4,5,6月',3:'秋季有7,8,9月',4:'冬季有10,11,12月'}
#创建字典的键和值

#等待用户输入一个整数查询这些季度
x = int(input("请输入您要查询的季度(1-4):"))

if  x in t:
    print(t[x])
else:
    print("信息不存在")