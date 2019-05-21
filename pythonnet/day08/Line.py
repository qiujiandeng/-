from test import *
import time 
t = time.time()
#单进程运行十次
# for i in range(10):
    # count(1,1)

#IO秘籍程序
for i in range(10):
    write()
    read()

print("single CPU:",time.time() - t)