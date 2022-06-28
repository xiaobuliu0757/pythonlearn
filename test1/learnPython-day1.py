# #计算0-100的和
# i=0
# sum=0
# while i<=100:
#     sum += i
#     i +=1
# print(sum)

# i=0
# while i<3:
#     i+=1
#     if i==2:
#         print("不干了")
#         continue
#     print("hehe")
# *
# **
# ***
# ****
# *****
#
# row=1
# while row<=9:
#     col = 1
#     while col <=row:
#         # print("*", end='')
#         print("%d * %d = %d" %(col,row,row*col),end='\t')
#         col +=1
#     # print("*")
#     row+=1
#     print("")
#
# name_list = ["zhangsan","lisi","wangwu"]
# A=name_list.index("lisi")
# name_list.insert(1,"xc")
#
# age_list=[88,66,77]
# name_list.extend(age_list)
# print(name_list)
#
# name_list.remove("wangwu")
# print(name_list)
#
# name_list.pop(1)
# print(name_list)
#
# del name_list[1]
# print(name_list)


# 列表长度
# a =len(name_list)
# print(a)
# name_list.append("zhangsan")
# print(name_list)
# aa = name_list.count("zhangsan")
# print("zhangsan出现的了%d次" % aa)
# name_list.remove("zhangsan")
# print(name_list)
# 列表中数据个数

# name_list=["zhangsan","lisi","wangwu"]
# #
# # 升序
# # name_list.sort()
# # print(name_list)
# # 降序
# # name_list.sort(reverse=True)
# # print(name_list)
# # #
# # 逆序
# name_list.reverse()
# print(name_list)
#
# dit={"name":"小明",
#      "age":18,
#      "gender":True}
# # 取值
# print(dit["name"])
#
# # 增加
#
# # 修改
# dit["name"]="溜"
# print(dit["name"])
# # 删除
# dit.pop("name")
# print(dit)
# 计算字典包含多少键值对

# print(len(dit))
# # 合并
# new_dit={
#     "age":55,
#     "favourite":"basketball"
# }
# dit.update(new_dit)
# print(dit)
# 清空
# dit.clear()
# print(dit)
# for k in dit:
#     print("%s - %s" %(k,dit[k]) )

# dit=[{"name":"张三",
#       "age":18,
#      "phone":110},
#         {"name":"李四",
#       "age":20,
#         "phone":120
# }]
# # print(dit)
# # for k in dit:
# print(dit)
#
# str = "hello python"
# print(str[6])
#
# for i in str:
#     print(i)

# 字符串长度
# str = "hello hello"
# print(len(str))
# # 统计
# str.count("llo")
# # 位置
#
# print("e的所在位置是:%s" % str.index("e"))



# str = " 1230 "
# #
# print(str.isspace())
# print(str.isdecimal())

# 判断是否以指定字符串开始
# print(str.startswith("hello"))
# # 判断是否以指定字符串结束
# print(str.endswith("0"))
# # 查找指定字符串
# print(str.find("2"))
# # 替换字符串
# print(str.replace("1230","hello"))
# print(str)
# print(str)
# print(str.strip())
# f = open('0319.txt')
# print("读取文件成功")

# f.close()
# poem = [
#  '\t\n登鹳雀楼',
#         '白日依山尽\t\n',
#     '黄河入海流',
#         '欲穷千里目',
#     '更上一层楼',
# ]
# # print(poem)
# for poem_str in poem:
#     print("|%s|" % poem_str.strip().center(10,' '))


#
# for i in open("0319.txt",encoding="utf-8"):
#     print(i.strip( ), end="")


# str ='\t\n登鹳雀楼 \t白日依山尽\t\n 黄河入海流\t 欲穷千里目\t 更上一层楼\t'
# print(str)
# new_str = str.split()
# print(new_str)
# result = " ".join(new_str)
# print(result)


# 切片
# str = '0123456789'
# str_1 = str[2:6]
# print(str_1)
#
# str_2 = str[2:]
# print(str_2)
#
# str_3 = str[0:6]
# print(str_3)
#
# str_4 = str[:]
# print(str_4)
#
# str_5 = str[0::2]
# print(str_5)
#
# str_6 = str[2:-1]
# print(str_6)
#
# str_7 = str[-2:]
# print(str_7)
#
# str_8 = str[::-1]
# print(str_8)


# for else的应用
# stu = [
#     {
#         "name":"张三"
#     },
#     {
#       "name":"李四"
#     }
# ]
#
# find_name = '消息'
#
# for stu_name in stu:
#     # print('查找的结果是：%s' %stu_name)
#     if stu_name["name"] == find_name:
#         print("找到了:%s" %find_name)
#         #如果找到了，就应该退出循环
#         break
# else:
#     print("抱歉，没找到%s" %find_name)

# print (('Hi,%s, you have $%d') % ('Michael', 1000000))
# list = ['张三','李四','王五']
# list.append('溜溜')  #末尾添加值
# list.insert(0,'显鹏') #
# list.pop(1)
# print(list)
# list[0]='xc'
# print(list)
# list2=[['xc','xp'],'yy','cbdd',{1,2,3}]
# print(len(list2))
# print(list2[0][0])
#
# tuple =(1,2)
# print(tuple)
# tuple2=()
# print(tuple2)

# L = [
#     ['Apple', 'Google', 'Microsoft'],
#     ['Java', 'Python', 'Ruby', 'PHP'],
#     ['Adam', 'Bart', 'Lisa']
# ]
#
# print(L[0][0])
# print(L[1][1])
# print(L[2][2])


'''
小明身高1.75，体重80.5kg。
请根据BMI公式（体重除以身高的平方）帮小明计算他的BMI指数，并根据BMI指数：

低于18.5：过轻
18.5-25：正常
25-28：过重
28-32：肥胖
高于32：严重肥胖
'''

# height = float(input("请输入你的身高:（米）"))
# weight = float(input("请输入你的体重:（公斤）"))
# BMI =(weight/(height**2))
#
# if BMI <18.5:
#     print("亲亲，你的体重过轻哦")
# elif BMI >=18.5 and BMI<25:
#     print("亲亲，你的体重正常")
# elif BMI >=25 and BMI<32:
#     print("亲亲，你的体重正常")
# else:
#     print("亲亲，你的体重严重肥胖")


# sum=0
# for x in range(101):
#     sum = sum + x
# print(sum)

# 计算100以内所有奇数之和
# sum=0
# for x in range(101):
#
#     if x%2 !=0:
#         print(x)
#         sum = sum +x
#
# print(sum)
#
#
# sum = 0
# n = 99
# while n > 0:
#     sum = sum + n
#     print(n)
#     n = n - 2
#
# print(sum)
# 2 4 6 8 10
#
# L = ['Bart', 'Lisa', 'Adam']
# for i in L:
#     print("hi %s" %i)

# n = 1
# while n < 100:
#     if n>=10:
#         break
#     print(n)
#     n = n+1

# n = 0
# while n<10:
#     n = n+1
#     if n % 2 ==0:
#         continue
#     print(n)


# a= -4
# print(abs(a))
# n1=255
# print(hex(n1))
# print(int(0xff))

# def my_abs(x):
# 校验数据类型
#     if not isinstance(x,(int)):
#         raise TypeError("类型有误，请重新输入")
#     if x > 0:
#         return x
#     if x < 0:
#         return -x
# print(my_abs("12"))
# def calc(*number):
#     sum =0
#     for i in number:
#         sum =sum + i**2
#     return sum
# print(calc(1,2,3))

# def mul(*numbers):
#     if len(numbers)==0:
#         raise TypeError("请输入数字")
#     else:
#         s = 1
#         for i in numbers:
#             s = s * i
#         return s
# 测试
# print('mul(5) =', mul(5))
# print('mul(5, 6) =', mul(5, 6))
# print('mul(5, 6, 7) =', mul(5, 6, 7))
# print('mul(5, 6, 7, 9) =', mul(5, 6, 7, 9))
# if mul(5) != 5:
#     print('测试失败!')
# elif mul(5, 6) != 30:
#     print('测试失败!')
# elif mul(5, 6, 7) != 210:
#     print('测试失败!')
# elif mul(5, 6, 7, 9) != 1890:
#     print('测试失败!')
# else:
#     try:
#         mul()
#         print('测试失败!')
#     except TypeError:
#         print('测试成功!')

# def trim(s):
#
#     while s[:1]==' ':
#
#         s=s[1:]
#
#     while s[-1:]== ' ':
#
#         s=s[:-1]
#
#     return s
# # 测试:
# if trim('hello  ') != 'hello':
#     print('测试失败!')
# elif trim('  hello') != 'hello':
#     print('测试失败!')
# elif trim('  hello  ') != 'hello':
#     print('测试失败!')
# elif trim('  hello  world  ') != 'hello  world':
#     print('测试失败!')
# elif trim('') != '':
#     print('测试失败!')
# elif trim('    ') != '':
#     print('测试失败!')
# else:
#     print('测试成功!')
# str =[1,2,3,4,5]
# print(str[1:])
# print(str[:1])
# print(str[0:])
# dit = {'name':"xc",'age':"18"}
# for key,value in dit.items():
#     print(key,value)
# for value in dit.values():
#     print(value)
#
# def findMinAndMax(*L):
#     if len(L)==0:
#         return none,none
#     else:
#         min = L[0]
#         max = L[0]
#     for i in L :
#         if i <=min:
#             min = i
#         else:
#             pass
#
#     for y in L:
#         if y >=max:
#             max = y
#         else:
#             pass
#     return min,max
# # 测试
# if findMinAndMax(1,2,3,4) == (1,4):
#     print("测试通过")
# else:
#     print("测试失败")
#
# if findMinAndMax(0,2,-1) == (-1,2):
#     print("测试通过")
# else:
#     print("测试失败")

# A = [x*y for x in range(1,11) for y in "@%$"]
# print(A)

# L1 = ['Hello', 'World', 18, 'Apple', None]
# L2 = [s.lower() for s in L1 if isinstance(s,str) == True]
# print(L2)
# 输出当前目录的所有文件
# import os
# q = os.listdir
# l1 = {d for d in os.listdir('.')}
# print(l1)

def triangles():
    L = [1]

    while True:
        yield L

        L = [1] + [L[n] + L[n + 1] for n in range(len(L) - 1)] + [1]

# n = 0
# results = []
# for t in triangles():
#     results.append(t)
#     n = n + 1
#     if n == 10:
#         break
#
# for t in results:
#     print(t)
#
# if results == [
#     [1],
#     [1, 1],
#     [1, 2, 1],
#     [1, 3, 3, 1],
#     [1, 4, 6, 4, 1],
#     [1, 5, 10, 10, 5, 1],
#     [1, 6, 15, 20, 15, 6, 1],
#     [1, 7, 21, 35, 35, 21, 7, 1],
#     [1, 8, 28, 56, 70, 56, 28, 8, 1],
#     [1, 9, 36, 84, 126, 126, 84, 36, 9, 1]
# ]:
#     print('测试通过!')
# else:
#     print('测试失败!')

