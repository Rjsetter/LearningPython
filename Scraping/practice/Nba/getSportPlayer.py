#_*_encoding:utf-8_*_
from selenium import webdriver # 从selenium导入webdriver
from bs4 import BeautifulSoup
import time 
class PlayerInfo(object):
	"""存储球员信息"""
	def __init__(self):
		self.ch_name = []
		self.eg_name = []
		self.num = []
		self.position =[]
		self.height = []
		self.weight = []
		self.age = []
		self.years = []

def get_info(url_, pi):
	"""获取页面上的球员信息"""
	chrome_options = webdriver.ChromeOptions()
	prefs = {"profile.managed_default_content_settings.images":2}
	chrome_options.add_experimental_option("prefs",prefs)
	driver = webdriver.Chrome(chrome_options=chrome_options)
	driver.get(url_) 
	html_text=driver.page_source    #获取网页源码
	soup = BeautifulSoup(html_text)
	driver.quit()  #关闭窗口
	#获取球员信息模块
	player_info = soup.find_all('tr', class_='show')
	info = BeautifulSoup(str(player_info))
	info_td = info.find_all('td')
	lent = len(info_td)
	for x in range(lent):
		i = x%9
		if i == 0:
			pass
		elif i == 1:
			contents = info_td[x].contents  #获取标签的直接子节点
			pi.ch_name.append(contents[1].string)
		elif i == 2:
			contents = info_td[x].contents  #获取标签的直接子节点
			pi.eg_name.append(contents[1].string)	
		elif i == 3:
			# print(infoof[x].string)
			pi.num.append(info_td[x].string)
		elif i == 4:
			pi.position.append(str(info_td[x].string))
		elif i == 5:
			pi.height.append(info_td[x].string)
		elif i == 6:
			pi.weight.append(info_td[x].string)
		elif i == 7:
			pi.age.append(info_td[x].string)
		else:
			pi.years.append((info_td[x].string))


if __name__ == '__main__':
	pi = PlayerInfo()
	start_time = time.time()
	for i in range(1,30):
		get_info('http://nba.stats.qq.com/player/list.htm#teamId={}'.format(i), pi)
	count = len(pi.num)
	for i in range(count):
		print("%s\t%s\t%s\t%s\t%s\t%s\t%s\t%s"%(pi.ch_name[i],pi.eg_name[i],pi.num[i],pi.position[i],pi.height[i],pi.weight[i],pi.age[i],pi.years[i]))
	end_time = time.time()
	print("耗时：",(start_time-end_time))
	print("球员数量：",count)