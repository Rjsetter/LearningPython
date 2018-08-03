#_*_ encoding:utf-8_*_

import requests

if __name__ == '__main__':
	target = 'http://www.biqukan.com/1_1094/5403177.html'     #目标网址
	req = requests.get(url=target)
	print(req.text)