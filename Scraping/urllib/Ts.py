#_*_ encoding:utf-8_*_
"""
说明：
	创建一个链接有道翻译的脚本，命名为Ts.py,
	运行python Ts.py input
	其中input为你的输入，可以是单词，也可以是字符串。
Modify:
	2018-8-2

"""
from urllib import request, parse
import json
import sys
word = sys.argv[1]

if __name__ == '__main__':
	Request_Url = 'http://fanyi.youdao.com/translate' #有道翻译的接口
	
	Form_Data = {}
	Form_Data['i'] = word
	Form_Data['doctype'] = 'json'


	#使用urlopen方法转换为标准格式
	data = parse.urlencode(Form_Data).encode('utf-8')     #数据转换
	response = request.urlopen(Request_Url, data)		#提交数据并解析
	html = response.read().decode('utf-8')		#服务器返回结果读取
	translate_results = json.loads(html)  		#以json格式载入
	translate_results = translate_results['translateResult'][0][0]['tgt']
	print(translate_results) #输出结果