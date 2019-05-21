#print.py

print(1, 2, 3, 4)   #1 2 3 4  #
print(1, 2, 3, 4,sep=' ')   
print(1, 2, 3, 4,sep='#')      #    1#2#3#4
print(1, 2, 3, 4,sep='<--->')
print(1, 2, 3, 4,sep='')


print(1, 2, 3, 4, sep=' ', end='\n')    #\n代表换行
print(5, 6, 7, 8, end='')
print(9, 10, end='\n')
print("hello",end='')
print("china", end='\n\n\n\n')
print("AAAAA", end='',flush=True)     
while True:      #死循环，让程序不退出
    pass