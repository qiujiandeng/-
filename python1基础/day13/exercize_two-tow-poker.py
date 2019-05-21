    # two.模拟斗地主发牌,排共54张
    #     种类:
    #         黑桃('\u2660'),梅花('\u2663'),方块('\u2665'),红桃('\u2666')
    #     数字:
    #         A2 - 10JQK
    #     王牌: 大小王
    #     三个人,没人发17张牌,底牌留三张
    #     输入回车,打印第一个人的17张牌
    #     输入回车,打印第二个人的17张牌
    #     输入回车,打印第三个人的17张牌
    #     输入回车,打印3张底牌
import random
# l = ['A','2','3','4','5','6','7','8','9','10','J','Q','K']
# l1 = ['大王','小王']
# for x in l:
#     a = ('\u2660')
#     b = ('\u2663')
#     c = ('\u2665')
#     d = ('\u2666')
#     l1.append(a+x)
#     l1.append(b+x)
#     l1.append(c+x)
#     l1.append(d+x)
# print(l1)
# assert len(l1)  == 54,'出错'

poke = ['大王','小王']
kinds = ['\u2660','\u2663','\u2665','\u2666'] #种类
numbers = ['A']
numbers += [str(x) for x in range(2,11)]
numbers += list("JQK")

for k in kinds:
    for n in numbers:
        poke.append(k + n)
#直接转成推导式
# poke += [k + n for k in kinds for n in numbers]

print(poke)
assert len(poke) == 54,'出错'

# 打乱
poke2 = poke.copy()
random.shuffle(poke2)

player1 = poke2[:17]
player2 = poke2[17:34]
player3 = poke2[34:51]
base = poke2[51:]

input()
print("打印第一个人的17张牌",player1)
input()
print("打印第二个人的17张牌",player2)
input()
print("打印第三个人的17张牌",player3)
input()
print("打印底牌",base)

