#打印1～20　在一行　。。打印10行
h = 1
while h <= 10:
    i = 1
    while i <= 20:
        print(i,end=' ',flush=True)
        i += 1
    print()
    h += 1