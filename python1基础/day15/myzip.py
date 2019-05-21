# myzip
# 此示例示意用生成器函数来创建一个与zip函数功能一致的函数

def myzip(iterable1,iterable2):
    it1 = iter(iterable1)
    it2 = iter(iterable2)
    while True:
        try:
            v1 = next(it1)
            v2 = next(it2)
            yield (v1,v2)
        except StopIteration:
            return

numbers = [10086,10000,10010,95588]
names = ['中国移动','中国电信','中国联通']

for t in myzip(numbers,names):
    print(t)