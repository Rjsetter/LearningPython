#!/usr/bin/python
#_*_ encoding:utf-8_*_
"""
Datetime:2018-7-29 00:31
Author：叶强
Version:基于mysql的学生管理系统 v1.0
这个版本较上一个版本，预计添加logging模块

#new#添加修改、删除校验函数 check_valid()
#new#将数据库的操作函数连接、增、删、改、查封装到新模块Db.py
"""
import time
from Menu import *
from Db import *
from logger import logger
import cProfile
import pstats

def insert2student(): 
	"""插入数据库"""
	"""返回一个sid值，用于插入user表中的外键"""
	sid = input("请输入学生的学号：")
	sname = input("请输入学生的姓名：")
	sage = input("请输入学生的年龄：")
	sgender = input("请输入学生的性别：")
	sphone = input("请输入学生的电话：")
	sql_insert = """insert into student_(sid,sname,sage,sgender,sphone)values
		('%s','%s','%d','%s','%d')"""%(sid, sname, int(sage),sgender,int(sphone))
	confirm =  input("确认插入吗？(yes/no):")
	if confirm == "yes":
		insert(sql_insert)
	return sid, confirm

def show_student(sql):
	"""打印学生库中的学生
	   返回一个包含所有学生信息的元组"""
	Tuple = search(sql)
	menu_show_stu(Tuple)
	return Tuple


def show_all_student():
	"""打印所有学生信息"""
	sql = "select * from student_"
	Tuple = show_student(sql)
	logger.info("打印了所有学生信息")
	return Tuple


def check_valid(id,index,turple_):
	"""用来验证更新时数据操作的正确性，
	id为用户输入要更新的索引，index为
	索引在表中的位置，turole_为返回的结果"""
	for t in turple_:
		if id == t[index]:
			return True
	return False


def search_student():
	"""按您选择的方式查询学生"""
	flag = True
	while flag:
		menu_search_stu()
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
			show_all_student()
		elif select == '4':
			print("查询结束，欢迎再次使用！")
			flag = False
		else:
			print("请输入正确的选择！")
		# 加入这个为了用户见面好看一点，一个页面结束要回车才会进入下一个页面
		# 添加了日志操作
		print("操作结束，回车进入下一页面")
		fl = input()
		if fl == '\n':
			logger.info("执行了一次查询操作")


def change_stu():
	"""修改学生"""
	Tuple = show_all_student()
	stu_id = input("请输入你想要修改的学生的学号:")
	sname = input("请输入学生的姓名：")
	sage = input("请输入学生的年龄：")
	sgender = input("请输入学生的性别：")
	sphone = input("请输入学生的电话：")
	sql_update = "update student_ set ,sname = '"+sname+"'"+",sage = %d, sgender = '"%(int(sage))+sgender+"'"+", sphone = %d where sid = %s"%(int(sphone),stu_id)
	confirm =  input("确认修改吗？(yes/no):")
	confirm_ = check_valid(stu_id,1,Tuple)       #验证输入的学号在库中
	if confirm == "yes" and confirm_:
		update(sql_update)
	else:
		print("update failed")


def del_student():
	"""删除学生"""
	Tuple = show_all_student()
	sid_ = input("请输入要删除的学生的学号：")
	sql_ = 'DELETE FROM student_ WHERE sid = %s'%sid_
	confirm_ = check_valid(sid_,1,Tuple)
	confirm =  input("确认删除吗？(yes/no):")
	if confirm == "yes" and confirm_:
		del_info(sql_)
	else:
		print("del failed")


def manage_student():
	"""管理学生 增、删、改"""
	flag = True
	while flag:
		menu_manage_stu()
		select = input("请输入你的选择：")
		if select == '1':
			insert2student()
		elif select == '2':
			del_student()
		elif select == '3':
			change_stu()
		elif select == '4':
			print("管理结束，退出管理系统")
			flag = False
		else:
			print("请输入正确的选择！")
		print("操作结束，回车进入下一页面")
		fl = input()
		if fl == '\n':
			logger.info("执行了一次学生管理操作")


def show_course():
	"""打印课程库里所有课程"""
	sql_course = "select * from course_"
	Tuple = search(sql_course)
	menu_show_close(Tuple)
	return Tuple


def add_course():
	"""插入课程"""
	cname = input("请输入课程名：")
	cstatu = input("请输入课程状态（0.开 1.不开）：")
	sql_addcourse = """insert into course_(cname, cstatus)values
		('%s','%d')"""%(cname,int(cstatu))
	confirm =  input("确认插入新课程吗？(yes/no):")
	if confirm == "yes":
		insert(sql_addcourse)
	else:
		print("add course failed")


def del_course():
	"""删除课程"""
	Tuple = show_course()
	cid_ = input("请输入要删除课程号：")
	sql_ = 'DELETE FROM course_ WHERE id = %d'%int(cid_)	
	confirm =  input("确认删除吗？(yes/no):")
	confirm_ = check_valid(cid_, 0, Tuple)
	if confirm == "yes" and confirm_:
		del_info(sql_)
	else:
		print("del course failed")


def change_course():
	"""修改"""
	Tuple = show_course()
	cid_ = input("请输入你想修改的课程号:")
	cname = input("请输入课程名：")
	cstatu = input("请输入课程的状态：")
	sql_update = "update course_ set cname = '"+cname+"'"+",cstatus = %d where id = %d"%( int(cstatu), int(cid_))
	confirm =  input("确认修改吗？(yes/no):")
	confirm_ = check_valid(cid_, 0, Tuple)
	if confirm == "yes" and confirm_:
		update(sql_update)
	else:
		print("update failed")


def manage_course():
	"""管理课程的增、删、改、查"""
	flag = True
	while flag:
		menu_manage_corse()
		select = input("请输入你的选择：")
		if select == '1':
			show_course()
		elif select == '2':
			add_course()
		elif select == '3':
			del_course()
		elif select == '4':
			change_course()
		elif select == '5':
			print("管理结束，退出管理系统")
			flag = False
		else:
			print("请输入正确的选择！")
		print("操作结束，回车进入下一页面")
		fl = input()
		if fl == '\n':
			logger.info("执行了一次课程管理操作")

def admin():
	"""管理员界面"""
	Flag = True
	while Flag:
		menu_admin()
		select = input("您想要进行什么操作？")
		if select == '1':
			manage_student()
		elif select == '2':
			search_student()
		elif select == '3':
			manage_course()
		elif select == '4':
			"""学生选课"""
			stu_select_course()
		elif select == '5':
			pass
			# checkCourse()
			# dealCourse()
		
		elif select == '6':
			"""给学生的课程打分"""
			pass
			# makeScore()
		elif select == '7':
			get_user()
		elif select == '8':
			Flag = False
			print("退出学生管理系统！")
		else:
			print("请输入正确的选择！")


def register():
	"""学生注册"""
	print("欢迎注册,请输入下列信息：")
	username = input("Username：")
	pwd = input("Password:")
	sid, confirm= insert2student()
	sql_register = """insert into user_(username, userpwd, stu_id)values
		('%s','%s','%s')"""%(username, pwd, sid)
	if confirm == "yes":
		insert(sql_register)
		print("注册成功，请牢记您的用户名和密码！")
	else:
		print("注册失败,即将回到主菜单！")


def show_stu_info(user):
	"""打印学生个人信息"""
	sql_show_stu = "SELECT student_.sid,student_.sname,student_.sgender,student_.sage, student_.sphone FROM student_,user_ WHERE user_.stu_id=student_.sid and user_.username = '"+user+"'"
	content = search(sql_show_stu)
	menu_per_info(content)
	return content


def change_stu_info(user):
	"""修改个人信息"""
	#请输入正确的学生学号，不然可能出现bug！
	content = show_stu_info(user)
	sid_ = content[0][0]   #获取学生学号，用以条件判断
	sname = input("请输入学生的姓名：")
	sage = input("请输入学生的年龄：")
	sgender = input("请输入学生的性别：")
	sphone = input("请输入学生的电话：")
	sql_update = "update student_ set sname = '"+sname+"'"+",sage = %d, sgender = '"%(int(sage))+sgender+"'"+", sphone = %d where sid = '"%(int(sphone))+sid_+"'"
	confirm =  input("确认修改吗？(yes/no):")
	if confirm == "yes":
		update(sql_update)
		print("您已修改您的个人信息")
	else:
		print("update failed")


def stu_info(user):
	"""操作学生个人信息"""
	logName = user
	Flag = True
	while Flag:
		menu_information()
		select = input("您想要进行什么操作？")
		if select == '1':
			show_stu_info(logName)
		elif select == '2':
			"""修改个人信息"""
			change_stu_info(logName)
		elif select == '3':
			"""退出学生页面"""
			Flag = False
			print("退出学生信息页面")
		else:
			print("请输入正确的选择，下面回到主菜单！")


def get_key(user, key):
	"""
	从user_和student表，获取输入的key的信息
	因为选课和查看选课会用到不一样的信息，所以才有了这个函数，
	这都是因为这个项目的功能是一项一项添加的，所以前期有些设
	计不合理。

	"""
	sql_find_key = "SELECT %s  FROM student_,user_ WHERE user_.stu_id=student_.sid and user_.username = '"%(key)+user+"'"     #开始位置反了，一直返回None
	item = searchOne(sql_find_key)
	# print(item)
	return item



def chose_class(user):
	"""学生进行选课"""
	show_course()   
	chose = input("你好，%s！请选择你想要上课的课程号"%user)
	stu_id = get_key(user, "student_.id")
	sql_insert_course = "insert into stu2course(sid, cid)values(%d,%d)"%(int(stu_id[0]),int(chose))
	insert(sql_insert_course)
	print("选课完成")


def show_chose_course(user):
	"""查看选课"""
	stu_id = get_key(user, "student_.sid")
	sql_ = """select student_.sname, student_.sage, student_.sgender, course_.cname, course_.cstatus from student_ inner join stu2course on student_.id=stu2course.sid and student_.sid = %s
		inner join course_ on course_.id=stu2course.cid
		 """%stu_id
	content = search(sql_)
	menu_show_selected_course(content)	

def Student(user):
	"""学生界面"""
	logName = user    #记录登陆的账户
	Flag = True
	while Flag:
		menu_stu()
		select = input("您想要进行什么操作？")
		if select == '1':
			'''个人信息'''
			stu_info(logName)
		elif select == '2':
			"""选课"""
			chose_class(logName)
		elif select == '3':
			"""查看选课"""
			show_chose_course(user)
		elif select == '4':
			"""学生选课"""
			pass
		elif select == '5':
			"""退出学生页面"""
			Flag = False
			print("退出学生管理系统！")
		else:
			print("请输入正确的选择，下面回到主菜单！")


def get_user():
	"""获取系统所有学生用户"""
	sql = 'select * from user_'
	Tuple = search(sql)
	menu_show_user(Tuple)


def check_student_login(user, pwd):
	"""验证学生登入"""
	Tuple = get_user()
	for tuple_ in Tuple:
		if user == tuple_[1] and pwd == tuple_[2]: #判断帐号密码是否正确
			return True
	return False


if __name__ == '__main__':
	Flag = True
	while Flag:
		menu()
		select = input("请输入您的选择：")
		if select == '1':
			logName, pwd =menu_login()   #login为登录函数，会返回用户输入的用户名和密码用于验证
			tag = check_student_login(logName, pwd)
			if tag:
				Student(logName)
				# cProfile.run("Student(logName)","prof.txt")
			else:
				print("用户名或者密码出错！下面回到主菜单")
		elif select == '2':
			logName, pwd = menu_login()
			if logName == "admin" and pwd == "root":
				admin()
			else:
				print("用户名或者密码出错！下面回到主菜单")
		elif select == '3':
			"""注册学生帐号"""
			register()
		elif select == '4':
			Flag =False
			print("感谢您使用我们的学生系统！欢迎再次使用～")
		else:
			print("请输入正确的选择！")
		# p = pstats.Stats("prof.txt")
		# p.sort_stats("time").print_stats()

