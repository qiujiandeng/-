#回顾生成器
def fun():
    print("启动生成器")
    yield 1
    print("生成器完成")

#生成器对象
g = fun()
#如何启动生成器 #通过next取生成器,因为生成器是可以迭代的
print(next(g))
print(next(g))
#关闭生成器对象
g.close()