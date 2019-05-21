#自定义列表
class MyList:
    def __init__(self,iterable = []):
        self.data = [x for x in iterable]
    #重写__abs__()函数,规则是自己定义的
    def __abs__(self):
        #给规则,对每个数求绝对值,用产生的结果实例化一个MyList对象
        return MyList(abs(x) for x in self.data)

    def __str__(self):
        ret = ''
        for x in self.data:
            ret += str(x) #将ABS(L)内的元素转换成字符串
            ret += ' '
        return ret #返回结果

    def __len__(self):
        return len(self.data) #返回结果
    
    def __round__(self):#对每个元素求近似值
        return MyList(round(x,2) for x in self.data)
    
    def __reversed__(self):
        return MyList(reversed(self.data))
    
    def __mul__(self,valie):#重载乘法运算符
        return MyList(self.data * valie)
    
    def __add__(self,other):#重载加法
        return (self.data + other.data)
    
    def __eq__(self,other): #重写 == 比较运算符
        # return (self.data == other.data)
        len1 = len(self.data)
        len2 = len(other.data)
        if len1 != len2:
            return False
        for i in range(0,len1):
            if self.data[i] != other.data[i]:
                return False
        return True
    
    def __lt__(self,other):#小于
        return (self.data < other.data)
    
    def __gt__(self,other):#大于
        # return (self.data > other.data)
        len1 = len(self.data)   #取data属性长度
        len2 = len(other.data) #取另外一个对象data的长度
        min_len = min(len1,len2)#获取循环上限

        for i in range(min_len):
            if self.data[i]  == other.data[i]:
                continue
            if self.data[i] > other.data[i]:
                return True
            if self.data[i] < other.data[i]:
                return False
        if len1 == len2:
            return False
        elif len1 >len2:#前面元素相等,长度比对方大
            return True
        else:
            return False
    
    def __neg__(self):#重载符号运算符
        return MyList(-x for x in self.data)

    def __contains__(self,e): #in/ not in 运算符重载
        print("__contains__()被调用")
        return e in self.data

    def __getitem__(self,i):  #重载[]取值操作
        return self.data[i]
    
    def __setitem__(self,i,value):#重载[]赋值操作
        self.data[i] = value#不需要返回值,取值才需要返回,赋值不需要

    def __delitem__(self,i):#重载[]删除操作
        del self.data[i]

if __name__ == "__main__":
    L = MyList([-1,2,-3,4,-5])
    print(L[0])   #索引取值
    L[2] = 333  #通过索引设置值
    print(L)
    del L[3]  #删除
    print(L)
 




    # abs(L) #重写了__abs__()函数,支持abs表达式
    # L2 = abs(L)   #要用L2来接收L<__main__.MyList object at 0x7fba1ebd2cc0>
    # L3 = MyList([1,2,3,])
    # L4 = MyList([1,2,3,4])
    # L5 = MyList([1,2,3,4])
    # print(L3 > L4)
    # print(L5 > L4)
    # print(L3 != L5)

    # print(L == L3)

    #重写了__str__参数后,所以支持print()
    # print(abs(L))   #绝对值
    # print(len(L))   #返回长度
    # print(round(L))#打印新产生的对象,每个元素都是原对象元素的近似值
    # print(reversed(L))
    # L3 = L * 2
    # print(L3)
    # L4 = L + L
    # print(L4)