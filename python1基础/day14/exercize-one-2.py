# exercize one:
#     写一个函数 get_scort() 来获取学生输入的成绩(0~100的整数),
#     如果输入出现异常,则此函数返回0,否则返回用户输入的成绩
#         如:
#             def get_score():
#                 .....#此处自己实现
#             score = get_score()
#             print("学生的成绩是",score)

def get_score():
    s = input("请输入学生成绩(0~100)")
    try:
        scr = int(s)  #字符串转为整数
    except ValueError:
        return 0
    if 0 > scr or scr > 100:
        return 0
    return scr
score = get_score()
print("学生的成绩是",score)