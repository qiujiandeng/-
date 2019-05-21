# 练习1:
#     1.输入一个圆的半径,打印出这个圆的面积
from math import pi ,sqrt
r = float(input("请输入圆的半径:"))
area = pi * r ** 2
print("半径为:",r,"的圆的面积是:",area)
#     2.输入一个圆的面积,打印出这个圆的半径
area2 = float(input("请输入圆的面积"))
r2 = sqrt(area2/pi)
print("面积为:",area2,'的圆的半径是:',r2)