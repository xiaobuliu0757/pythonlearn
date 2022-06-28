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
lin = Tian()
lin.fly()