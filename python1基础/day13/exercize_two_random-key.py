# exercise two:
#     one. 随机生成6为密码:
#         可以作为密码的字符有:
#         a-z  ,  A-Z ,  0-9
#     随机生成一个6位的密码

# >>> ord('a')
# 97
# >>> ord('z')
# 122
# >>> ord('A')
# 65
# >>> ord('Z')
# 90
# >>> ord('0')
# 48
# >>> ord('9')
# 57
# >>> 
import random

# l = []
# for x in range(97,123):
#     l.append(chr(x))
# for x in range(65,91):
#     l.append(chr(x))
# for x in range(48,58):
#     l.append(chr(x))

# l1 = random.sample(l,6)
# for x in l1:
#     print(x,end='')
# print()

# 方法2 老师
charator = [chr(x) for x in range(65,65+26)]
charator += [chr(x) for x in range(97,97+26)]
charator += [str(x) for x in range(10)]

passwd = ''
for _ in range(6):
    passwd += random.choice(charator)

print("密码是:",passwd)