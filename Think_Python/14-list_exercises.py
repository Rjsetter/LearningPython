#_*_ encoding:utf-8 _*_
import itertools
import random
def nested_sum(l):
	"""接受一个内嵌整数列表，并将列表中所有整数加起来返回结果"""
	result = 0
	for x in l:
		result = result + sum(x)
	return result


def cumsum(l):
	"""接收一个数字列表，返回累计和"""
	res = []
	for i in range(len(l)):
		t = sum(l[:(i+1)])
		res.append(t)
	return res


def middle(l):
	"""接收一个列表作为形参，返回一个除了首尾元素的列表"""
	return l[1:len(l)-1]


def chop(l):
	"""接收一个列表，修改它，删除第一个和最后一个元素并返回None"""
	l = l[1:len(l)-1]
	print("这是在函数chop内部打印的，它返回一个None:",l)
	return None


def is_sorted(l):
	"""接收一个列表当形参，并当列表是升序排好时返回true，否则返回false"""
	new = sorted(l)
	if new == l :
		return True
	return False


def is_anagram(word1,word2):
	"""接收两个单词，如果重新排序其中一个可以得到另外一个则返回true"""
	if word1 == word2:
		"""不用重排就能得到"""
		return True
	s = [''.join(x) for x in itertools.permutations(word2)]
	print(s)
	if word1 in s:
		return True
	return False


def has_duplicates(l):
	"""当列表中任一元素出现多于一次时返回True"""
	return len(set(l)) < len(l)


def birthday_random(n):
	"""随机生成n位学生的生日，并存入列表中然后返回列表"""
	t = []
	for i in range(n):
		day = random.randint(1,365)
		t.append(day)
	return t


def count_matches(num_students, num_simulations):
    count = 0
    for i in range(num_simulations):
        t = birthday_random(num_students)
        if has_duplicates(t):
            count += 1
    return count

def main():
    """Runs the birthday simulation and prints the number of matches."""
    num_students = 23
    num_simulations = 1000
    count = count_matches(num_students, num_simulations)

    print('After %d simulations' % num_simulations)
    print('with %d students' % num_students)
    print('there were %d simulations with at least one match' % count)


if __name__ == '__main__':
	main()
	l = [1,2,3]
	t1 = nested_sum([[1,2,3],[4,5]])
	t2 = cumsum([1,2,3])
	t3 = middle(l)
	t4 = chop([1,2,3,4])
	t5 = is_sorted([2,3,4])
	t6 = is_sorted([3,2,4])
	t7 = is_sorted(['b', 'a'])
	t8 = is_sorted(['a', 'b'])
	t9 = is_anagram('hello','hello')
	t10 = is_anagram('hello','as')
	t11 = is_anagram('abc', 'cba')
	t12 = has_duplicates(['a', 'b', 'c'])
	t13 = has_duplicates(['a', 'a', 'b'])
	print(t1)
	print(t2)
	print(t3)
	print("原来的列表：",l)
	print(t4)
	print("应该打出false：",t6)
	print("应该打出true:",t5)
	print("应该打出false：",t7)
	print("应该打出true:",t8)
	print("tft",t9,t10,t11)
	print('ft',t12,t13)