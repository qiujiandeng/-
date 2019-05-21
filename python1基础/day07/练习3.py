# 练习3:
#     有如下字符串列表:
#         L = ['tarena','xiaozhang','hello']
#     生成如下字典:
#         d = {'tarena':6,'xiaozhang':9,'hello':5}
#     注:字典的值为键的长度

L = ['tarena','xiaozhang','hello']

c = {x:len(x) for x in L}
print(c)
