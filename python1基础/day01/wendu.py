#　温度转换：
# 　　摄氏温度＝５.0/9.0 * (华氏温度-32)
# 　　开氏温度＝摄氏温度+273.15
# 问：
# 　　100华氏温度转为摄氏温度式多少度，转为开氏温度式多少度？
hs=100
ss = 5.0/9.0*(hs-32)
ks = ss+273.15
print("转为摄氏温度为：",ss,"℃")
print("转为开氏温度为：",ks,"开氏温度")