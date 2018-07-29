#!/usr/bin/python
#_*_ encoding:utf-8_*_
"""
日志管理模块
"""
import logging

"""创建日志"""
logger = logging.getLogger(__name__)
logger.setLevel(level = logging.INFO)
handler = logging.FileHandler("stu_manage_log.txt")
handler.setLevel(logging.INFO)
formatter = logging.Formatter('%(asctime)s - %(name)s - %(levelname)s - %(message)s')
handler.setFormatter(formatter)
logger.addHandler(handler)