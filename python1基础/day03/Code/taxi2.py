# 练习：
#     １．北京出租车计价程序
#     　　收费标准：
#     　　　　３公里以内收费１３元
#     　　　　基本单价２．３元／公里（超出３公里以外）
# 　　　　　　空驶费：超过１５公里后，每公里加收单价的50%空驶费（即：１５公里后为３．４５／公里）
#         　要求：
#             输入公里数，打印出费用金额（以元为单位，精准到分，分以后四舍五入）

km = float(input("请输入公里数："))
money = 13
# 此处开始计算钱数，修改money变量

#超过一公里以外多收2.3／ｋｍ
if km > 3:
    money += 2.3 *(km - 3)
if km > 15:
    money += 2.3 * .5 * (km - 15)  #加收回城费



# if km <= 3:
#     money = 13
# elif 15> km > 3:
#     money = 13 + (km - 3)*2.3
# else:
#     money = 13 + (15 - 3)*2.3 + (km - 15) * (2.3 * 1.5)
#     #money = 13 + 2.3*(km - 3) + 2.3 *.5*(km-15)


print("您的公里数是",km,"km","总金额：",round(money,2),'元')
