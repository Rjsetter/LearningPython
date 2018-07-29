#!/usr/bin/python
#_*_ encoding:utf-8_*_
import pymysql
from logger import logger     

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

def searchOne(sql):
	"""接受sql语句，查询满足条件语句的元组"""
	logger.info(sql)
	con = connect_db()
	cur = con.cursor()
	try:
		cur.execute(sql)
		#查询时获取结果集中的所有行，一行构成一个元组，然后再将这些元组返回（即嵌套元组）
		content = cur.fetchone()
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
	"""更新信息"""
	logger.info(sql_update)
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