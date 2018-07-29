#!/usr/bin/python
#_*_ encoding:utf-8_*_
"""
	这个模块为mysql版本的学生管理系统提供菜单页面
	Authour: Rjsetter
"""
import datetime


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
	print("+\t      7.查分                          +")
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
	datetime_dt = datetime.datetime.today()  # 获取当前日期和时间
	datetime_str = datetime_dt.strftime("%Y-%m-%d %H:%M:%S")  # 格式化日期时间
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

def login():
	print("+"*28)
	print("+{0:\u3000^13}+".format("登陆页面"))
	print("+"*28)
	username = input("Username：")
	pwd = input("Password：")
	print("")
	return username,pwd

if __name__ == '__main__':
	# menu_manage_corse()
	# login()
	# menu_stu()
	menu()