# 此示例示意模块的隐藏属性,当此模块用from import * 语句导入
# 时,不会导入_f,__f,和_name属性
def f():胡
    pass

def _f():
    pass

def __f():
    pass

name = 'aaa'
_name = 'bbb'