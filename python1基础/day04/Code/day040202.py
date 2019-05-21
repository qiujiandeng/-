# 练习：
# 　　写一个程序，输入三行文字，让这三行文字依次以２０个字符的宽度右对齐输出
# 如：
# 　　请输入第一行：hello  china 
# 　　请输入第二行：tanena
# 　　请输入第三行：ａ
# 打印如下：
# 　　　　　　hello china
#                tanena
#                     a
# 做完上题后在思考：
# 　　能否以最长的字符串长度进行右对齐显示（左侧填充空格）

a = input("请输入第一行文字：")
b = input("请输入第二行文字：")
c = input("请输入第三行文字：")
#求最大的函数
max_len = len(a)
if len(b) > max_len:
    max_len = len(b)
if len(c) > max_len:
    max_len = len(c)

# print('最长的字符串长度是：',max_len)

# #方法1，左侧手动添加空格
# print(' '*(max_len-len(a))+a)
# print(' '*(max_len-len(b))+b)
# print(' '*(max_len-len(c))+c)


#方法２，根据最长的字符长度max_len 来生成相应的格式化字符串
#如 max_len 绑定１０,则生成‘％１０ｓ＇

fmt = "%" + str(max_len) + "s"
print("fmt=",fmt)
print(fmt %a)
print(fmt %b)
print(fmt %c)
