# _*_ encodig:utf-8_*_
import time

def fibonacci(n):
	if n == 0:
		return 0
	if n == 1:
		return 1
	else:
		return fibonacci(n-1) + fibonacci(n-2)

known = {0:0,1:1}
def finbonacci_2(n):
	if n in known:
		return known[n]

	res = finbonacci_2(n-1) + finbonacci_2(n-2)
	known[n] = res
	return res


start_time = time.time()	
print(fibonacci(50))
escape_time = time.time() - start_time
print(escape_time)
start_time = time.time()	
print(finbonacci_2(900))	

escape_time = time.time() - start_time
print(escape_time)
