    # 2.输入一些单词和解释,将单词作为键,将解释作为值,存入字典中,
    #   当输入单词或解释为空是停止输入,并打印这个字典

    #   然后,输入查询的单词,给出单词的内容,如果单词不存在则提示:查无此词
mydict = {} #创建一个空字典准备存储数据
while True:
    word = input("请输入单词:")
    if not word:#如果word空字符串,则退出
        break
    trans = input("请输入解释:")
    if not trans:
        break
    #走到此处说明word,trans都绑定了正确的值
    mydict[word] = trans
print("mydict=",mydict)

print("-------------以下开始查词")
while True:
    w = input("请输入你要查询的单词:")
    if w in mydict:
        print("解释是:",mydict[w])
    else:
        print("查无此词")
        break