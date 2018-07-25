#_*_ encoding:utf-8_*_

class Kangaroo:
    """A Kangaroo is a marsupial."""
    
    def __init__(self, name, contents=[]):
        """Initialize the pouch contents.

        name: string
        contents: initial pouch contents.
        """
        self.name = name
        self.pouch_contents = contents

    def __str__(self):
        """Return a string representaion of this Kangaroo.
        """
        t = [ self.name + ' has pouch contents:' ]
        for obj in self.pouch_contents:
            s = '    ' + object.__str__(obj)
            t.append(s)
        return '\n'.join(t)

    def put_in_pouch(self, item):
        """Adds a new item to the pouch contents.

        item: object to be added
        """
        self.pouch_contents.append(item)


kanga = Kangaroo('Kanga')
roo = Kangaroo('Roo')
kanga.put_in_pouch('wallet')
kanga.put_in_pouch('car keys')
kanga.put_in_pouch([1,2,3,4])
kanga.put_in_pouch(roo)

print(kanga)
print(roo)


# class Kangroo(object):
# 	def __init__(self, content = []):
# 		self.pouch_contents = content

# 	def put_in_pouch(self, *args, **kwargs):
# 		for x in args:
# 			self.pouch_contents.append(x)

# 		for y in kwargs:
# 			self.pouch_contents.append(y)

# 	def __str__(self):
# 		str_ = ''
# 		for x in self.pouch_contents:
# 			str_ =str_ + x
# 		return str_


# p = Kangroo()
# p.put_in_pouch('kanga','roo','[1,2,3,4]')
# print(p)