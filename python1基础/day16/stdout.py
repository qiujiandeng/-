#此示例示意标准输出文件的用法
import sys
sys.stdout.write("hello world\n")

# sys.stdout.close() #关闭文件 后 ,print() 将不能用
print("hello world!!!")

f = open('myprint.txt','w')
print(1,2,3,4,file=f) #写入内容到文件  myprint.txt  
print("hello world!!!!!!!",file=f) #这些写文件到myptiny中,不打印