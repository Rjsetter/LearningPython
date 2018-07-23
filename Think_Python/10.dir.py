#_*_ encoding:utf-8 _*_
import os

def walk(dirname):
	for name in os.listdir(dirname):
		path = os.path.join(dirname, name)

		if os.path.isfile(path):
			print(path)
		else:
			print("%s's child_dir:"%name)
			walk(path)
cwd = os.getcwd()
dir_ = '/home/python/Desktop/Git/LearnPython/LearningPython'
walk(dir_)