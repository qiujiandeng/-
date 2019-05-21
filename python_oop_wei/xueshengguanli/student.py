# 1.用类来描述一个学生的信息(可以修改之前写的Student类)
# class Student:
#     #此处自己实现

#     要求该类的对象用于存储学生信息:
#         姓名,年龄,成绩
#     将这些对象存于列表中,可以任意添加和删除学生信息
#         1.打印出学生的个数
#         2.打印出所有学生的平均成绩
#         (建议用类变量春初学生的个数,也可以把列表当做类变量)

class Student:
    count = 0 #此类变量用来记录学生的个数
    # docs = [] #此列表保存所有的学生对象

    def __init__(self,name,a,s=0):
        self.__name = name
        self.__age = a
        self.__score = s
        Student.count += 1 #让对象个数加1

    def __del__(self):#删除学生信息重建__函数__
        Student.count -= 1  #对象销毁时,count 减1

    @classmethod
    def getTotalCount(cls):
        '''此方法用来得到学生对象的个数'''
        return cls.count



    def get_infos(self): #返回学生信息
        return (self.__name,self.__age,self.__score)
    
    def is_name(self,n): #删除学生和修改学生成绩时候,判断输入的名字是不是相同
        '''判断n是否和self的名字相同'''
        return self.__name == n

    def set_score(self,score):#修改学生成绩
        '''此方法用于制定设置成绩时的规则'''
        if 0 <= score <= 100:
            self.__score = score
            return
        raise ValueError('不合法的成绩信息'+str(score))
    def get_age(self):  #年龄
        return self.__age
    
    def get_name(self):#名字
        return self.__name
    
    def get_score(self): #返回成绩给对象使用
        return self.__score


#写一个测试程序,
def test():
    L = []  #一班的学生
    L.append(Student('小张',20,100))
    L.append(Student('小王',18,97))
    L.append(Student('小李',19,98))

    print('此时学生对象的个数是',Student.getTotalCount())

    L2 = []  #2班的学生
    L2.append(Student('小赵',18,99))
    print(Student.getTotalCount())  #4
    #删除L中的一个学生
    L.pop(1)#这里调用__del__ 调用一次count -1
    print('此时学生的个数为:',Student.getTotalCount())

    all_student = L + L2 #两个班学生保存在一起
    scores = 0 #用来记录所有学生的总和
    for s in all_student:
        # scores += s.score   #累加所有学生的成绩
        scores += s.get_score #可以用函数来返回一个score
    print('平均成绩:',scores / len(all_student))

if __name__ == "__main__":
    test()