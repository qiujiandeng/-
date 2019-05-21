# ２．输入一个整数代表，代表正方形的宽和高，打印相应的正方形
#     如：
#         请输入：５
#     打印：
#         1　2　3　4　5　
#         2　3　4　5　6　
#         3　4　5　6　7
#         4　5　6　7　8　
#         5　6　7　8　9　

w = int(input("请输入："))
for line in range(1,w+1):
    
    # 打印一行从ｌｉｎｅ号开始的ｗ个字母
    for x in range(line,line+w):
        print(x,end=' ')
    print()
    # print(line)