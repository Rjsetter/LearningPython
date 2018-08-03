#_*_ encoding:utf-8_*_
from urllib import request, parse
import json
import sys
word = sys.argv[1]
if __name__ == '__main__':

	Request_Url = 'http://fanyi.youdao.com/translate' #有道翻译的接口
	#创建Form_data字典，储存网页上对应的form data
	Form_Data = {}
	Form_Data['i'] = word
	Form_Data['doctype'] = 'json'


	#使用urlopen方法转换为标准格式
	data = parse.urlencode(Form_Data).encode('utf-8')
	response = request.urlopen(Request_Url, data)
	html = response.read().decode('utf-8')
	translate_results = json.loads(html)  #以json格式载入
	translate_results = translate_results['translateResult'][0][0]['tgt']
	print(translate_results) #输出结果