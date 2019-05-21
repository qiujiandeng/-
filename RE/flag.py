import re

#只匹配ascii字符
# regex = re.compile(r'\w+',flags=re.A)

#忽略字母大小写
# regex = re.compile(r'[a-z]+',flags=re.I)

#.可以匹配换行
# regex = re.compile(r'.+',flags = re.S)

#可以变的能匹配每一行的开始位置
# regex = re.compile(r'to$',flags=re.M)

#为正则表达式添加注释
pattern = r'''[A-Z][a-z]*#匹配第一个单词
\s+\w+\s+#匹配空行的第二个单词
\w+#匹配汉子
'''
regex = re.compile(pattern,flags=re.X)
l = regex.findall('Welcome to\n 北京')
print(l)

