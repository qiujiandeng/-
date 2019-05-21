# binary_file_read.py

# 此示例示意用二进制模式操作文件,实现读取文件myfile.bin数据中的前10个字节

fr = open('myfile.bin','rb')
b = fr.read(10)  #此处返回是的字节串
print('b=',b)
fr.close()
