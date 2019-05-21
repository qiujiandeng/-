
x = 100
y = 200

s = 'x + y + 1'
r = eval(s)
print('r=',r)
print('s=',s)
#先创建一个局部作用域的字典
local_scope = {'x':1,'y':2}
a = eval(s,None,local_scope)
print('a=',a)

#创建一个全局作用域的字典
global_scope = {'x':10,'y':20}
b = eval(s,global_scope)
print('b',b)  #31

c = eval(s,{'x':10,'y':20},{'x':1})
print('c=',c) #22