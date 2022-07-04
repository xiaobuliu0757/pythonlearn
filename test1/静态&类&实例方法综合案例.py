class Game(object):
    # 类属性
    top_score = 0

    #初始化方法
    def __init__(self, player_name):
        # 实例属性
        self.player_name = player_name

    #静态方法
    @staticmethod
    def show_help():
        print("你好，欢迎光临~")

    # 类方法
    @classmethod
    def show_top_score(cls):
        print("历史记录： %d" %cls.top_score)

    # 实例方法
    def start_game(self):
        print("欢迎你，%s"%self.player_name)

# 查看游戏的帮助信息
Game.show_help()
# 查看历史最高分
Game.show_top_score()
# 创建游戏对象
xiaoming = Game("小明")
xiaoming.start_game()


