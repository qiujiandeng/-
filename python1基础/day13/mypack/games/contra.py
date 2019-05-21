#file:mypack/games/contra.py

def play():
    print("正在玩魂斗罗...")

def gameover():
    print("魂斗罗游戏结束!!!!")
    #调用上一层文件夹里的menu.py 里的 show_menu函数

    #用绝对导入的方式
    # from mypack.menu import show_menu
    #用相对导入放式
    from ..menu import show_menu
    show_menu()  #调用

    #想在此处调用tanks.py 里的play() 函数怎么导入?
    #1相对导入方式
    # from .tanks import play
    #2绝对导入方式
    # from mypack.games.tanks import play
    # play()
    #3  as 模块新名
    # import mypack.games.tanks as p
    # p.play()
    #4
    from ..games.tanks import play
    play()
    #5
    # for ...mypack.games.tanks import play
    # play() #报错 ... 三个点超出包的外部了.

    


print("魂斗罗模块被加载!!!")
