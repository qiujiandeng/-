#此示例示意用双星字典形参接收多余的关键字传参

def func(a,b,**kwargs):
    print("关键字传参的个数是:",len(kwargs))
    print("kwargs=",kwargs)

func (a=1,b=2,c=3)

