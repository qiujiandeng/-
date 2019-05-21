
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

for x in myyield():
    print(x)


print('程序结束')