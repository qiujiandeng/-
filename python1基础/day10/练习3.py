L = [1,2,3]
v = 100
def f1():
    L.append(4)
    v= 200
f1()
print(L) #[1,2,3,4]
print(v) #100 全局变量 局部赋值语句是不行的

def f2():
    L.extend([5])
    # L += [5]   #赋值语句不能改变全局变量
    # v += 1   #赋值语句不能改变全局变量
f2() #此处会怎样?为什么?
print(L)
print(v)