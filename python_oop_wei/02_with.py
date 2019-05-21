#此示例示意用try-except 和 with 语句来组合实现文件的操作
def read_from_file(filename='info.txt'):
    try:
        with open(filename) as f:#打开文件改名成f
            print("正在读取文件")
            n = int(f.read())
            print('n=',n)
            print('文件已经关闭')
    except OSError:
        print("文件打开失败")

read_from_file()