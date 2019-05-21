#  练习：
#     打印１０以内的偶数（要求使用ｗｈｉｌｅ语句＋ｃｏｎｔｉｎｕｅ采用跳过奇数的方式实现）
   
w = 1

while w < 10:
    if w % 2 == 1:
        w += 1
        continue
    print('%2d'%w,end=' ')
    w += 1
print() 


#奇数
i = 1

while i < 10:
    if i %2 ==0:
        i += 1
        continue
    print('%2d'%i,end=' ')
    i += 1
print()
