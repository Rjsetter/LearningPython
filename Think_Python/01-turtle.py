#_*_ encoding:utf-8_*_


"""
fd的参数是移动的距离，以像素为单位
bk用于前进和后退
lt和rt用于左转和右转，它们的参数是旋转的角度，单位是度
"""
import turtle as  T
bob = T.Turtle()
bob.fd(100)
bob.lt(90)
bob.fd(100)
bob.pu()
bob.lt(90)
bob.fd(100)
bob.pd()
bob.lt(90)
bob.fd(100)
bob.bk(200)#负数是前进
bob.rt(90)
bob.bk(100)
T.mainloop()