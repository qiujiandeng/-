    # 2.写一个函数 get_chinaese_char_count(s),此函数功能是
    # 给定一个字符串s,返回这个字符串中中文字符的个数
    # def get_chinaese_char_count(s):
    #     ....
    # s = input("请输入中引文混合的字符串:")
    # print("中文字符的个数是:",get_chinaese_char_count(s))
    # 注:中文的编码范文是: 0x4E00~0x9FA5

def get_chinaese_char_count(s):
    count = 0
    for ch in s:
        if 0x4e00 <= ord(ch) <= 0x9fa5:
            count += 1
    return count
s = input("请输入中引文混合的字符串:")
print("中文字符的个数是:",get_chinaese_char_count(s))
# 注:中文的编码范文是: 0x4E00~0x9FA5   

