def demo1():
    return int(input("请输入数字"))

def demo2():
    return demo1()

try:
    print(demo2())
# except ValueError:
#     print("请重新输入")
except Exception as result:
    print("未知错误：%s"%result)