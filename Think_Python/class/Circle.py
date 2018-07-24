#_*_ encoding:utf-8 _*_
import math,copy,turtle


class Point(object):
	"""定义一个point类"""
	def __init__(self, x, y):
		self.pX = x
		self.pY = y


class Circle(Point):
	"""定义一个圆类，继承point类"""
	def __init__(self, x, y, radius):
		super(Circle, self).__init__(x, y)
		self.cRadius = radius


class Rectangle(Point):
	"""定义一个矩形类，point指向矩形左下角的点"""
	def __init__(self, x, y, width, height):
		# super(Rectangle,self).__init__(x,y)
		self.width = width
		self.height = height
		self.point = Point(x,y)


def points_distance(cir,poi):
	"""计算两个点之间的距离"""
	X = abs(cir.pX-poi.pX)
	Y = abs(cir.pY-poi.pY)
	return math.sqrt(X**2 + Y**2)



def point_in_circle(Circle, Point):
	"""判断点在圆内"""
	d = points_distance(Circle, Point)
	if d <= Circle.cRadius:
		print("Point is in circle!")
		return True
	else:
		print("Point is not in circle!")
		return False

def rect_in_circle(Circle, Rectangle):
	"""判断矩形在圆内"""
	p = Rectangle.point
	p1 = copy.copy(p)
	p2 = copy.copy(p) 
	p3 = copy.copy(p)
	p1.pY += Rectangle.height
	p2.pX += Rectangle.width
	p2.pY += Rectangle.height
	p3.pX += Rectangle.width
	if not point_in_circle(Circle,p):
		print("矩形不在圆内")
		return False
	elif not point_in_circle(Circle,p1):
		print("矩形不在圆内")
		return False
	elif not point_in_circle(Circle,p2):
		print("矩形不在圆内")
		return False
	elif not point_in_circle(Circle,p3):
		print("矩形不在圆内")
		return False
	print("矩形在圆内")
	return True


def draw_rect(t,rect):
	"""使用turtle画rect"""
	turtle.setup(width=800,height=800, startx=100, starty=100)
	t.fd(rect.width)
	t.lt(90)
	t.fd(rect.height)
	t.lt(90)
	t.fd(rect.width)
	t.lt(90)
	t.fd(rect.height)
	turtle.mainloop()

if __name__ == '__main__':
	bob = turtle.Turtle()
	c = Circle(100,150,75)
	r= Rectangle(100,100,50,50)
	rect_in_circle(c,r)
	draw_rect(bob, r)