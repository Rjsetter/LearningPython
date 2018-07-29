#_*_ encoding:utf-8_*_

# 较上版本预期添加的功能：
# 1.优化了一下显示窗口，下版本进行持久化功能的增加
#-------------分割线------------------


#定义count变量来记录添加学生的id,定义stu_list列表来存储学生
count = 1
stu_list = []
course = ['python', 'C++', 'ruby', 'java']

#定义一个基类Prson,存储基本的信息
class Person(object):
	def __init__(self, name="test", age = 100, gender = 'test', phone = 1111111111):
		self.__name = name
		self.__gender = gender
		self.__age = age
		self.__phone = phone

	@property
	def name(self):
		return self.__name
	
	@name.setter
	def name(self, name_):
		if name_ == "":
			raise IOError("请输入姓名哦")
		self.__name = name_
	@property	
	def gender(self):
		return self.__gender

	@gender.setter
	def gender(self, gender_):
		if gender_  == "":
			raise AttributeError("性别不要输入空值哦")
		self.__gender = gender_			

	@property
	def age(self):
		return self.__age

	@age.setter
	def age(self, age_):
		if not isinstance(age_, int):
			raise TypeError("年龄只能是整数哦～")
		self.__age = age_

	@property
	def phone(self):
		return self.__phone

	@phone.setter
	def phone(self, phone_):
		if len(str(phone_)) != 11 or not isinstance(phone_, int):
			raise AttributeError("电话号码只能是11位的整数") 
		self.__phone = phone_


class Course(object):
	"""定义课程类"""
	def __init__(self, score, cName):
		self.__cNama = cname     #课程名
		self.__score = score     #分数

	#课程名的getter和setter方法
	@property
	def cname(self):
		return self.__cNama
	
	@cname.setter
	def cname(self, cname_):
		self.cName = cname_
	

	# 获取score
	@property
	def score(self):
		return self.__score
    
	@score.setter
	def score(self, score_):
		if not isinstance(score_, int):
			raise ValueError('Score必须是int类型！')
		if score_ < 0 or score_ > 100:
			raise ValueError('Score值必须在0=<score<=100')
		self.__score = score_


class Student(Person, Course):
	"""定义学生类继承Person"""
	def __init__(self, id):
		self.sid = id

	def addStudent(self, name, gender, age, phone ):
		self.name = name
		self.gender = gender
		self.age = age
		self.phone = phone
		self.course = {} #该版本有列表改为字典，可以用来储存课程的成绩


def addCourse():
	"""给学生添加课程"""
	id = int(input("请输入你将要添加课程的学生的学号："))
	flag = True
	for stu in stu_list:
		if id == stu.sid:	
			flag = False
			for c in course:
				print(c)
			if course:
				print("目前课程库里有以上课程")
				chose = True
				while chose:
					print("请输入你想要添加的课程名")
					inC = input()
					stu.course[inC] = 0#设各科成绩初始为0
					p = input("是否继续选择课程？（Y/N）：")
					if p == 'Y' or p == 'y': #区分大小写
						pass
					else:
						chose = False
			else:
				print("目前课程库没有可以添加的课程！")
	if flag:
		print("学生库里没有此人！")


def checkCourse():
	"""查看课程库"""
	print("目前课程库里的课程如下：")
	for c in course:
		print("%d.%s"%((course.index(c)+1),c))


def dealCourse():
	"""操作课程库"""
	fg = True
	while fg:
		print("---------------------------")
		print("选择你想要进行的操作：")
		print("1.添加课程")
		print("2.删除课程")
		print("3.查看课程库")
		print("4.退出")
		select = input("输入你的选择：")
		print("---------------------------")
		if select == '1':
			course_ = input("请输入你要添加的课程名：")
			course.append(course_)
		elif select == '2':
			id = int(input("请输入你想要删除的课程号："))
			if id not in range(len(course)):
				print("请输入正确的选择！")
				continue
			del course[(id-1)]
		elif select == '3':
			checkCourse()
		elif select == '4':
			fg = False


def addStudent():
	"""添加学生"""
	global count
	p = Student(count)
	inName = input("请输入学生的姓名：")
	inGender = input("请输入学生的性别：")
	inAge = int(input("请输入学生的年龄:"))
	inPhone = int(input("请输入学生的电话（11位整型数）："))
	p.addStudent(inName, inGender, inAge, inPhone)
	stu_list.append(p)
	count +=1


def showStudent():
	"""打印学生信息"""
	if stu_list:
		print("学号\t姓名\t性别\t年龄\t电话")
		for stu in stu_list:
			print("%d\t%s\t%s\t%d\t%d"%(stu.sid, stu.name, stu.gender, stu.age, stu.phone))
	else:
		print("学生库里暂时没有学生！")


def showStu_Course():
	"""打印学生选课信息"""
	if stu_list:
		for stu in stu_list:
			print("学生ID\t姓名\t所选课程")
			if stu.course:
				print("%d\t%s"%(stu.sid,stu.name),end="\t")
				for key in stu.course.keys():
					print("%s"%key, end = " ")	
			else:
				print("%s还没有选课！"%stu.name)
	else:
		print("学生库里暂时没有学生！")		


def makeScore():
	"""给学生打分"""
	Fg = True
	while Fg:
		print("请输入你想要打分学生的学号：")
		id =int(input())
		t = 1
		for stu in stu_list:
			if stu.sid == id:
				t = 0
				if stu.course:
					for key in stu.course.keys():
						cj = int(input("请给课程%s打分："%key))
						stu.course[key] = cj  #给课程打分
					print("您已经给该生的所有课程打分！")
				else:
					print("该学生没有选择任何课程！")
		if t:
			print("该学生不在学生库中！")
		F = input("是否继续打分？Y/N：")
		if F == 'Y' or F == 'y':
		 	pass
		else:
			Fg = False


def showScore():
	"""分别打印学生的分数"""
	if stu_list:
		for stu in stu_list:
			print(stu.name)
			for key,value in stu.course.items():
				if value != 0:
					print("%s : %d"%(key,value))
				else:
					print("该生的%s没有打分"%key)
			if not stu.course :
				print("该生还没有选课！")
	else:
		print("学生库中没有该学生！")

def  menu():
	"""用户可视窗口，即主菜单"""
	print("------------------------------------------------")
	print("|            学生管理系统1.0                  |")       
	print("|\t1.添加学生                            |")
	print("|\t2.学生选课                            |")		
	print("|\t3.查看学生                            |")		
	print("|\t4.学生选课情况                        |")
	print("|\t5.查改课程                            |")
	print("|\t6.打分程序                            |")
	print("|\t7.查分                                |")
	print("|\t8.退出系统                            |")
	print("|\tAuthor：叶强	  	Version：1.0  |")
	print("-----------------------------------------------")

	      													 
if __name__ == '__main__':
	
	Flag = True
	while Flag:
		menu()
		select = input("您想要进行什么操作？")
		print("------------------------------")
		if select == '1':
			addStudent()

		elif select == '2':
			addCourse()

		elif select == '3':
			showStudent()

		elif select == '4':
			"""打印学生选课信息"""
			showStu_Course()
		elif select == '5':
			checkCourse()
			dealCourse()
		
		elif select == '6':
			"""给学生的课程打分"""
			makeScore()
		elif select == '7':
			showScore()

		elif select == '8':
			Flag = False
			print("谢谢您使用我们的学生系统！欢迎再次使用～")
		else:
			print("请输入正确的选择！")



	# s1 = Student(1)
	# s1.name = "小明"
	# s1.age = 18
	# s1.phone = 13371913706
	# s1.gender = "男"
	# s1.cName = "Python"
	# s1.score = 99
	# print(s1.name, s1.gender, s1.age, s1.phone, s1.cName, s1.score)
