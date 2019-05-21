#此示例示意 静态方法的创建和使用

class A:
    @staticmethod
    def myadd(x,y):
        '''此方法为静态方法
        此方法的形参不需要传入类或示例
        '''
        return x + y
    pass

print('1+2=',A.myadd(1,2))
a = A()
print('100+200=',a.myadd(100,200))
