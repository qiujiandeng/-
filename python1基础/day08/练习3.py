
    #     写一个函数print_event,传入一个参数n代表终止的整数,打印0~n 之间的偶数
    # 如:
    #     def print_event(n):
    #         ......此处自己完成
    #         print_event(10)
    #     打印:
    #         0
    #         2
    #         4
    #         6
    #         8

def print_event(n):
    for x in range(n+1):   #for x in range(0,n,2):
        if x % 2 == 0:
            print(x)

print_event(10)