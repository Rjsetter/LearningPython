#_*_ encoding:utf-8_*_
from urllib import request


if __name__ == '__main__':
	req = request.Request("http://fanyi.baidu.com")
	response = request.urlopen(req)
	print("geturl:\n",response.geturl())
	print("*"*30)
	print("info:\n",response.info())
	print("*"*30)
	print("getcode:\n",response.getcode())

	
	