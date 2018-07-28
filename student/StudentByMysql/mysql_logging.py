#!/usr/bin/python
#_*_ encoding:utf-8_*_
"""
Datetime:2018-7-29 00:31
Author：叶强
Version:基于mysql的学生管理系统 v1.0
这个版本较上一个版本，预计添加logging模块
"""
import pymysql, time
import datetime
import logging


"""创建日志"""
logger = logging.getLogger(__name__)
logger.setLevel(level = logging.INFO)
handler = logging.FileHandler("stu_manage_log.txt")
handler.setLevel(logging.INFO)
formatter = logging.Formatter('%(asctime)s - %(name)s - %(levelname)s - %(message)s')
handler.setFormatter(formatter)
logger.addHandler(handler)


def connect_db():
	"""连接数据库"""
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
	logger.info(sql)
	try:
		cursor.execute(sql)
		con.commit()
	except:
		con.rollback()
		logger.exception("Insert operation error")
		raise 
	finally:
		cursor.close()
		con.close()


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



def search(sql):
	"""多出复用"""
	"""接收表名，获取表的所有信息，返回含有表内所有信息的元组对象"""
	logger.info(sql)
	con = connect_db()
	cur = con.cursor()
	try:
		cur.execute(sql)
		#查询时获取结果集中的所有行，一行构成一个元组，然后再将这些元组返回（即嵌套元组）
		content = cur.fetchall()
	except:
		logger.exception("Search operation error")
		raise 
	finally:
		cur.close()
		con.close()
	return content


def del_info(sql):
	"""删除信息"""
	logger.info(sql)
	con = connect_db()
	cur = con.cursor()
	try:
		cur.execute(sql)
		con.commit()
		print("delete success")
	except:
		logger.exception("Search operation error")
		print("delete error")
		raise 
	finally:
		cur.close()
		con.close()
	

def update(sql_update):
	"""更新学生信息"""
	logger.info(sql)
	con = connect_db()
	cur = con.cursor()
	try:
		cur.execute(sql_update)
		con.commit()
		print("update success")
	except:
		logger.exception("Search operation error")
		print("update failed")
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


def show_all_student():
	"""打印所有学生信息"""
	sql = "select * from student_"
	show_student(sql)
	logger.info("打印了所有学生信息")

def  menu_search_stu():
	"""学生查询界面"""
	print("+"*28)
	print("+{0:^20}+".format("学生查询界面"))
	print("+"*28)
	print("|{0:<21}|".format("1.按学号查询"))
	print("|{0:<21}|".format("2.按姓名查询"))
	print("|{0:<20}|".format("3.打印所有学生"))
	print("|{0:\u3000<14}|".format("4.退出查询页面"))
	print("+"*28)
	print("|{0:^21}|".format("功能待拓展"))
	print("+"*28)
	
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


def menu_manage_stu():
	"""管理界面的函数"""
	print("+"*28)
	print("+{0:^20}+".format("学生管理界面"))
	print("+"*28)
	print("|{0:<22}|".format("1.增加学生"))
	print("|{0:<22}|".format("2.删除学生"))
	print("|{0:<22}|".format("3.修改学生"))
	print("|{0:\u3000<14}|".format("4.退出学生管理界面"))
	print("+"*28)

def manage_student():
	"""管理学生 增、删、改"""
	flag = True
	while flag:
		menu_manage_stu()
		select = input("请输入你的选择：")
		if select == '1':
			insert2student()
		elif select == '2':
			show_all_student()
			sid_ = input("请输入要删除的学生的学号：")
			sql_ = 'DELETE FROM student_ WHERE sid = %s'%sid_
			del_info(sql_)
		elif select == '3':
			show_all_student()
			stu_id = input("请输入你想要修改的学生的学号:")
			sid = input("请输入学生的学号：")
			sname = input("请输入学生的姓名：")
			sage = input("请输入学生的年龄：")
			sgender = input("请输入学生的性别：")
			sphone = input("请输入学生的电话：")
			sql_update = "update student_ set sid = %s,sname = '"%(sid)+sname+"'"+",sage = %d, sgender = '"%(int(sage))+sgender+"'"+", sphone = %d where sid = %s"%(int(sphone),stu_id)
			update(sql_update)
		elif select == '4':
			print("管理结束，退出管理系统")
			flag = False
		else:
			print("请输入正确的选择！")
		print("操作结束，回车进入下一页面")
		fl = input()
		if fl == '\n':
			logger.info("执行了一次管理操作")





def  menu():
	"""用户可视窗口，即主菜单"""
	datetime_dt = datetime.datetime.today()  # 获取当前日期和时间
	datetime_str = datetime_dt.strftime("%Y-%m-%d %H:%M:%S")  # 格式化日期时间
	print("+++++++++++++++++++++++++++++++++++++++++++++++")
	print("+            学生管理系统2.0(mysql版本)       +") 
	print("+++++++++++++++++++++++++++++++++++++++++++++++")      
	print("+\t      1.管理学生                      +")
	print("+\t      2.查看学生                      +")		
	print("+\t      3.学生选课                      +")		
	print("+\t      4.学生选课情况                  +")
	print("+\t      5.查改课程                      +")
	print("+\t      6.打分程序                      +")
	print("+\t      7.查分                          +")
	print("+\t      8.退出系统                      +")
	print("+++++++++++++++++++++++++++++++++++++++++++++++") 
	print("+{0: ^45}+".format(datetime_str))
	print("+++++++++++++++++++++++++++++++++++++++++++++++") 

	      													 
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

