class Animal:
    def eat(self):
        print("吃")
    def drink(self):
        print("喝")
    def run(self):
        print("跑")
    def sleep(self):
        print("睡")

class Dog(Animal):
    def bark(self):
        print("汪汪")

class Tian(Dog):
    def fly(self):
        print("飞吧")

class cat(Animal):
    def catch(self):
        print("抓老鼠")
    #     重写父类的方法
    def sleep(self):
        print('布溜睡觉觉')
        #利用super调用父类的方法
        super().sleep()


# lin = Tian()
# lin.fly()
w = cat()
w.sleep()


