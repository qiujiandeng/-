#练习３：
#    １．输入一个数，然后做下面两步判断
#        １．判断这个书是否在５０～１００之间
#        ２，判断这个书是否小于０


#x = float(input('请输入一个数：'))

#if x >= 50 <= 100:
#    print(x,"在50～100之间")
#elif x < 0:
#    print(x,"小于０")
#else :
#    print(x,"不在50～100之间")

n = int(input("请输入一个数："))
if 50 <= n <= 100:
    print(n,"在50～100之间")
else:
    print(n,"bu在50～100之间")
if n < 0:
    print(n,"小于0")
else:
    print(n,"大于0")