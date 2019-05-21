#Gun
#枪械类
class Gun:
    #构造方法
    def __init__(self,name,max_bullets,bullet_left,dest_ratio,firing_bullets):
        self.name = name  #名称
        self.max_bullets = max_bullets #最大弹夹容量
        self.bullet_left = bullet_left #剩余子弹
        self.dest_ratio = dest_ratio #杀伤系数
        self.firing_bullets = firing_bullets  #每次发射数量
        #后坐力

    
    #填弹方法
    def reload(self):
        #填弹后,剩余子弹就等于弹夹容量
        self.bullet_left = self.max_bullets
        print("填弹完成,剩余子弹%d发"%self.bullet_left)

    #开枪方法
    def fire(self):
        if self.bullet_left <= 0: #没子弹
            print("请填弹")
            return
        if self.bullet_left >= self.firing_bullets:
            #计算剩余子弹
            self.bullet_left -= self.firing_bullets #打出1发子弹
        else:  #剩余子弹小于一次击发打出的子弹
            self.bullet_left = 0 #全部打出

        #计算杀伤力
        damage = int(self.dest_ratio * 100)
        #打印,模拟开火
        if self.firing_bullets == 1:
            print("嘣...%s开火,杀伤力%d,剩余子弹%d"%(self.name,damage,self.bullet_left))
        if self.firing_bullets == 3:
            print("哒哒哒...%s开火,杀伤力%d,剩余子弹%d"%(self.name,damage,self.bullet_left))
            