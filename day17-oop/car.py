#car.py
#家用小汽车类,此示例示意集成
from auto_mobile import *

#定义Car类,继承自automobile类
class Car(AutoMobile):
    pass#占位符,内容已经继承了父类

#添加测试代码
if __name__ == "__main__":
    mycar = Car('小汽车','蓝色',1.40)
    mycar.startup()  #启动父类中的启动def
    mycar.run()   #行驶
    mycar.stop()   #停止
    mycar.info()   #打印信息