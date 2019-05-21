	# ３．输入三行文字，让这三行文字在　一个方框居中显示
	# 	(注：不要输入中文)
	# 	如输入：
	# 		hello!
	# 		I'm studing python!
	# 		I like python!
	# 	打印如下：
	# 	+-----------------------+	
	# 	|	hello!              |
	　# 	|	I'm studing python! |
	# 	|	I like python!      |
	# 	+-----------------------+
	# 	center_frame.py


    a = input("请输入第一行文字：")
    b = input("请输入第二行文字：")
    c = input("请输入第三行文字：")

    max_len = max(len(a)),max(len(b)),max(len(c))

    line1 = '+'+'-'*max_len+'+'
    print(line1)
    print('|'+a.center(max_len)+'|')
    print('|'+b.center(max_len)+'|')
    print('|'+c.center(max_len)+'|')
    print(line1)