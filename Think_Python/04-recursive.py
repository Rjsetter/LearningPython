# def print_n(s, n):
# 	if n <= 0:
# 		return 
# 	print(s)
# 	print_n(s, n-1)
# print_n("hello!",3)
def print_n():
	print("test")


def recusive(fun, n):
	if n <= 0:
		print("递归结束！")
		return
	fun()
	recusive(fun, n-1)



recusive(print_n,10)
