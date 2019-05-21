#flush.py

#此示例示意文件缓冲的作用及清倒(清除)方法

# print('hello',end=' ',flush=True)
print('hello',end=' ')
import sys
sys.stdout.flush() #清空缓冲区
while True:
    pass