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
#刚开始的时候进入了一个小白盲区，先把函数print_n给f，再把f传递给recusive函数，
#然后递归函数中一直无法使用函数打印


recusive(print_n,10)
