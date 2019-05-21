

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


def mydelxs(a):#创建删除学生信息的函数
    x = input("请输入你要删除的学生信息:")
    xx = 0
    for ch in a:
        if x in ch['name']:
            del a[xx]
            print("已删除",x,"学生信息")
        if x not in ch:
            xx += 1

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
    x = input("请输入你要修改成绩的学生:")
    xx = 0
    for ch in c:
        if x in ch['name']:
            chengji = int(input("请输入您要修改的成绩:"))
            ch['score'] = chengji
            print('已将',x,'学生成绩修改为:',chengji)

            
def cj_gao_di(L):
    sorted_x = sorted(L, key=lambda x : x['score'],reverse=True)
    output_student(sorted_x)

def cj_di_gao(L):
    sorted_x = sorted(L, key=lambda x : x['score'],reverse=False)
    output_student(sorted_x)

def nl_gao_di(L):
    sorted_x = sorted(L, key=lambda x : x['age'],reverse=True)
    output_student(sorted_x)

def nl_di_gao(L):
    sorted_x = sorted(L, key=lambda x : x['age'],reverse=False)
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

                d = dict(name=n,age=a,score=scr)
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





# def zhujianmian():
#     print('+-------------------------------------+') #22
#     print("|",'1) 添加学生信息',' '*19,'|')
#     print("|",'2) 显示学生信息',' '*19,'|')
#     print("|",'3) 删除学生信息',' '*19,'|') #去创建删除学生信息的函数
#     print("|",'4) 修改学生成绩',' '*19,'|') #去创建修改学生成绩的函数
#     print("|",'5) 按学生成绩高-低显示学生信息'," "*4,'|')
#     print("|",'6) 按学生成绩低-高显示学生信息'," "*4,'|')
#     print("|",'7) 按学生年龄高-低显示学生信息'," "*4,'|')
#     print("|",'8) 按学生年龄低-高显示学生信息'," "*4,'|')
#     print("|",'q) 退出系统    ',' '*19,'|')
#     print('+-------------------------------------+')





# #创建界面循环函数
# def main():
#     infos = [] #保存学生信息
#     while True:
#         zhujianmian()
#         # print('+----------------------+') #22
#         # print("|",'1) 添加学生信息'.center(14),'|')
#         # print("|",'2) 显示学生信息'.center(14),'|')
#         # print("|",'3) 删除学生信息'.center(14),'|') #去创建删除学生信息的函数
#         # print("|",'4) 修改学生成绩'.center(14),'|') #去创建修改学生成绩的函数
#         # print("|",'q) 退出系统    '.center(16),'|')
#         # print('+----------------------+')
#         s = input("请输入您的操作:")
#         if s == '1':
#             infos += input_student()
#         elif s == '2':
#             output_student(infos)
#         elif s == '3':
#             mydelxs(infos)
#             # infos = mydelxs(a)
#         elif s == '4':
#             xiugai(infos)
#         elif s == '5':
#             cj_gao_di(infos)
#         elif s == '6':
#             cj_di_gao(infos)
#         elif s == '7':
#             nl_gao_di(infos)
#         elif s == '8':
#             nl_di_gao(infos)
#         elif s == 'q':
#             break

# main()


# infos = input_student()
# print(infos) #打印实参infos打印表格
# output_student(infos)