#!/usr/bin/python
#_*_ encoding:utf-8_*_
"""
	设置logging，创建一个FileHandler，并对输出消息的格式进行设置，将其添加到logger，然后将日志写入到指定的文件中，
"""
import logging
from logging.handlers import RotatingFileHandler
logger = logging.getLogger(__name__)
logger.setLevel(level = logging.INFO)

#定义一个RotatingFileHandler，最多备份3个日志文件，每个日志文件最大1K
#日志输出到文件
rHandler = RotatingFileHandler("log.txt",maxBytes = 1*1024,backupCount = 3)
rHandler.setLevel(logging.INFO)

# handler = logging.FileHandler('log.txt')
# handler.setLevel(logging.INFO)
formatter = logging.Formatter('%(asctime)s - %(name)s - %(levelname)s - %(message)s')    #设置写入文件的格式
#日志输出到流，可以是sys.stderr，sys.stdout或者文件
# handler.setFormatter(formatter)
rHandler.setFormatter(formatter)
#logger中添加StreamHandler，可以将日志输出到屏幕上
console =  logging.StreamHandler()
console.setFormatter(formatter)
console.setLevel(logging.INFO)
#添加处理方式
# logger.addHandler(handler)
logger.addHandler(console)
logger.addHandler(rHandler)


logger.info("Start print log")
logger.debug("Do something")
logger.warning("Something maybe fail.")
logger.info("Finish")