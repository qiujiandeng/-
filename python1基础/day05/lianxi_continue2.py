    # 2,求１～１００之间所有不能被２，３，５和７中任意一个数整除的数的和（用ｃｏｎｔｉｎｕｅ实现）


i = 0
for ch in range(101):
    if ch % 2 == 0:
        continue
    if ch % 3 == 0:
        continue
    if ch % 5 == 0:
        continue
    if ch % 7 == 0:
        continue
    i += ch
    
    print(ch,end=' ')
print()
print(i)