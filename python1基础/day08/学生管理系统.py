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
def input_student():
    L = []  #创建一个列表,存储学生数据的字典
    while True:
        n = input("请输入姓名:")
        if not n: #如果用户输入空字符串就结束输入
            break
        a = int(input("请输入年龄:"))
        s = int(input("请输入成绩:"))
        d = {}#一定要每次都创建一个新的字典
        d['name'] = n
        d['age'] = a
        d['score'] = s
        L.append(d)  #把d加入到列表L中
    return L

def output_student(L):
    print('+---------------+----------+----------+')
    print('|     姓名      |   年龄   |   成绩   |')
    print('+---------------+----------+----------+')
    for d in L:
        name = d['name']
        age = str(d['age'])
        score = str(d['score'])
        zhongwen = 0
        for ch in name:
            if 0x4e00 <= ord(ch) <= 0x9fa5:
                zhongwen += 1
        print("|%s|%s|%s|"%(name.center(15-zhongwen),age.center(10),score.center(10)))

        # print("|%s|%s|%s|"%(name.center(15),age.center(10),score.center(10)))
    # print('|  tarena |   20   |    99    |')
    # print('|  name2  |   18   |    88    |')
    print('+---------------+----------+----------+')

infos = input_student()
print(infos) #打印实参infos打印表格
output_student(infos)

