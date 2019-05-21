#awp.py
#狙击枪类

from Gun import *

class AWP(Gun):  #AWP类,继承子Gun类
    def openTelescope(self):#打开瞄准镜
        print("瞄准镜已打开")

    def closeTelescope(self):  #关闭瞄准镜
        print("瞄准镜已关闭")