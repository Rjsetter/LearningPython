#_*_ encoding:utf-8 _*_
class point(object):
	def __init__(self ,x ,y):
		self.x = x
		self.y = y

	def __str__(self):
		return '(%d,%d)'%(self.x, self.y)

	def __add__(self, other):
		return self.x+other.x,self.y+other.y

p1 = point(5,6)
p2 = point(5,5)
print(p1+p2)