class Person(object):
    def __init__(self,name):
        self.name = name
    def game_with_dog(self, dog):
        print("%s和%s玩" % (dog.name, self.name))
        dog.game()

class Dog(object):
    def __init__(self,name):
        self.name = name
    def game(self):
        print("%s狗狗飞盘"%self.name)

class XiaoTianDog(Dog):
    def game(self):
        print("%s飞了起来"%self.name)


#
# wangcai = Dog("旺财")

wangcai =XiaoTianDog("飞天旺财")
# wangcao.game()
xiaoming = Person("小明")
xiaoming.game_with_dog(wangcai)