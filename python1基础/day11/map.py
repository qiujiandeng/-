#此示例示意map的用法

def power2(x):
    return x ** 2

#生成一个可迭代对象,此可迭代对象可以生成1~9自然数的平方
# 1 4 9 16 25 36 .....

for x in map(power2,range(1,10)):
    print(x)

#求:
# 1+4+9+16+......的和
print(sum(map(power2,range(1,10))))