from selenium import webdriver
import time
from selenium.webdriver.firefox.firefox_profile import FirefoxProfile
from lxml import etree
 ## get the Firefox profile object
firefoxProfile = FirefoxProfile()
 ## Disable CSS
firefoxProfile.set_preference('permissions.default.stylesheet', 2)
 ## Disable images
firefoxProfile.set_preference('permissions.default.image', 2)
 ## Disable Flash
firefoxProfile.set_preference('dom.ipc.plugins.enabled.libflashplayer.so',
 'false')
driver = webdriver.Firefox(firefoxProfile)
driver.get("https://www.douyu.com/g_jdqscjzc")
pages = driver.page_source
selector = etree.HTML(pages)
dy_name = selector.xpath('//*[@id="live-list-contentbox"]/li[1]/a/div[1]/p/span[1]/text()')[0]
print(selector)
print(dy_name)
# print("2秒后关闭浏览器")
# time.sleep(2)
# driver.quit()
# //*[@id="live-list-contentbox"]/li[1]/a/div[1]/p/span[1]