#!/usr/bin/python
#_*_ encoding:utf-8_*_
"""
	这个模块为mysql版本的学生管理系统提供菜单页面
	Authour: Rjsetter
"""
import datetime
datetime_dt = datetime.datetime.today()  # 获取当前日期和时间
datetime_str = datetime_dt.strftime("%Y-%m-%d %H:%M:%S")  # 格式化日期时间

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


def  menu_admin():
	"""用户可视窗口，即主菜单,管理员表"""
	datetime_dt = datetime.datetime.today()  # 获取当前日期和时间
	datetime_str = datetime_dt.strftime("%Y-%m-%d %H:%M:%S")  # 格式化日期时间
	print("+++++++++++++++++++++++++++++++++++++++++++++++")
	print("+            学生管理系统2.0(mysql版本)       +") 
	print("+++++++++++++++++++++++++++++++++++++++++++++++")      
	print("+\t      1.管理学生                      +")
	print("+\t      2.查看学生                      +")		
	print("+\t      3.课程管理                      +")		
	print("+\t      4.学生选课                      +")
	print("+\t      5.查改课程                      +")
	print("+\t      6.打分程序                      +")
	print("+\t      7.查看学生                      +")
	print("+\t      8.退出系统                      +")
	print("+++++++++++++++++++++++++++++++++++++++++++++++") 
	print("+{0: ^45}+".format(datetime_str))
	print("+++++++++++++++++++++++++++++++++++++++++++++++") 

def menu_manage_corse():
	"""管理课程界面"""
	print("+"*28)
	print("+{0:^20}+".format("课程管理界面"))
	print("+"*28)
	print("|{0:<22}|".format("1.查看课程"))
	print("|{0:<22}|".format("2.添加课程"))
	print("|{0:<22}|".format("3.删除课程"))
	print("|{0:<22}|".format("4.修改课程"))
	print("|{0:\u3000<14}|".format("5.退出课程管理界面"))
	print("+"*28)


def menu():
	"""学生管理系统主菜单"""
	datetime_dt = datetime.datetime.today()  # 获取当前日期和时间
	datetime_str = datetime_dt.strftime("%Y-%m-%d %H:%M:%S")  # 格式化日期时间
	print("++++++++++++++++++++++++++++++++++++++++")
	print("+        欢迎使用学生管理系统3.0       +") 
	print("++++++++++++++++++++++++++++++++++++++++")      
	print("+\t      1.学生登入               +")
	print("+\t      2.管理员登入             +")		
	print("+\t      3.学生注册               +")
	print("+\t      4.退出系统               +")			
	print("++++++++++++++++++++++++++++++++++++++++") 
	print("+{0: ^38}+".format(datetime_str))
	print("++++++++++++++++++++++++++++++++++++++++") 


def menu_stu():
	"""学生主菜单"""
	print("########################################")
	print("#              学生页面                #") 
	print("########################################")      
	print("#\t      1.个人信息               #")
	print("#\t      2.选    课               #")		
	print("#\t      3.查看选课               #")
	print("#\t      4.查看成绩               #")			
	print("#\t      5.退出系统               #")			
	print("########################################") 
	print("#{0: ^38}#".format(datetime_str))
	print("########################################") 


def menu_information():
	"""学生个人信息页面"""
	print("########################################")
	print("#        学生个人信息页面              #") 
	print("########################################")      
	print("#         1.查看个人信息               #")	
	print("#         2.修改个人信息               #")	
	print("#         3.退出系统                   #")			
	print("########################################") 
	print("#{0: ^38}#".format(datetime_str))
	print("########################################") 

def menu_login():
	"""登录页面"""
	print("+"*28)
	print("+{0:\u3000^13}+".format("登陆页面"))
	print("+"*28)
	username = input("Username：")
	pwd = input("Password：")
	print("")
	return username,pwd


def menu_per_info(content):
	"""打印个人信息"""
	print('\n\n########################################')
	print("#          个人信息如下                #")
	print('########################################')
	print("#学号：{0:\u3000<38}".format(content[0][0]))
	print("#姓名：{0:\u3000<38}".format(content[0][1]))
	print("#性别：{0:\u3000<38}".format(content[0][2]))
	print("#年龄：{0:\u3000<38}".format(content[0][3]))
	print("#电话：{0:\u3000<38}".format(content[0][4]))
	print('########################################')
	print('\n\n')

def menu_show_close(Tuple):
	"""打印课程信息"""
	if Tuple:
		statu = ('开', '不开')    #用一个元组记录课程状态
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


def menu_show_stu(Tuple):
	"""打印学生信息"""
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


def menu_show_selected_course(Tuple):
	"""打印个人所选的课"""
	if Tuple:
		statu = ('开', '不开')    #用一个元组记录课程状态
		print("选课情况如下：")
		print("+++++++++++++++++++++")
		print("|  课程名  |课程状态|")
		print("+++++++++++++++++++++")
		for tuple_ in  Tuple:
			# print(tuple_)
			print("|{0: <10}|{1:\u3000^4}|".format(tuple_[3],statu[tuple_[4]]))
		print("+++++++++++++++++++++")
	else:
		print("++++++++++++++++++++++++")
		print("+      您还没有选课    +")
		print("++++++++++++++++++++++++")


def menu_show_user(Tuple):
	"""打印注册的学生"""
	count = 0
	if Tuple:
		print("注册学生情况如下：")
		print("++++++++++++++++++++++++++++")
		print("|编号|   姓名   |   密码   |")
		print("++++++++++++++++++++++++++++")
		for tuple_ in  Tuple:
			count += 1
			# print(tuple_)
			print("|{0:^4}|{1:<10}|{2:<10}|".format(count,tuple_[1],tuple_[2]))
		print("++++++++++++++++++++++++++++")
	else:
		print("++++++++++++++++++++++++++++")
		print("+     目前还没有学生注册    +")
		print("++++++++++++++++++++++++++++")
		print("这个功能没有测试，或许输出表格会有点问题！")


if __name__ == '__main__':
	# menu_manage_corse()
	# login()
	# menu_stu()
	# menu()
	information()