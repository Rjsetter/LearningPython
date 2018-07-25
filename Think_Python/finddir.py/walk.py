#_*_encoding:utf-8_*_

#os.path.splitext(path) 
#分离文件名与扩展名；默认返回(fname,fextension)元组，可做分片操作 

# os.path.basename(path) 
# 返回path最后的文件名。如何path以／或\结尾，那么就会返回空值。即os.path.split(path)的第二个元素。
import os
#遍历文件夹返回后缀文件的集合
#全局变量，用来存储.mp3后缀的文件的名字
name = []
def walk(dirname):
	for name in os.listdir(dirname):
		path = os.path.join(dirname, name)

		if os.path.isfile(path):
			name,ext = os.path.splitext(path)  #用解元组方式获取文件后缀名用来进行判断
			if ext == ".mp3":
				print(path)
				name_ = os.path.basename(path)
				name.append(name)
		else:
			walk(path)


#md5校验
def md5(filename):
	cmd = 'md5sum' + filename
	fp = os.popen(cmd)
	res = fp.read()
	fp.close()
	return res


#判断是否重复
def isRepert():
	for n in name:
		for m in name[1:]:
			if n == m:
				if md5(n) == md5(m):
					print("它们可能有相同的内容")

# if __name__ == '__main__':
# 	walk()
# 	isRepert()