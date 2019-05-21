# 练习：
#     已知有列表：
#         Ｌ＝ [3,5]
#     1) 用索引和切片操作，将原列表改变为：
#         Ｌ＝　［１，２，３，４，５，６】
#     ２，将列表反转，删除最后一个元素，打印此列表：
#     。。。。
#     print(L)   #[6,5,4,3,2]

#     day0601.py


L = [3,5]   #L列表等于3，5

L[0:0] = [1,2]  #索引开始0结束　＝　【１，２】
print(L)    #1,2,3,5
L[3:3] = [4]    #切片第三位中间插入　4
print(L)    #输出　1，2，3，4，5
L[len(L):] = [6]    #索引Ｌ的长度开始：ｅｎｄ　插入6
print(L)            #输出1，2，3，4，5，6

L = L[::-1]         #L=L的方向索引：：-1
print(L)            #输出6，5，4，3，2，1

del L[-1]           #删除Ｌ的-1位
print(L)            #输出6，5，4，3，2，