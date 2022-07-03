class Run:
    # 既不需要访问类属性或者调用类方法，
    # 也不需要访问实例属性或者调用实例方法就可以用静态方法
    @staticmethod
    def run():
        print("这是一个静态方法")