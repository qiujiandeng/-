    # ４．写一个程序，输入一个开始的整数存于begin变量中
    # 　　输入一个结束的整数，存于end变量中
    # 　　打印从　begin　到　end（不包含end)的每个打印整数，
    # 　　打印在一行内，
    # 　　如：
    #     　请输入：８
    #     　请输入：２０
    #     打印：
    #     8　9　10　11　12　......　19
    #     附加思考：
    #     如何实现每５个打印在一行内，打印多行？
    #     提示：多家一个变量来记录打印的个数？？

begin = int(input("请输入一个开始整数："))
end = int(input("请输入一个结束整数："))
count = 0
i = begin
while i < end:
    print(i,end=' ')
    count += 1
    if count % 5 == 0:
        print()
    i += 1
else:
    print()