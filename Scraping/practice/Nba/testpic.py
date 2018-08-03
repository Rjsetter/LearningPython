from selenium import webdriver
 

options=webdriver.ChromeOptions()
prefs = {
    'profile.default_content_setting_values' : {
        'images' : 2
    }
}
options.add_experimental_option('prefs',prefs)
 
browser = webdriver.Chrome(chrome_options=options)
browser.get("https://www.baidu.com/")