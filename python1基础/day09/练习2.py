# 练习2:
#     写一个函数myadd,此函数可以计算两个数,三个数及四个数的和
def myadd(a,b,c=0,d=0):
    return a+b+c+d
print(myadd(10,20))   #30
print(myadd(100,200,300))  #600
print(myadd(1,2,3,4))   #10