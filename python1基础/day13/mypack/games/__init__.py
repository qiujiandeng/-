#file:mypack/games/__init__.py

#此列表会在from mypack.games import *导入时,导入
# contra 模块 和 supermario 模块
__all__ = ['contra','supermario']
print('mypack.games  子包被导入')

