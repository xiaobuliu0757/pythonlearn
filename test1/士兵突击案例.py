class Gun:
    # 创建基本属性：类型、子弹数量
    def __init__(self, model):
        self.model = model
        self.bullet_count = 0

    # 创建增加子弹方法
    def add_bullet(self, count):
        self.bullet_count += count

    # 创建发射方法
    def shoot(self):
        # 1、判断子弹数量
        if self.bullet_count <= 0:
            print("【%s】没有子弹了" % self.model)
            return
        # 2、发射子弹
        self.bullet_count -= 1
        # 3、提示发射信息
        print("【%s】突突突" % self.model)


class Soldier:
    def __init__(self, name):
        self.name = name
        # gun没有值，默认为None
        self.gun = None
    def fire(self):
        # 1、判断士兵是否有枪
        if self.gun == None:
            print("抱歉，%s没有枪"% self.name)
            return
        # 2、高喊口号
        print("冲呀！！！！")
        # 3、让枪装填子弹
        self.gun.add_bullet(1)
        # 4、让枪发射子弹
        self.gun.shoot()
# 调试Gun类
a = Gun('AK47')
# a.add_bullet(1)
# print(a.bullet_count)
# a.shoot()

xiaobuliu = Soldier('xiaobuliu')
xiaobuliu.gun = a
xiaobuliu.fire()
print(a.bullet_count)