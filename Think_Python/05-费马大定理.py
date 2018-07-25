# _*_ encoding:utf-8 _*_

#费马大定理，又被称为“费马最后的定理”，由17世纪法国数学家皮耶·德·费玛提出。
#它断言当整数n >2时，关于x, y, z的方程 x^n + y^n = z^n 没有正整数解。

def check_fermat(x, y, z, n):
	if x**n + y**n == z**n and n>2:
		print("it can't work!")
	else:
		print("Fermat is right!")

def main():
	print("please input x,y,z,n to comfire Fermat's Last Theorem:")
	x = int(input("x="))
	y = int(input("y="))
	z = int(input("z="))
	n = int(input("n(n must >2)="))
	check_fermat(x, y, z, n)

if __name__ == '__main__':
	main()