#_*_ encoding:utf-8_*_
class Time(object):
	"""定义一天的时间"""
	def __init__(self,hour=0,minute=0,second=0):
		self.hour = hour
		self.minute = minute
		self.second = second

def time2int(time):
	"""时间转换为秒"""
	minutes = time.hour * 60 +time.minute
	seconds = minutes * 60 +time.second
	return seconds

def int2time(seconds):
	"""秒转换为时间"""
	time = Time()
	minutes, time.second = divmod(seconds,60)
	time.hour, time.minute = divmod(minutes, 60)
	return time

def valid_time(time):
	if time.hour < 0 or time.minute < 0 or time.second < 0:
		return False
	if time.minute > 60 or time.second > 60:
		return False
	return True

def mul_time(time_,num):
	"""时间乘积"""
	time = Time()
	assert valid_time(time_)
	seconds = time2int(time_) * num
	time = int2time(seconds)
	return time


def miles_per_second(time, distance):
	second = time2int(time)
	v = distance/second
	return v



if __name__ == '__main__':
	t = Time(8,45,13)
	t2 = mul_time(t,2)
	print("%d:%d:%d"%(t.hour,t.minute,t.second))
	print("%d:%d:%d"%(t2.hour,t2.minute,t2.second))
	t3 = Time(1,1,1)
	print(miles_per_second(t3,30000))


