#_*_ encoding:utf-8_*_

#打算建立一个学生教师管理系统
#1.0版本，无法储存，退出程序程序即失去信息
#2.0版本，或许可以用文件管理来储存学生和教师的信息
#3.0版本，用上数据库mysql或者sqlite3之类的数据库
#4.0版本，有可能的话用TK做一个图形界面
# ----------开始时间2018-7-19---------------

#定义一个基类Prson,存储基本的信息
class Person(object):
	def __init__(self, name="test", age = 100, gender = 'test', phone = 1111111111):
		self.__name = name
		self.__gender = age
		self.__age = gender
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

	def addStudent(self, name, gender, age, phone, ):
		self.name = name
		self.gender = gender
		self.age = age
		self.phone = phone
		self.cName = ""

def  menu():
	"""用户可视窗口，即主菜单"""
	print(
	"""
----------------------------------------------------
          学生管理系统1.0                     
1.添加学生										 
2.添加课程										 
3.查看学生 										 	
4.退出系统										 
	      													 
Author：叶强										 
Version：1.0							 		 	 
----------------------------------------------------	      
	      """)


#定义count变量来记录添加学生的id,定义stu_list列表来存储学生
count = 1
stu_list = []
course = ['python', 'C++', 'ruby', 'java']
if __name__ == '__main__':
	
	Flag = True
	while Flag:
		menu()
		select = int(input("您想要进行什么操作？"))
		if select == 1:
			p = Student(count)
			inName = input("请输入学生的姓名：")
			inGender = input("请输入学生的性别：")
			inAge = int(input("请输入学生的年龄:"))
			inPhone = int(input("请输入学生的电话（11位整型数）："))
			p.addStudent(inName, inGender, inAge, inPhone)
			stu_list.append(p)
			count +=1
			

		elif select == 2:
			id = int(input("请输入你将要添加课程的学生的学号："))
			flag = 1
			for stu in stu_list:
				if id == stu.sid:	
					flag = 0
					for c in course:
						print(c)
					if course:
						print("目前课程库里有以上课程，请输入你想要添加的课程名：")
						inC = input()
						stu.cName = inC
					else:
						print("目前课程库没有可以添加的课程！")
			if flag:
				print("学生库里没有此人！")

		elif select == 3:
			if stu_list:
				print("学号\t姓名\t性别\t年龄\t电话\t\t课程")
				for stu in stu_list:
					print("%d\t%s\t%s\t%d\t%d\t%s"%(stu.sid, stu.name, stu.gender, stu.age, stu.phone, stu.cName))
			else:
				print("学生库里暂时没有学生！")

		elif select == 4:
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
