#coding=utf-8
from bs4 import BeautifulSoup
from selenium import webdriver
from collections import OrderedDict
from time import time, sleep
from log import logger   #日志
from Db import insert
from lxml import etree
from selenium.webdriver.firefox.firefox_profile import FirefoxProfile
import threading
# from retrying  import retry


urls = OrderedDict()     #有序字典，存取斗鱼分类的链接，用字典存储，分类名称：链接
Count_num = 1
Count_page = 0
Count_time = 0

#设定重试机制，以防网络波动

def get_firefox():
	"""获取禁止加载图片和css的firefox接口，还可以添加headless"""
	 ## get the Firefox profile object
	firefoxProfile = FirefoxProfile()
 	## Disable CSS
	firefoxProfile.set_preference('permissions.default.stylesheet', 2)
 	## Disable images
	firefoxProfile.set_preference('permissions.default.image', 2)
 	## Disable Flash
	firefoxProfile.set_preference('dom.ipc.plugins.enabled.libflashplayer.so','false')
 	## set bowser headless 
	options = webdriver.FirefoxOptions()
	options.add_argument('-headless')
	driver = webdriver.Firefox(firefoxProfile,options=options)
	return driver


def get_info(source):
	"""获取一个页面中的所有数据"""
	global Count_num
	selector = etree.HTML(source)
	print(selector)
	type_ = ''
	tCount = 0
	for page in range(1, 121):
		tCount += 1
		"""如果满的话，每一页有120个主播"""
		try:
			#主播名字
			dy_name = selector.xpath('//*[@id="live-list-contentbox"]/li[%d]/a/div[1]/p/span[1]/text()'%(page))[0]
			#直播分类
			dy_type = selector.xpath('//*[@id="live-list-contentbox"]/li[%d]/a/div[1]/div/span/text()'%(page))[0]
			#直播标题
			dy_title = selector.xpath('//*[@id="live-list-contentbox"]/li[{}]/a/div[1]/div/h3/text()'.format(page))[0]
			#直播热度
			dy_num = selector.xpath('//*[@id="live-list-contentbox"]/li[{}]/a/div[1]/p/span[2]/text()'.format(page))[0]
			if dy_num.isdigit():
				pass
			else:
				dy_num = dy_num.replace('万','')
				dy_num = int(float(dy_num)*10000)      #转换为数字
			#主播标签
			tags = ''
			for i in range(1,4):
				try:
					dy_tag = selector.xpath('//*[@id="live-list-contentbox"]/li[%d]/a/div[2]/span[%d]/text()'%(page,i))[0]
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
		print("正在爬取第{}个主播!".format(Count_num))
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
	global Count_page
	global Count_time
	t1 = time()
	driver = get_firefox()
	t = time()- t1
	Count_time += t
	driver.get(url_)
	Flag = True
	page = 1
	threads = []
	while Flag:
		Count_page += 1
		print("开始第{}页爬取：".format(page))
		pages = driver.page_source		
		t = threading.Thread(target=get_info, args=(pages,))
		threads.append(t)
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
	for i in range(len(threads)):
		threads[i].start()

	for i in range(len(threads)):
		threads[i].join()
	driver.quit() 
	#J-pager > a.shark-pager-next.shark-pager-disable.shark-pager-disable-next

def get_url():
	global urls
	driver = get_firefox()
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
	s_time = time()
	count = 0
	for name, url in urls.items():
		count += 1
		get_one_type(url, name)
	e_time = time()
	print("总耗时：", (e_time - s_time))
	print("总人数：",Count_num)
	print("爬取页数：",Count_page)
	print("启动浏览器总用时：",Count_time)
	print("打开了{}个分类：".format(count))

