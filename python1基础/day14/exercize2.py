# exercize 2:
#     写一个函数 get_age 用来获取一个人的年龄信息
#     此函数规定用户只能输入1~140之间的整数,如果用户输入其他的数
#     则直接出发ValueError类型的错误!
# 如:
#     def get_age():
#         ...
    
#     try:
#         age = get_age()
#         print("用户输入的年龄是:",age)
#     except ValueError:
#         print("用户输入的不是1~140的整数,获取年龄失败)


def get_age():
    age = int(input("请输入年龄(1~140):"))
    if age < 0 or age >140:
        raise ValueError 
    return age
try:
    age = get_age()
    print("用户输入的年龄是:",age)   
except ValueError:
    print("用户输入的不是1~140的整数,获取年龄失败")
# print("用户输入的年龄是:",age)