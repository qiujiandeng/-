# 练习1:
#     1.求:
#         1**2 + 2**2 + 3**2 +.....+ 9**2 的和
    
#     2.求:
#         1**3 + 2**3 + 3**2 +......+ 9**2 的和

#     3.求:
#         1**9 + 2**8 + 3**7 + ..... + 9**1的和 
print(sum(map(pow,range(1,10),[2]*len(range(1,10)))))
print(sum(map(lambda x: x**2,range(1,10))))
print(sum(map(pow,range(1,10),[3]*len(range(1,10)))))
print(sum(map(lambda x: x**3,range(1,10))))
print(sum(map(pow,range(1,10),range(9,0,-1))))
