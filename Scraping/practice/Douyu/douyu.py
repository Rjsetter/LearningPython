#coding=utf-8
from bs4 import BeautifulSoup
from selenium import webdriver
from collections import OrderedDict
import time
urls = OrderedDict()     #有序字典，存取斗鱼分类的链接，用字典存储，分类名称：链接
Count_num = 1

def get_info(driver):
	"""获取一个页面中的所有数据"""
	global Count_num
	for page in range(1, 5):
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
					print("该主播没有标签！")
					tags = '该主播没有标签!'
					break
		except:
			print("该页已经没有主播！")
			break
		print("第{}个主播：".format(Count_num))
		print("名字：", dy_name)
		print("分类：", dy_type)
		print("标题：", dy_title)
		print("热度：", dy_num )
		print("标签：", tags)
		Count_num += 1
		

def get_one_type(url_):
	driver = webdriver.Chrome()
	# driver.maximize_window()
	driver.get(url)
	Flag = True
	page = 1
	while Flag:
		print("开始第{}页爬取：".format(page))
		time.sleep(1)
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
			print("出现错误了！该类型在直播的主播比较少")
			Flag  = False #已经爬取完该类所有主播
	driver.quit() 
	#J-pager > a.shark-pager-next.shark-pager-disable.shark-pager-disable-next

def get_url():
	global urls
	driver = webdriver.Chrome()
	driver.maximize_window()
	driver.get('https://www.douyu.com/directory')
	for i in range(1, 290):
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
	for k, url in urls.items():
		get_one_type(url)
	e_time = time.time()
	print("总耗时：", (e_time - s_time))
	print("总人数：",Count_num)