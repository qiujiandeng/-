# file:main.py

from menu import *
from student_info import *


#创建界面循环函数
def main():
    infos = [] #保存学生信息
    while True:
        zhujianmian()
        # print('+----------------------+') #22
        # print("|",'1) 添加学生信息'.center(14),'|')
        # print("|",'2) 显示学生信息'.center(14),'|')
        # print("|",'3) 删除学生信息'.center(14),'|') #去创建删除学生信息的函数
        # print("|",'4) 修改学生成绩'.center(14),'|') #去创建修改学生成绩的函数
        # print("|",'q) 退出系统    '.center(16),'|')
        # print('+----------------------+')
        s = input("请输入您的操作:")
        if s == '1':
            infos += input_student()
        elif s == '2':
            output_student(infos)
        elif s == '3':
            mydelxs(infos)
            # infos = mydelxs(a)
        elif s == '4':
            xiugai(infos)
        elif s == '5':
            cj_gao_di(infos)
        elif s == '6':
            cj_di_gao(infos)
        elif s == '7':
            nl_gao_di(infos)
        elif s == '8':
            nl_di_gao(infos)
        elif s == '9':
            infos += read_from_file()
        elif s == 'q':
            break

main()