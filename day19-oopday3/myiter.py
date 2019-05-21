#通过函数重写,实现自定义迭代器
class MyIter:
    #构造方法,用一个列表初始化对象
    def __init__(self,lst):
        self.data = lst  #lst是列表
        self.cur_index = 0 #计数器,用来返回当前的哪一个元素

    def __iter__(self):#返回一个可迭代对象
        return MyIter(self.data)
    
    def __next__(self):#获取下一个元素,直到没有而报错
        if self.cur_index >= len(self.data):
            raise StopIteration  #抛出异常
        else:
            i = self.cur_index  #记录计数器
            self.cur_index += 1  #计数器加1
            return self.data[i]

if __name__ == "__main__":
    myiter = MyIter(range(1,10))
    for x in myiter:  #现在MyIter不是可迭代对象 要实现的话要重写两个方法
        print(x,end=" ")