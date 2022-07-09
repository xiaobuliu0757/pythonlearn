try:
    i = int(input("请输入:"))
    num = 8/i
    print(num)
#
# except ZeroDivisionError:
#     print("0不能最为被除数~")
#
# except ValueError:
#     print("请输入数字~")

except Exception as result:
    print("未知错误:%s"%result)