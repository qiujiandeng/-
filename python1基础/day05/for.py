# for 语句语法:
#     for 变量列表 in 可迭代对象 :
#           语句块1
#     else:
#            语句块2

s = "ABCDE"

for ch in s :
    print("ch绑定----->",ch)
else:
    print("for语句迭代访问结束")

print("程序退出")