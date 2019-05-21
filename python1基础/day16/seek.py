#此示例示意用seek方法用来该表文件流的读写位置

f = open("char20.txt",'rb')
print("当前文件的读写位置是:",f.tell())
b = f.read(3)  #b = b'ABC',读写位置向后移动3个字节
print("读写三个字节后的读写位置是:",f.tell())

#此处读取低5~9这五个字节
#方法一.从文件头开始偏移
# f.seek(5,0)
#方法二.相对当前位置开始偏移
# f.seek(2,1)
#方法三.相对文件尾向前开始偏移
f.seek(-15,2)
print("移动后的文件读取位置是:",f.tell())#5
b = f.read(5)
print('b=',b)
#b = .....

f.close()