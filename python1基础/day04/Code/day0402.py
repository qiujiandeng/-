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
aa = 20-len(a)
bb = 20-len(b)
cc = 20-len(c)
print(' '*aa,a)
print(' '*bb,b)
print(' '*cc,c)


a = input("请输入第一行文字：")
b = input("请输入第二行文字：")
c = input("请输入第三行文字：")
print("%20s",a)
print("%20s",b)
print("%20s",c)