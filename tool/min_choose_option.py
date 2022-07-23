from jsonpath import jsonpath
import json
# 打开存放json格式的数据
with open('./origin.txt', 'r', encoding='utf-8') as file:
    file_json = json.loads(file.readline())
# 提取想要的字段
question_code = jsonpath(file_json, "$..question_code")
min_choose_option = jsonpath(file_json, "$..min_choose_option")
#提供个列表待会存数据用
list = []
not_answer = []
should_answer = []
# 利用迭代方式实现A\B两两凑对
for x,y in zip(question_code,min_choose_option):
    # 转成字符串给writeline用
    list = str([x,y])
    # 0非必填，1必填
    if y:
        should_answer.append(x)
    else:
        not_answer.append(x)
    # 打开文本文档，w是指在覆盖上一份文件
    Note = open('result.txt', mode='w')
    # 通过“+”号加了个换行好看点
    Note.writelines("非必填：%s"% not_answer+'\n')
    Note.writelines("必填：%s"% should_answer)
# 记得关下文档
Note.close()
print("运行成功，结果已更新到'result.txt'文件中~")





