#if_embed.py


#输一个整数１～１２代表月份，打印这个月在哪个季节
month = int(input('请输入月份(1~12)：'))
if 1 <= month <= 12:
    print("合法的月份")
    if month <= 3:
        print('春季')
    elif month <= 6:
        print('夏季')
    elif month <= 9:
        print('秋季')
    elif month <= 12:
        print('冬季')
else:
    print("您输入有错")