# 3.<<学生信息管理项目>>
#       输入任意个学生的姓名,年龄,成绩,每个学生的信息存入字典,然后放入列表中,
#       每个学生的信息需要手动输入,当输入姓名为空时,结束输入
#       如:
#          请输入姓名:tarena
#          请输入年龄:20
#          请输入成绩:99
#          请输入姓名:name2
#          请输入年龄:18
#          请输入成绩:88
#          请输入姓名:<回车> 结束输入
        #  内部存储格式如下:
        #  [{'name':'tarena','age':20,'score':99},
        #  {'name':'name2','age':18,'score':88}]
        #  打印上述此列表
        #  然后再用表格的形式打印学生信息如下:
        #  +---------+--------+----------+
        #  |   姓名   |  年龄   |   成绩   |
        #  +---------+--------+----------+
        #  |  tarena |   20   |    99    |
        #  |  name2  |   18   |    88    |
        #  +---------+--------+----------+

xuesheng = {}  #创建空字典
z = [] #创建总字典序列
ml = ['name','age','score']

xx = [] #临时姓名列表#年龄列表#成绩列表
xx2 = []#存储姓名列表#年龄列表#成绩列表
 
while True:

    x = input("请输入学生姓名:")
    
    if len(x) > 0:
        xx.append(x)
        xx2.append(x)
        x1 = input("年龄:")
        if len(x1) == 0:
            print("退出系统")
            break
            
        xx.append(x1)
        xx2.append(x1)
        x2 = input("成绩")
        if len(x2) > 0:
            
            xx.append(x2)
            xx2.append(x2)
            xuesheng = {ml[i]:xx[i] for i in range(len(ml))}
            z.append(xuesheng)
            xx = []
            xuesheng = {}
            
        
        else:
            print("退出系统")
            break
    else:
        print("退出系统")
        break

zz1 = 0
while zz1 < len(z):
    print(z[zz1])
    zz1 += 1
print('总列表',z)

qq = []
for ch in range(1000):
    qq.append(ch)


print("学生成绩信息打印如下:")


print('+----------+---------+-----------+')
print('|   姓名   |   年龄  |    成绩   |')
print('+----------+---------+-----------+')

for ch in range(len(xx2)):
    if ch in qq[::3]: 
        print('|',xx2[ch].center(8),'|',end='')
    if ch in qq[1::3]:
        print( xx2[ch].center(8),'|',end='  ')
    if ch in qq[2::3]:
        print(xx2[ch].center(8),'|')




print('+----------+---------+-----------+')