#_*_ encoding:utf-8_*_
from urllib import request
import chardet   #自动获取网页编码

if __name__ == '__main__':
	response = request.urlopen("http://fanyi.baidu.com")
	html = response.read()
	# html = html.decode('utf-8')
	# print(html)
	charset = chardet.detect(html)
	print(charset.get('key','not found'))
	html = html.decode(charset.get('encoding','None'))
	print(html)
	