    # 2. 分解质因数,输入一个正整数,分解质因数
    #   如:
    #     输入:90
    #   打印:
    #     90 = 2*3*3*5
    # (质因数是指最小能被原数整数的素数(不包括1))

x = int(input('请输入一个整数:'))
xx = x
ss = []
zs = 2
while x != 1:
    if x % zs ==0:
        ss.append(zs)
        x = x // zs
        zs = 2
    else:
        zs += 1
# print(ss)
print(xx,'= ',end='')
b = 1
for ch in ss:
    if b < len(ss):
        print(ch,end='*')
        b += 1
    else:
        print(ch)
# print()

