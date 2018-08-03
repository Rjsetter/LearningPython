#_*_ encoding:utf-8_*_
from bs4 import BeautifulSoup
import requests


if __name__ == '__main__':
	target = 'http://www.biqukan.com/1_1094/'     #目标网址
	server = 'http://www.biqukan.com/'
	req = requests.get(url = target)
	html = req.text
	bf = BeautifulSoup(html)
	div = bf.find_all('div', class_ = 'listmain')
	a_bf = BeautifulSoup(str(div[0]))
	a = a_bf.find_all('a')
	for each in a:
		print(each)
		print(each.string, server +each.get('href'))
		break
# -*- coding:UTF-8 -*-
# from bs4 import BeautifulSoup
# import requests
# if __name__ == "__main__":
#      server = 'http://www.biqukan.com/'
#      target = 'http://www.biqukan.com/1_1094/'
#      req = requests.get(url = target) html = req.text
#      div_bf = BeautifulSoup(html)
#      div = div_bf.find_all('div', class_ = 'listmain')
#      a_bf = BeautifulSoup(str(div[0]))
#      a = a_bf.find_all('a')
#      for each in a:
#           print(each.string, server + each.get('href'))