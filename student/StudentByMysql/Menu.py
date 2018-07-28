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


def  menu():
	"""用户可视窗口，即主菜单"""
	datetime_dt = datetime.datetime.today()  # 获取当前日期和时间
	datetime_str = datetime_dt.strftime("%Y-%m-%d %H:%M:%S")  # 格式化日期时间
	print("+++++++++++++++++++++++++++++++++++++++++++++++")
	print("+            学生管理系统2.0(mysql版本)       +") 
	print("+++++++++++++++++++++++++++++++++++++++++++++++")      
	print("+\t      1.管理学生                      +")
	print("+\t      2.查看学生                      +")		
	print("+\t      3.课程管理                      +")		
	print("+\t      4.学生选课情况                  +")
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


if __name__ == '__main__':
	menu_manage_corse()