# 练习1:
#     经理有:曹操,刘备,孙权
#     技术员有:曹操,孙权,张飞,关羽
#     用集合求:
#     1.即是经理也是技术员的有谁?
#     2.是经理,但不是技术人员的都有谁?
#     3.是技术员,但不是经理的有谁?
#     4.张飞是经理吗?
#     5.身兼一值的人都有谁>
#     5.经理的技术员共有几人?

manager={'曹操','刘备','孙权'}
technician={'曹操','孙权','张飞','关羽'}
print('即是经理也是技术员的有:',manager & technician)
print('是经理,但不是技术人员的都有:',manager - technician)

print('是技术员,但不是经理的有:',technician - manager)
if '张飞' in manager:
    print("张飞是经理")
else:
    print("张飞不是经理")
print('身兼一值的人都有:',manager ^ technician)
print('经理的技术员共有:',len(manager|technician),'人')

    