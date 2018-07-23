#_*_ encoding:utf-8_*_

def sed(mStr, rStr, file1, file2):
	try:
		f1 = open(file1, 'r')
		f2 = open(file2, 'w')
		for line in f1:
			line = line.replace(mStr, rStr)
			f2.write(line)
		f1.close()
		f2.close()
	except:
		print("something went wrong!")

sed('test', 'TEST', 'oldfile.txt','newfile2.txt')
f = open('newfile.txt')
txt = f.read()
print(txt)