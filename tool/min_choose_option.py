from jsonpath import jsonpath
import json

with open('./origin.txt', 'r', encoding='utf-8') as file:
    file_json = json.loads(file.readline())

# print(file_json)
question_code = jsonpath(file_json, "$..question_code")
min_choose_option = jsonpath(file_json, "$..min_choose_option")
# print(len(question_code))
# peace = zip(question_code, min_choose_option)
peace = question_code+min_choose_option
peace_str = str(peace)
Note = open('result.txt', mode='w')
for i in peace_str:
    # print(i)
    Note.write(i)

Note.close()

