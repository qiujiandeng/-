l = [{'name':'qiu','age':20},{'name':'qi','age':22},{'name':'qiu1','age':25},
{'name':'zu','age':24}]

import operator
 
x = [{'name':'Homer', 'age':39}, {'name':'Bart', 'age':10}]
# sorted_x = sorted(l, key=operator.itemgetter('age'),reverse=False) # True 是倒叙  默认是False
sorted_x = sorted(l, key=lambda x : x['age'],reverse=True)
print(sorted_x)