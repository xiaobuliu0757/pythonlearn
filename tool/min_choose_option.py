from jsonpath import jsonpath
import json
# 打开存放json格式的数据
with open('./origin.txt', 'r', encoding='utf-8') as file:
    file_json = json.loads(file.readline())

# 提取想要的字段
question_code = jsonpath(file_json, "$..question_code")
min_choose_option = jsonpath(file_json, "$..min_choose_option")
#提供个列表待会存数据
list = []
# 利用迭代方式实现A\B两两凑对
for x,y in zip(question_code,min_choose_option):
    # 转成字符串给writeline用
    list = str([x,y])
    # 打开文本文档，a是指在末尾连接输出
    Note = open('result.txt', mode='a')
    # 通过“+”号加了个换行好看点
    Note.writelines(list+'\n')
print("结果已更新到'result.txt'文件中~")
# 记得关下文档哦
Note.close()

