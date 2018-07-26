#_*_ encoding:utf-8_*_
import datetime
#为所有新的备注存储下一个可用的id
last_id = 0

class Note(object):
	"""创建notebook中的note，存储内容的memo和标签tag"""
	def __init__(self, memo, tags = ''):
		"""初始化notede内容memo,和标签tag，另外自动创建时间和一个唯一的id"""
		self.memo = memo
		self.tags = tags
		self.creation_date = datetime.date.today()
		global last_id
		last_id += 1
		self.id = last_id

	def match(self, filter):
		"""过滤查找，如果note中含有filter，返回True，否则返回False
		   查找方法对文本和标签是敏感的"""
		return filter in self.memo or filter in self.tags

class Notebook(object):
	"""定义一个笔记本集，可以被标记，修改和查询"""
	def __init__(self):
		"""创建一个没有note的笔记本，初始化为一个空列表"""
		self.notes = []

	def new_note(self, memo, tags=''):
		"""添加一个新的note，其中tags可以没有"""
		self.notes.append(Note(memo,tags))


	def _find_note(self, note_id):
		"""通过给定的note_id定位note"""
		for note in self.notes:
			if note.id == note_id:
				return note
			return None
	

	def modify_memo(self, note_id, memo):
		"""修改给定的note的id，改变相应的note的内容memo"""
		note = self._find_note(note_id)
		if note:
			note.memo = memo
			return True
		return False
		# for note in self.notes:
		# 	if note.id == note_id:
		# 		note.memo = memo
		# 		break    #修改完成后退出for循环！


	def modify_tags(self, note_id, tags):
		"""修改给定的note的id，改变相应的note的标签tags"""
		note = self._find_note(note_id)
		if note:
			note.tags = tags
			return True
		return False
		# for note in self.notes:
		# 	if note.id == note_id:
		# 		note.tags = tags
		# 		break

	def search(self, filter):
		"""通过给定的filter查询满足要求的所有note"""
		#通过列表生成器返回查询结果，使代码更简洁
		return [note for note in self.notes if note.match(filter)]















