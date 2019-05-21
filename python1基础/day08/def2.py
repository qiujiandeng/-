# def2.py


# 此示例示意用def语句来定义带有参数的函数
#此函数名为mymax,有两个形式参数a,b 用于接收实参的传递
# 此函数计算两个参数的最大值并打印

def mymax(a,b):
    print('a=',a)
    print('b=',b)
    if a > b:
        print(a,'大于',b)
    else:
        print(a,'小于等于',b)

mymax(100,200)   #函数调用