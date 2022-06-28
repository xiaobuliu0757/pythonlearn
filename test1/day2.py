class Cat:

    def __init__(self,name):
        self.name = name

    def drink(self):
        print("%s爱喝水" % self.name)


    def eat(self):
        print("%s爱吃饭"% self.name)

    def __del__(self):
        print("%s886" % self.name)
tom = Cat('小布溜')


tom.drink()
tom.eat()
print('-'*50)
