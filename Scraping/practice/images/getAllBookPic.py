#_*_ encoding:utf-8_*_
"""
info：
	写个爬虫软件，爬取http://books.toscrape.com/网页上所有书本的图片
Modify：
	2018-8-2
"""
from bs4 import BeautifulSoup
import requests, time, re
from retrying  import retry
class getPicture(object):
	"""获取所有图片的类"""
	def __init__(self):
		self.url = ['http://books.toscrape.com/']   #存取网页的地址,默认为首页

	def getAllUrls(self):
		"""经过分析可以知道地址的规律"""
		url = 'http://books.toscrape.com/'
		for i in range(2,51):
			s = 'catalogue/page-%d.html'%i
			self.url.append(''.join([url,s]))   #通过join(),获取所有子网址
	

	@retry(stop_max_attempt_number=10)
	#retry_on_exception=ReadTimeout 
	def loadPic(self, url__): 
		print(url__)
		try:
			req = requests.get(url__, timeout=3)
		except Exception:
			print("超时！休息五秒再继续尝试！")
			time.sleep(5)
		return req





	def getPerPage(self, url_, index):
		"""获取每一页的图片"""
		count = 1
		req = requests.get(url = url_)
		baseUrl = 'http://books.toscrape.com/'
		html = req.text
		bf = BeautifulSoup(html)
		img = bf.find_all( 'img')    #通过img标签获取图片地址信息地址
		pattern = re.compile(r'm.*') 
		for i in img:
			x = i.attrs.get('src','None')
			ret = re.search(pattern, x)   #排除首页后面图片地址获取前面会有../
			url__ = baseUrl+ret.group()    #获取图片地址
			name = str(index)+'-'+str(count)
			f = open(name+'.jpg','wb')
			req_ = self.loadPic(url__)
			if req_:
				buf = req_.content     #图片内容
				f.write(buf)
				f.close()
				count += 1
			else:
				print("读取图片出现错误！")
			


if __name__ == '__main__':
	Pic = getPicture()
	Pic.getAllUrls()
	# Pic.getPerPage(Pic.url[2],2) # fortest
	ind = len(Pic.url)
	start_time = time.time()
	print("开始爬取1-10页图片")
	for i in range(10):
		Pic.getPerPage(Pic.url[i],i+1)
	print("这十页的图片爬取完成！\n")
	print("休息2秒")
	time.sleep(2)
	print("开始爬取11-20页图片")
	for i in range(10, 20):
		Pic.getPerPage(Pic.url[i],i+1)
	print("这十页的图片爬取完成！\n")
	print("休息2秒")
	time.sleep(2)
	print("开始爬取20-30页图片")
	for i in range(20, 30):
		Pic.getPerPage(Pic.url[i],i+1)
	print("这十页的图片爬取完成！")
	print("休息2秒")
	time.sleep(2)
	print("开始爬取30-40页图片")
	for i in range(30, 40):
		Pic.getPerPage(Pic.url[i],i+1)
	print("这十页的图片爬取完成！")
	print("休息2秒")
	time.sleep(2)
	print("开始爬取40-50页图片")
	for i in range(40, 50):
		Pic.getPerPage(Pic.url[i],i+1)
	print("这十页的图片爬取完成！")
	end_time = time.time()
	processtime = start_time - end_time
	print("总耗时：", processtime)