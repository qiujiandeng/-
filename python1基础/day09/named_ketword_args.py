#此示例示意命名关键字形参的定义和使用

def func1(a,b,*,c,d):
    print(a,b,c,d)

func1(1,2,3,4)
func1(1,2,c=30,d=40)
func1(a=10,b=20,c=30,d=40)