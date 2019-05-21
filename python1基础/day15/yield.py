
#此示例示意生成器函数的定义和使用
def myyield():
    print("即将生成2")
    yield 2  #生成2
    print("即将生成3")
    yield 3
    print("即将生成5")
    yield 5
    print("即将生成7")
    yield 7

    print("myyield函数运行结束!")

g = myyield() #生成器函数调用,将返回生成器对象,g绑定一个生成器
# print(g)
it = iter(g) #让生成器提供迭代器
print(next(it)) #2
print(next(it)) #3
print(next(it)) #5
print(next(it)) #7
print(next(it)) #StopIteration异常

print('程序结束')