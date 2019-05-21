# 练习6:
#     1.写程序算出1~20的阶乘的和,即:
#         1! + 2! + 3! +4! +..........+20!

def jc(n):
    i = 0
    for ch in range(n+1):
        i += ch*ch
    return i
print(jc(20))  