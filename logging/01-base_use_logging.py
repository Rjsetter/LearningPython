#!/usr/bin/python
#_*_ encoding:utf-8_*_
"""
	logging模块的基本设置，然后在控制台输出日志
	__date__ 2018-7-28
"""
import logging
logging.basicConfig(level = logging.DEBUG,format = '%(asctime)s - %(name)s - %(levelname)s - %(message)s')
#建议不要使用logging，通过一下方式命名一个新的logging
logger = logging.getLogger(__name__)

logger.info("Start print log")
logger.debug("Do Something")
logger.warning("Something maybe fail.")
logger.info("Finish")