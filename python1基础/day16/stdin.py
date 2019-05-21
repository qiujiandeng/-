
import sys
# s = input("请输入")  #内部就是调用sys.stdin
print("请输入内容:")
s = sys.stdin.readline()
print(s)

s = sys.stdin.read()  #ctrl + D 结束
print(s)