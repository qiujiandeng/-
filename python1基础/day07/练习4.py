
# 字典练习4:
#     已知有两个字符串列表:
#     Nos = [1001, 1002, 1005,1008]
#     names = ['Tom', 'Jerrt','Spike','Tyke']
    
#     生成一Nos 中项为键, 一names 中的项为值的字典


Nos = [1001, 1002, 1005,1008]
names = ['Tom', 'Jerrt','Spike','Tyke']

# d = { Nos[i] : names[i] for i in range(len(Nos))}
# print(d)


# #老师的
# d = {}
# for i in range(len(Nos)):
#     print(i)
#     d[Nos[i]] = names[i]
# print(d)


# d = {}
# for n in Nos:
#     d[n] = names[Nos.index(n)]


d ={n:names[Nos.index(n)]for n in Nos}
print(d)