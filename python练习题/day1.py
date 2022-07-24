# str1 = 'Hello World!'
# str2 = 'Hello Nowcoder!'
# print(str1)
# print(str2)
#
# 格式化输出
# name = input()
# print("I am %s and I am studying Python in Nowcoder!" %name)

# name = input('输入英文名：')
# print(name.lower(),name.upper(),name.title(),sep='\n')

# name = input("")
# print(name.strip())
#
# print(2==3)
# print(2!=3)
# print(2>3)
# print(2<3)
# print(2>=3)
# print(2<=3)
#
# print((2<3)&(2<1))
# print((2<3)|(2<1))
#
# print('Python' == "Python")
# print('Python2' != "Python3")
# print('PYTHON'.lower() == 'Python'.lower())
#
# my_list = [1,2,3]
# if 2 in my_list:
#     print('2 is in my_list!')
# if 8 not in my_list:
#     print('8 is not in my_list!')

# 计算器
# import math
# x = eval(input())
# y = eval(input())
#
# print(x+y)
# print(x-y)
# print(x*y)
# print(math.floor(x/y))
# print(x%y)

# 字符串删除、新增
# offer_list = ['Allen', 'Tom']
# for i in offer_list:
#     print("%s, you have passed our interview and will "
#           "soon become a member of our company."%i)
#
# offer_list.remove('Tom')
# offer_list.append('Andy')
#
# for i in offer_list:
#     print("%s, welcome to join us!"%i)

# 字符串插入位置（采用下标的方式）
# guest_list = [ 'Niuniu','Niu Ke Le']
# for i in guest_list:
#     print(i +',do you want to come to my celebration party?')
# print()
# guest_list.insert(0,'GURR')
# guest_list.insert(guest_list.index('Niu Ke Le'),'Niumei')
# guest_list.append('LOLO')
# for k in guest_list:
#     print(k +', thank you for coming to my celebration party!')
#
# company_list = ['Alibaba', 'Baidu', 'Tencent', 'MeiTuan', 'JD']
# for i in company_list:
#     print('Hello %s,here is my resume!'%i)
# # del函数后面要跟序号
# del company_list[0]
# # pop只能删除列表最后一个元素
# company_list.pop()
# company_list.pop()
# company_list.remove('Tencent')
# print()
# for i in company_list:
#     print('%s,thank you for passing my resume.I will attend the interview on time!' %i)

# my_list = ['P','y','t','h','o','n']
# print('Here is the original list:')
# print(my_list)
# print()
# # 倒叙排列（一次性）
# print('The result of a temporary reverse order:')
# print(sorted(my_list,reverse=True))
# print()
# print('Here is the original list again:')
# print(my_list)
# print()
#
# #正序排列
# print('The list was changed to:')
# my_list.sort(reverse=True)
# print(my_list)
# print()
#输出1-20
# for i in range(1,21):
#     print(i)

# name = ['Niumei', 'YOLO', 'Niu Ke Le', 'Mona']
# friends = []
# friends.append(name)
# food = ['pizza', 'fish', 'potato', 'beef']
# friends.append(food)
# number = [3, 6, 0, 3]
# friends.append(number)
# print(friends)

# my_list =['P','y','t','h','o','n']
# print('Here is the original list:')
# print(my_list)
# print()
# print('The number that my_list has is:')
# # 计算字段的长度
# print(len(my_list))
# 循环输出
# users_list =['Niuniu','Niumei','Niu Ke Le']
# for i in users_list:
#     print('Hi, %s! Welcome to Nowcoder!'%i)
# print("Happy Programmers' Day to everyone!")
