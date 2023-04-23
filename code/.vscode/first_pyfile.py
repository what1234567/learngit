# //*[@id]/div/div[1]/h3/a
# //*[@id="boxWrapper"]/div[1]/div/div/div[1]/div/div/a/span
# //*[@id="tablepress-1"]/tbody/tr[1]/td[7]/a

from selenium import  webdriver
import time
from selenium.webdriver.common.by import By

options = webdriver.ChromeOptions()
options.add_experimental_option('detach', True)  #不自动关闭浏览器
# options.add_argument('--start-maximized')#浏览器窗口最大化
driver=webdriver.Chrome(options=options)


# 2、driver.get方法将定位在给定的URL的网页 。

driver.get("https://www.baidu.com/s?ie=UTF-8&wd=%E7%99%BE%E5%BA%A6%E7%BF%BB%E8%AF%91") # get接受url可以是任何网址，此处以百度为例
time.sleep(5)
# 3、定位元素 。

# //*[@id="3"]/div/div[1]/h3/a
for i in range(2,3):
    i = str(i)
    button = driver.find_element(by=By.XPATH, value="//*[@id=" + i + "]/div/div[1]/h3/a")
    print(button.href)

    time.sleep(3)



# 3.2、用id定位点击对象，用click()触发点击事件 ：点击百度一下

# driver.find_element(by=By.ID, value='su').click()



# 4、退出访问的实例网站。

driver.quit()





# #查找页面的“设置”选项，并进行点击
# driver.find_elements_by_link_text('设置')[0].click()
# #打开设置后找到“搜索设置”选项，设置为每页显示50条
# driver.find_elements_by_link_text('搜索设置')[0].click()
# sleep(2)
# m = driver.find_element_by_id('nr')
# sleep(2)
# m.find_element_by_xpath('l/*[@id="nr"]/option[3]').click()
# sleep(2)
# #处理弹出的警告页面
# driver.find_element_by_class_name("prefpanelgo").click()
# sleep(2)
# driver.switch_to_alert().accept0sleep(2)
# #找到百度的输入框，并输入“selenium"
# driver.find_element_by_id('kw').send_keys('selenium"')
# sleep(2)
# #点击搜索按钮
# driver.find_element_by_id('su').click()
# sleep(2)
# #在打开的页面中找到“Selenium-开源中国社区”，并打开这个页面driver.find_elements_by_link_text('Selenium -开源中国社区')[O].clicko
