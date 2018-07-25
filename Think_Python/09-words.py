#_*_ encoding:utf-8_*_
fin = open('words.txt')
# for line in fin:
# 	if len(line) > 20:
# 		word = line.strip()
# 		print(word)

def has_no_e(f):
	count = 0
	count_e = 0
	for line in f:
		count+=1
		if 'e' not in line:
			count_e+=1
			word = line.strip()
			print(word)
	print("e/total",count_e/count)

def avoids(word, avoid_word):
	for letter in word:
		if letter in avoid_word:
			return False
	print("zdssda")
	return True


avoids("tttttts",'qqweqw')

# has_no_e(fin)
