# _*_ encodig:utf-8_*_
import time
import bisect
#二分查找模块bisect
def wordslist1():
	"""创建单词列表"""
	f = open('words.txt','r')
	t = []
	for line in f:
		word = line.strip()
		t.append(word)
	return t


def binary_search_recursion(lst, value, low, high):  
    """递归方式实现二分查找"""
    if high < low:  
        return None
    mid = int((low + high) / 2)  
    if lst[mid] > value:  
        return binary_search_recursion(lst, value, low, mid-1)  
    elif lst[mid] < value:  
        return binary_search_recursion(lst, value, mid+1, high)  
    else:  
        return mid 


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


if __name__ == '__main__':
	t = wordslist1()
	start_time = time.time()
	s = binary_search_recursion(t, 'summations', 0, len(t))
	process_time = time.time() - start_time
	print("递归用的时间：", process_time)
	print((s+1))
	start_time = time.time()
	s = binary_search_loop(t,'summations')
	process_time = time.time() - start_time
	print("循环用的时间：", process_time)
	print((s+1))
	
	index = bisect.bisect(t,'summations')
	print("index:",index)
	# import random
	# lst = [random.randint(0, 10000) for i in range(100000)]
	# lst.sort()
 
	# def test_recursion():
	# 	binary_search_recursion(lst, 999, 0, len(lst)-1)
 
	# def test_loop():
	# 	binary_search_loop(lst, 999)
 
	# import timeit
	# t1 = timeit.Timer("test_recursion()", setup="from __main__ import test_recursion")
	# t2 = timeit.Timer("test_loop()", setup="from __main__ import test_loop")
 
	# print ("Recursion:", t1.timeit())
	# print ("Loop:", t2.timeit())
