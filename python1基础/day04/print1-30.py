#  １，打印０～３０范围内的所有偶数（能被２整除的数）
i = 1
while i <= 30:
    a = i%2
    while a == 0:
        print(i,end=' ')
        a += 1
    i += 1
print()


#老师的
x = 0 
while x < 30:
    print(x)
    x += 2　#偶数一定相差为２