#!/usr/bin/python
#_*_ encoding:utf-8_*_
import pymysql, time


def connect_db():
	return pymysql.connect(host="127.0.0.1",
	                       port = 3306,
	                       user = "root",
	                       password = "mysql",
	                       database = "Python"
	                       )

def insert(sql):
	"""插入操作"""
	con = connect_db()
	cursor = con.cursor()

	try:
		cursor.execute(sql)
		con.commit()
	except:
		con.rollback()
		# logging.exception("Insert operation error")
		raise 
	finally:
		cursor.close()
		con.close()


def insert2student():
	Id = 'null'
	sid = input("请输入学生的学号：")
	sname = input("请输入学生的姓名：")
	sage = input("请输入学生的年龄：")
	sgender = input("请输入学生的性别：")
	sphone = input("请输入学生的电话：")
	sql = """insert into student_(sid,sname,sage,sgender,sphone)values
		('%s','%s','%d','%s','%d')"""%(sid, sname, int(sage),sgender,int(sphone))
	insert(sql)


def search(sql):
	"""多出复用"""
	"""接收表名，获取表的所有信息，返回含有表内所有信息的元组对象"""
	con = connect_db()
	cur = con.cursor()
	try:
		cur.execute(sql)
		#查询时获取结果集中的所有行，一行构成一个元组，然后再将这些元组返回（即嵌套元组）
		content = cur.fetchall()
	except:
		#logging.exception("Search operation error")
		raise 
	finally:
		cur.close()
		con.close()
	return content


def del_info(sql):
	"""删除信息"""
	con = connect_db()
	cur = con.cursor()
	try:
		cur.execute(sql)
		con.commit()
		print("delete success")
	except:
		#logging.exception("Search operation error")
		print("delete error")
		raise 
	finally:
		cur.close()
		con.close()
	


def show_student(sql):
	#返回的是一个嵌套元组
	
	Tuple = search(sql)
	if Tuple:
		print("+++++++++++++++++++++++++++++++++++++++++++++++++")
		print("|   学号    |  姓名   | 年龄| 性别 |  电话      |")
		print("+++++++++++++++++++++++++++++++++++++++++++++++++")
		for tuple_ in  Tuple:
			# print(tuple_)
			print("|{0:^11}| {1:\u3000<4}| {2:^4}| {3:^4}| {4:^11}|".format(tuple_[1],tuple_[2],tuple_[3],tuple_[4],tuple_[5]))
		print("+++++++++++++++++++++++++++++++++++++++++++++++++")
	else:
		print("目前学生库里没有学生")


def search_student():
	"""按您选择的方式查询学生"""
	flag = True
	while flag:
		print("-"*20)
		print("您想如何查询？")
		print("1.学号")
		print("2.姓名")
		print("3.打印所有学生信息")
		print("4.退出")
		print("*****功能待添加*****")
		print("-"*40)
		select = input("请输入想查询的方式：")
		if select == '1':
			num = input("请输入要查询学号：")
			sql = "select * from student_ where sid = %s"%num
			show_student(sql)
		elif select == '2':
			name = str(input("请输入要查询名字："))
			sql = "select * from student_ where sname = '"+name+"'"
			show_student(sql)
		elif select == '3':
			sql = "select * from student_"
			show_student(sql)
		elif select == '4':
			print("查询结束，欢迎再次使用！")
			flag = False
		else:
			print("请输入正确的选择！")
		# 加入这个为了用户见面好看一点，一个页面结束要回车才会进入下一个页面
		print("操作结束，回车进入下一页面")
		fl = input()
		if fl == '\n':
			pass



	

def manage_student():
	"""管理学生 增、删、改"""
	flag = True
	while flag:
		print("+"*20)
		print("学生管理界面")
		print("1.增加学生")
		print("2.删除学生")
		print("3.修改学生")
		print("退出学生管理界面")
		print("+"*20)
		select = input("请输入你的选择：")
		if select == '1':
			insert2student()
		elif select == '2':
			sql = "select * from student_"
			show_student(sql)
			sid_ = input("请输入要删除的学生的学号：")
			sql_ = 'DELETE FROM student_ WHERE sid = %s'%sid_
			del_info(sql_)
		elif select == '3':
			pass
		elif select == '4':
			print("管理结束，退出管理系统")
			flag = False
		else:
			print("请输入正确的选择！")
		print("+"*20)
		print("操作结束，回车进入下一页面")
		print("+"*20)
		fl = input()
		if fl == '\n':
			pass





def  menu():
	"""用户可视窗口，即主菜单"""
	print("------------------------------------------------")
	print("|            学生管理系统1.0                  |")       
	print("|\t1.管理学生                            |")
	print("|\t2.查看学生                            |")		
	print("|\t3.学生选课                            |")		
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
			manage_student()
		elif select == '2':
			search_student()
			# addCourse()

		elif select == '3':
			pass

		elif select == '4':
			"""打印学生选课信息"""
			pass
			# showStu_Course()
		elif select == '5':
			pass
			# checkCourse()
			# dealCourse()
		
		elif select == '6':
			"""给学生的课程打分"""
			pass
			# makeScore()
		elif select == '7':
			pass
			# showScore()

		elif select == '8':
			Flag = False
			print("谢谢您使用我们的学生系统！欢迎再次使用～")
		else:
			print("请输入正确的选择！")

