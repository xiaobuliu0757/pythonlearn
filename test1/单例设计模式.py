class MusicPlayer(object):

    def __new__(cls, *args, **kwargs):
        # 创建对象时，new方法会被自动调用

        # 1、为对象分配空间
        # 2、返回对象的引用
        return super().__new__(cls)

    def __init__(self):
        print("播放器初始化")

yyy = MusicPlayer()
print(yyy)