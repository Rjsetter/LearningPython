# #coding=utf-8
# from selenium import webdriver # 从selenium导入webdriver
# # chromeOptions = webdriver.ChromeOptions()
# # chromeOptions.add_argument('--proxy-server=http://ip:port')
# driver = webdriver.Chrome(chrome_options = chromeOptions)
# # driver = webdriver.Chrome()  # Optional argument, if not specified will search path.
# driver.get('https://www.baidu.com') # 获取百度页面

# coding=utf-8
import time
from selenium import webdriver
 
driver = webdriver.Chrome() # 打开chrome，如果没有安装chrome,换成webdriver.Firefox()
driver.maximize_window()    # 最大化浏览器窗口
driver.implicitly_wait(8)   # 设置隐式时间等待
 
driver.get("https://www.baidu.com")  # 地址栏输入百度地址
driver.find_element_by_xpath("//*[@id='kw']").send_keys("selenium")  # 搜索输入框输入Selenium
driver.find_element_by_xpath("//*[@id='su']").click()  #点击百度一下按钮
 
# 导入time模块，等待2秒
 
time.sleep(2) 
# 这里通过元素XPath表达式来确定该元素显示在结果列表，从而判断Selenium官网这个链接显示在结果列表。
# 这里采用了相对元素定位方法/../
# 通过selenium方法is_displayed() 来判断我们的目标元素是否在页面显示。
driver.find_element_by_xpath("//div/h3/a[text()='官网']/../a/em[text()='Selenium']").is_displayed()
driver.quit()
