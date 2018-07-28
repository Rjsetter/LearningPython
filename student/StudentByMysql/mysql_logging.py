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
import logging, time
from Menu import *
from Db import *

"""创建日志"""
logger = logging.getLogger(__name__)
logger.setLevel(level = logging.INFO)
handler = logging.FileHandler("stu_manage_log.txt")
handler.setLevel(logging.INFO)
formatter = logging.Formatter('%(asctime)s - %(name)s - %(levelname)s - %(message)s')
handler.setFormatter(formatter)
logger.addHandler(handler)


def insert2student():
	"""插入数据库"""
	sid = input("请输入学生的学号：")
	sname = input("请输入学生的姓名：")
	sage = input("请输入学生的年龄：")
	sgender = input("请输入学生的性别：")
	sphone = input("请输入学生的电话：")
	sql = """insert into student_(sid,sname,sage,sgender,sphone)values
		('%s','%s','%d','%s','%d')"""%(sid, sname, int(sage),sgender,int(sphone))
	confirm =  input("确认添加吗？(yes/no):")
	if confirm == "yes":
		insert(sql)


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
	sid = input("请输入学生的学号：")
	sname = input("请输入学生的姓名：")
	sage = input("请输入学生的年龄：")
	sgender = input("请输入学生的性别：")
	sphone = input("请输入学生的电话：")
	sql_update = "update student_ set sid = %s,sname = '"%(sid)+sname+"'"+",sage = %d, sgender = '"%(int(sage))+sgender+"'"+", sphone = %d where sid = %s"%(int(sphone),stu_id)
	confirm =  input("确认修改吗？(yes/no):")
	confirm_ = check_valid(stu_id,1,Tuple)
	if confirm == "yes" and confirm_:
		update(sql_update)
	else:
		print("update failed")


def del_student():
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
	statu = ('开', '不开')    #用一个元组记录课程状态
	sql_course = "select * from course_"
	Tuple = search(sql_course)
	if Tuple:
		print("+++++++++++++++++++++++++++++")
		print("|课程号|  课程名   |课程状态|")
		print("+++++++++++++++++++++++++++++")
		for tuple_ in  Tuple:
			# print(tuple_)
			print("|{0:^6}| {1: <10}|{2:\u3000^4}|".format(tuple_[0],tuple_[1],statu[tuple_[2]]))
		print("+++++++++++++++++++++++++++++")
	else:
		print("++++++++++++++++++++++++++++")
		print("+      课程库里没有课程    +")
		print("++++++++++++++++++++++++++++")
	return Tuple


def add_course():
	"""插入课程"""
	cname = input("请输入课程名：")
	cstatu = input("请输入课程状态（0.开 1.不开）：")
	sql_addcourse = """insert into course_(cname, cstatus)values
		('%s','%d')"""%(cname,int(cstatu))
	confirm =  input("确认添加吗？(yes/no):")
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

												 
if __name__ == '__main__':
	Flag = True
	while Flag:
		menu()
		select = input("您想要进行什么操作？")
		if select == '1':
			manage_student()
		elif select == '2':
			search_student()
			# addCourse()

		elif select == '3':
			manage_course()

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


