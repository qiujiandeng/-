# exercize4:
#     1. 一个球从100米高空落下,每次落地后反弹高度为原来的一般,在落
#     下,写程序算出:
#         1.皮球在第10次落地后反弹的高度
#         2.皮球在第10次落地反弹后工经历多少米路程

h = 100 #球的高度
m = 0#总路程
cs = 0#计算次数

#计算球停止需要多少次数
# while h > 0:
#     m += h
#     h = h/2
#     cs += 1

for x in range(10):
    m += h
    h /= 2
    m += h
print(m)
print(h)
# print(cs)

def get_last_height(height,times):
    '''height 原来的高度
    times 为反弹次数'''
    for _ in range(times):
        height /= 2
    return height
print("皮球从100米高度落下反弹十次后的高度为:",get_last_height(100,10))

def get_distance(height,times):
    meter = 0#用来记录总路程
    for _ in range(times):
        #累加下落过程
        meter += height
        height /= 2 #计算返回后的高度
        #累加反弹后的过程
        meter += height
    return meter
print("皮球从100米高度落下反弹十次后的总路程为:",get_distance(100,10))