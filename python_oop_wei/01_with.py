#此示例示意用try-except 和 try - finally 组合来对文件进行操作
#用with语句可以实现同样的功能,见02_with.py
def read_from_file(filename='info.txt'):
    try:
        f = open(filename)
        try:
            print("正在读取文件")
            n = int(f.read())
            print("n=",n)
        finally:
            #关闭文件
            f.close()
    except OSError:
        print("文件打开失败")

read_from_file()