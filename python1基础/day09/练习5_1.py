# 练习5:
#     1.算出100~999 以内的水仙花数(Narcissistic number)
#         水仙花数是值百威的3次方加上十位的3次方加上个位的3次方
#         等于原数的整数
#         例如: 153 = 1**3 + 5**3 +3**3
#         答案: 153, 370,.....

#方法1:
# for x in range(100,1000):
#     #拆出百位,十位,个位
#     bai = x // 100 #百位
#     shi = x % 100 //10
#     ge = x % 10 #个位
#     if x == bai **3 + shi ** 3 + ge ** 3:
#         print(x)#满足条件的水仙花数 
    
# #方法2,将数字转为字符串
# for x in range(100,1000):
#     s = str(x)
#     bai = int(s[0])
#     shi = int(s[1])
#     ge = int(s[2])
#     if x == bai ** 3 + shi ** 3 + ge ** 3:
#         print(x)
#方法三 水表式
for bai in range(1,10):
    for shi in range(0,10):
        for ge in range(10):
            x = bai*100 + shi *10 +ge
            if x == bai ** 3 + shi ** 3 + ge ** 3:
                print(x)
