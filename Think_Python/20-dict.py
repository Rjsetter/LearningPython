
import time
def wordslist1():
	f = open('words.txt','r')
	t = []
	for line in f:
		word = line.strip()
		t.append(word)
	return t

def dict_word():
	d = dict()
	f = open('words.txt')
	for line in f:
		word = line.strip()
		d[word] = 1
	return d

def binary_search_loop(lst,value):  
    """循环方式实现二分查找"""
    low, high = 0, len(lst)-1  
    while low <= high:  
        mid = int((low + high) / 2)  
        if lst[mid] < value:  
            low = mid + 1  
        elif lst[mid] > value:  
            high = mid - 1
        else:
            return mid  
    return None



d = dict_word()
# print(d)
start_time = time.time()
if 'selsyn' in d:
	print("Done!")
escape_time = time.time() - start_time	
print("所用的时间：",escape_time)
te = wordslist1()
start_time = time.time()
binary_search_loop(te,'selsyn')
escape_time = time.time() - start_time
print("所用的时间：",escape_time)