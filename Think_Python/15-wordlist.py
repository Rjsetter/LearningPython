#_*_ encoding:utf-8 _*_
import time
def wordslist1():
	f = open('words.txt','r')
	t = []
	for line in f:
		word = line.strip()
		t.append(word)
	return t


def wordslist2():
	t = []
	f = open('words.txt')
	for line in f:
		word = line.strip()
		t = t + [word]
	return t

start_time = time.time()
t = wordslist1()
elapsed_time = time.time() - start_time

print(len(t))
print(t[:10])
print(elapsed_time, 'seconds')

start_time = time.time()
t = wordslist2()
elapsed_time = time.time() - start_time

print(len(t))
print(t[:10])
print(elapsed_time, 'seconds')