import urllib
import urllib.request
import re
from selenium import webdriver
from time import sleep
from selenium.webdriver.common.by import By
'''
driver = webdriver.Chrome()
driver.get('http://www.qdtech.ai/eztalk2/#/project/detail?project_id=9157308')

#最大化窗口
driver.maximize_window()
sleep(2)

#定位手机号输入框
driver.find_element(by=By.XPATH,value="//input[@type='text']").click()
sleep(2)

#在输入框中输入手机号
driver.find_element(by=By.XPATH,value="//input[@placeholder='账号']").send_keys("xiaochun.guo@qdtech.ai")

#定位密码输入框
driver.find_element(by=By.XPATH,value="//input[@placeholder='密码']").click()
sleep(2)

#输入密码
driver.find_element(by=By.XPATH,value="//input[@placeholder='密码']").send_keys("Qdtech@2021")
sleep(2)

#点击登录按钮
driver.find_element(by=By.XPATH,value="//button[@class='el-button qd-login__btn el-button--primary']").click()

sleep(10)
'''
#加载页面
def load_page(url):
    request=urllib.request.Request(url)
    response=urllib.request.urlopen(request)
    data=response.read()
    return data
#下载图片
def get_image(html):
    regx = r'img[\S]*png'
    # regx = r'http://[\S]*png'
    pattern = re.compile(regx)

    get_image=re.findall(pattern,repr(html))
    print("get_image:%s"% get_image)

    list = []
    for i in get_image:
        i = 'https://'+i
        list.append(i)
    print('list:%s'%list)

    num = 1
    for img in list:
        image = load_page(img)
        with open('F:\\study\\tool\img\\%s.jpg'%num,'wb') as fb:
             fb.write(image)
             print("正在下载第%s张图片" %num)
             num=num+1
    print("下载完成！")

url='https://www.qdtech.ai/eztalk2/#/login'
html=load_page(url)
print(html)
get_image(html)


print("关闭文件成功!!")

