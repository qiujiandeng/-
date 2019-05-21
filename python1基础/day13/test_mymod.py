# test_mymod.py

# 此示意示例调用自定义的mymod.py 模块内的两个函数和两个字符串

import mymod#导入自定义模块

mymod.myfac(5) #调用自定义模块的函数
mymod.mysum(100)

print(mymod.name1) #获取mymod里的nname1绑定的字符串
