# 家具
class HouseItem:
    def __init__(self,name,area):
        self.area = area
        self.name = name

    def __str__(self):
        return "[%s] 占地%.2f " % (self.name, self.area)

# 房子
class House:
    def __init__(self, house_type, area):
        self.house_type = house_type
        self.area = area
        # 剩余面积
        self.free_area = area
        #家具名称列表
        self.item_list = []
    def __str__(self):
        return ("户型：%s \n总面积：%.2f ,剩余面积：%.2f\n 家具：%s"
               %(self.house_type,self.area,
                 self.free_area,self.item_list))
    # 添加家具
    def add_item(self,item):
        # 1、判断家具的面积
        if item.area > self.free_area:
            print("注意：%s的面积:%.2f>剩余面积:%.2f，无法添加！！"%(item.name,item.area,self.free_area))
            return
        # 2、将家具的名称添加到列表中
        self.item_list.append(item.name)
        # 3、计算剩余
        self.free_area -= item.area
#创建家具
bed = HouseItem('席梦思', 400)
chest = HouseItem('衣柜', 2)
table = HouseItem('餐桌', 1.5)
# print(bed)
# print(chest)
# print(table)
# 创建房子
my_home = House('两室一厅',80)
# 添加家具
my_home.add_item(bed)
my_home.add_item(chest)
my_home.add_item(table)
print(my_home)