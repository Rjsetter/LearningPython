# 如何加载页面的时候不显示图片
from selenium import webdriver
 
# 设置不加载图片
chrome_opt = webdriver.ChromeOptions()
# 不加载图片，设置的参数很固定
prefs = {"profile.managed_default_content_settings.images": 2}
 
# 将参数设置到chrome_opt里面
chrome_opt.add_experimental_option("prefs", prefs)
 
# 模拟浏览器的时候将chrome_opt添加进去
browser = webdriver.Chrome( chrome_options=chrome_opt)
 
browser.get("http://www.bilibili.com")