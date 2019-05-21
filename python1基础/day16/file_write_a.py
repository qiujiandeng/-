#此示例示意写文件的基本操作
try:
    # 1.打开文件
    f = open("mynote.txt",'a')
    # 2.写文件
    f.write("ABCD\n")
    f.write("你好~!")
    # f.write({1:'一'})  #出错 只能字符串
    f.writelines(['abcd','1234\n'])
    # 3.关闭文件
    f.close
except OSError:
    print('打开文件失败')