

def fx(n):
    print('递归进入第',n,'层')
    if n == 4:
        return
    fx(n + 1)
    print('递归退出第',n,'层')
fx(1)
print("程序退出")
print(fx(1))