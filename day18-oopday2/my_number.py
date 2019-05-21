#自定义数字类型
#数值转换函数重写示例

class MyNumber:
    def __init__(self,value):
        self.data = value#值,字符串
    
    def __int__(self):
        return int(float(self.data))
    
    def __float__(self):
        return float(self.data)

    def __complex__(self):
        return complex(self.data)

if __name__ == "__main__":
    num = MyNumber("123.45")
    setattr(num,"data","456.78")#设置对象属性值
    print(getattr(num,"data"))#"456.78"获取对象的属性值
    print(num.data)  #"456.78"

    delattr(num,"data")  #删除data属性
    print(hasattr(num,"data"))   #判断有没有某个属性值False

    # print(int(num))   #将num对象转换乘int类型
    # print(float(num))
    # print(complex(num))