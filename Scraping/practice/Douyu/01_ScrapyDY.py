#coding=utf-8
from bs4 import BeautifulSoup
from selenium import webdriver
from collections import OrderedDict
import time
from log import logger   #日志
from Db import insert
# from retrying  import retry
from selenium.webdriver.chrome.options import Options

# chrome_options = Options()
# chrome_options.add_argument('--headless')
# chrome_options.add_argument('--disable-gpu')
# prefs = {"profile.managed_default_content_settings.images": 2}
# chrome_options.add_experimental_option("prefs", prefs)

urls = OrderedDict()     #有序字典，存取斗鱼分类的链接，用字典存储，分类名称：链接
Count_num = 1


#设定重试机制，以防网络波动


def get_info(driver):
	"""获取一个页面中的所有数据"""
	global Count_num
	type_ = ''
	tCount = 0
	for page in range(1, 121):
		tCount += 1
		"""如果满的话，每一页有120个主播"""
		try:
			#主播名字
			dy_name = driver.find_element_by_css_selector('#live-list-contentbox > li:nth-child({}) > a > div.mes > p > span.dy-name.ellipsis.fl'.format(page)).text
			#直播分类
			dy_type = driver.find_element_by_css_selector('#live-list-contentbox > li:nth-child({}) > a > div.mes > div > span'.format(page)).text
			#直播标题
			dy_title = ddy_title = driver.find_element_by_css_selector("#live-list-contentbox > li:nth-child({}) > a > div.mes > div > h3".format(page)).text
			#直播热度
			dy_num = driver.find_element_by_css_selector("#live-list-contentbox > li:nth-child({}) > a > div.mes > p > span.dy-num.fr".format(page)).text
			if dy_num.isdigit():
				pass
			else:
				dy_num = dy_num.replace('万','')
				dy_num = int(float(dy_num)*10000)      #转换为数字
			#主播标签
			tags = ''
			for i in range(1,4):
				try:
					dy_tag = driver.find_element_by_css_selector("#live-list-contentbox > li:nth-child({}) > a > div.impress-tag-list > span:nth-child({})".format(page, i)).text
					tags = tags + "[" + dy_tag + "] "
				except:
					# print("该主播没有标签！")
					tags = '该主播没有标签!'
					break
		except:
			logger.info("{}类已经爬取完毕，一共有{}条数据。".format(type_, tCount))
			logger.info("一共已经爬取{}条数据！".format(Count_num))
			break
		Sql_insert = "INSERT INTO douyu3(dy_name,dy_type,dy_title,dy_num,dy_tag)VALUES('%s','%s','%s','%d','%s')"%(dy_name,dy_type,dy_title,int(dy_num),tags)
		print("正在爬取第{}个主播：".format(Count_num))
		# print("名字：", dy_name)
		# print("分类：", dy_type)
		# print("标题：", dy_title)
		# print("热度：", dy_num )
		# print("标签：", tags)
		try:
			insert(Sql_insert)
		except:
			print("插入错误！")
			logger.info("{}插入错误！".format(dy_name))
			pass
		Count_num += 1
		

def get_one_type(url_, name):
	# chrome_options=chrome_options
	driver = webdriver.Chrome()
	# driver.maximize_window()
	driver.get(url_)
	Flag = True
	page = 1
	while Flag:
		print("开始第{}页爬取：".format(page))
		time.sleep(0.5)
		get_info(driver)
		try:
			tag = driver.find_element_by_css_selector("#J-pager > a.shark-pager-next").get_attribute('class')
			if tag == 'shark-pager-next':
				driver.find_element_by_css_selector("#J-pager > a.shark-pager-next").click()
				print("开始下一页主播爬取！")
				page += 1
			else:
				Flag = False
		except:
			logger.info("{}类型主播目前在播人数不足１２０人！".format(name))
			Flag  = False #已经爬取完该类所有主播
	driver.quit() 
	#J-pager > a.shark-pager-next.shark-pager-disable.shark-pager-disable-next

def get_url():
	global urls
	# chrome_options = Options()
	# chrome_options.add_argument('--headless')
	# chrome_options.add_argument('--disable-gpu')
	# chrome_options=chrome_options
	driver = webdriver.Chrome()
	driver.maximize_window()
	driver.get('https://www.douyu.com/directory')
	for i in range(1, 6):
		target = driver.find_element_by_css_selector('#live-list-contentbox > li:nth-child({}) > a'.format(i))
		name = target.text
		url = target.get_attribute('href')
		urls[name] = url
	driver.quit() 


def show_urls():
	for name, url in urls.items():
		print("{}:{}".format(name, url))


if __name__ == '__main__':
	print("先收集所有分类的地址：")
	get_url()
	print("收集完成，下面开始爬数据！！！")
	s_time = time.time()
	for name, url in urls.items():
		get_one_type(url, name)
	e_time = time.time()
	print("总耗时：", (e_time - s_time))
	print("总人数：",Count_num)

