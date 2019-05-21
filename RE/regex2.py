import re

pattern = r"(ab)cd(?P<pig>ef)"

regex = re.compile(pattern)
#获取match对象
# obj = regex.search('abcdefgh')
#截取0=6为匹配内容
obj = regex.search('abcdefgh',pos=0,endpos=6)

######## match 属性变量 #######
print(obj.pos)
print(obj.endpos)
print(obj.re)
print(obj.string)
print(obj.lastgroup)
print(obj.lastindex)


#############  match 属性方法  ###########
print(obj.span())
print(obj.start())
print(obj.end())
print(obj.groupdict())
print(obj.groups())


print(obj.group())
print(obj.group(1))   #获取第一个子组内容
print(obj.group('pig'))  #获取对应不获取内容

