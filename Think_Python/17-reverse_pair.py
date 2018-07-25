# _*_ encodig:utf-8_*_
import time
import bisect
def wordslist1():
	"""创建单词列表"""
	f = open('words.txt','r')
	t = ['None']
	for line in f:
		word = line.strip()
		t.append(word)
	return t

def find_reverse(t):
	for i in range(100):
		j = i+1
		temp = t[i][::-1]
		for j in range(100):
			if temp == t[j]:
				print("(%s,%s)"%(t[i],t[j]))

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
    return False


def find_reverse2(t):
	count = 0
	for i in range(len(t)):
		temp = t[i][::-1]
		index = binary_search_loop(t, temp)
		if index != False:
			print("(%s,%s)"%(t[i],t[index]))
			count += 1
	print(count)	



te = wordslist1()
print("单词表已经生成，下面开始找寻单词表中的反响对：")
start_time = time.time()
find_reverse2(te)
escape_time = time.time() - start_time
print("结束！")
print("所用的时间：",escape_time)
