    # ３．ＢＭＩ指数（Ｂｏｄｙ　Ｍａｓｓ　Ｉｎｄｅｘ）又称身体质量指数
    #     ＢＭＩ值计算公司：ＢＭＩ　＝　体重（公斤）／身高的平方（米）
    #     如：
    #         一个69公斤的人，身高是173公分
    #         ＢＭＩ＝69/1.73**2　得23.05
    #     标准表：
    #         BMI　< 18.5　体重过轻
    #         BMI　>=　18.5　<24　正常范围
    #         BMI　> 24 体重过重
    #         输入身高和体重，打印出BMI的值，并打印出体重状况




shengao = float(input("请输入您的身高(cm):"))
tizhong = float(input("请输入您的体重(kg):"))

BMI = tizhong/(shengao/100)**2

if BMI < 18.5:
    print("BMI:",round(BMI,2),"您的体重过轻")
elif  24 >= BMI >= 18.5:
    print("BMI:",round(BMI,2),"您的体重在正常范围")
else:
    print("BMI:",round(BMI,2),"体重过重")

