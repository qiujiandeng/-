#  star_tuple_args.py

#此示例示意星号元组形参的定义和使用

def func(*args):
    print("实参个数是:",len(args))
    print('args=',args)

func(1,2,3,4)
func(5,6,7,8,'A','B','C','D')