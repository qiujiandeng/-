    # 2.输入一些单词和解释,将单词作为键,将解释作为值,存入字典中,
    #   当输入单词或解释为空是停止输入,并打印这个字典

    #   然后,输入查询的单词,给出单词的内容,如果单词不存在则提示:查无此词
danci = []
jieshi = []

while True:
    x = input("请输入单词:")
    if len(x) > 0 :
        
        y = input("请输入解释:")
        if len(y) > 0:

            danci.append(x)
            jieshi.append(y)
        else:
            break
    else:
        break
zidian = {danci[x]:jieshi[x] for x in range(len(danci))}
print(zidian)

while True:
    cx = input("请您输入你要查询的单词:")
    print()
    # print(len(cx))
    if cx not in danci:
        print("查无此词,请重新输入")
        
    elif cx in danci:
        print(cx,"的解释是:",zidian[cx])
        print()
    if len(cx) == 0:
        break