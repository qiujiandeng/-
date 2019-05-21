from student import Student

def input_student():
    L = []  #创建一个列表,存储学生数据的字典
    while True:
        n = input("请输入姓名:")
        if not n: #如果用户输入空字符串就结束输入
            break
        try:
            a = int(input("请输入年龄:"))
            s = int(input("请输入成绩:"))
        except ValueError:
            print("您的输入有错,请重新输入!!")
            continue
        d = Student(n,a,s)#用对象封装
        # d = {}#一定要每次都创建一个新的字典
        # d['name'] = n
        # d['age'] = a
        # d['score'] = s
        L.append(d)  #把d加入到列表L中
    return L

def output_student(L):
    print('+---------------+----------+----------+')
    print('|     姓名      |   年龄   |   成绩   |')
    print('+---------------+----------+----------+')
    for d in L:
        n,a,s = d.get_infos()
        name = n
        age = str(a)
        score = str(s)
        zhongwen = 0
        for ch in name:
            if 0x4e00 <= ord(ch) <= 0x9fa5:
                zhongwen += 1
        print("|%s|%s|%s|"%(name.center(15-zhongwen),age.center(10),score.center(10)))

        # print("|%s|%s|%s|"%(name.center(15),age.center(10),score.center(10)))
    # print('|  tarena |   20   |    99    |')
    # print('|  name2  |   18   |    88    |')
    print('+---------------+----------+----------+')


def mydelxs(a):#创建删除学生信息的函数
    x = input("请输入你要删除的学生信息:")
    for i in range(len(a)):#从0开始索引
        if a[i].is_name(x):
            del a[i]
            print('已成功删除:',x)
            return True
    else:
        print('未找到名为:%s的学生'%(x))
    # xx = 0
    # for ch in a:
    #     if x in ch['name']:
    #         del a[xx]
    #         print("已删除",x,"学生信息")
    #     if x not in ch:
    #         xx += 1

#老师的删除学生            
# def delete_student(L):
#     name = input('请输入要删除学生的名字')
#     i = 0 #i代表列表的索引
#     while i < len(L):
#         d = [i]  #d板绑定字典
#         if d['name'] == name:
#             del L[i]
#             print('删除',name,'成功!')
#             break
#     else:
#         print('删除失败')

def xiugai(c):#创建修改学生成绩的函数
    name = input("请输入你要修改成绩的学生:")
    xx = 0
    for d in c:
        # if x in ch['name']:
        if d.is_name(name): #添加is_name方法
            score = int(input("请输入您要修改的成绩:"))
            # d['score'] = score
            d.set_score(score)
            print('已将',name,'学生成绩修改为:',score)

            
def cj_gao_di(L):
    # sorted_x = sorted(L, key=lambda x : x['score'],reverse=True)
    sorted_x = sorted(L, key=lambda x : x.get_score(),reverse=True)
    output_student(sorted_x)

def cj_di_gao(L):
    # sorted_x = sorted(L, key=lambda x : x['score'],reverse=False)
    sorted_x = sorted(L, key=lambda x : x.get_score(),reverse=False)
    output_student(sorted_x)

def nl_gao_di(L):
    # sorted_x = sorted(L, key=lambda x : x['age'],reverse=True)
    sorted_x = sorted(L, key=lambda x : x.get_age(),reverse=True)
    output_student(sorted_x)

def nl_di_gao(L):
    # sorted_x = sorted(L, key=lambda x : x['age'],reverse=False)
    sorted_x = sorted(L, key=lambda x : x.get_age(),reverse=False)
    output_student(sorted_x)

def read_from_file():
    L = [] #创建一个准备存放字典的列表
    try:
        # 1 打开文件
        # f = open("./si.txt")
        f = open("si.txt")
        # f = open("/home/tarena/qiu/day15/xueshengguanli/si.txt") #绝对路径
        # 2 读取信息
        try:
            while True:
                line = f.readline()  #读取一行   'xiaohang,20,100\n'
                if not line: #到达文件尾
                    break
                s = line.strip() #去掉两边的空白字符 ['xiaohang,20,100']
                lst = s.split(",")#['xiaohang', '20', '100']
                n = lst[0]
                a = int(lst[1])
                scr = int(lst[2])
                d = Student(n,a,scr)
                # d = dict(name=n,age=a,score=scr)
                L.append(d)
        finally:
            # 3 关闭文件   
            f.close()
            print('读取数据成功')
    except OSError:
        print("读取数据失败")    
    except ValueError:
        print("数据类型错误!")   
    return L

def save_to_file(L): #10保存信息到文件si.txt
    try:
        f = open('si.txt','w')
        #循环写入每个学生信息
        for x in L:
            # f.write(x['name'])
            f.write(x.get_name())
            f.write(',')
            # f.write(str(x['age'])) #年龄 一定要转成字符串才能写进txt
            f.write(str(x.get_age())) #年龄 一定要转成字符串才能写进txt
            f.write(',')
            # f.write(str(x['score'])) #成绩 一定要转成字符串才能写进txt
            f.write(str(x.get_score())) #成绩 一定要转成字符串才能写进txt
            f.write('\n')  #换行
        f.close
    except OSError:
        print('保存失败')
