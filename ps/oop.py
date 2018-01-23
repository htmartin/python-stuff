#!//usr/local/bin/python3

class Person(object):
	
	def __init__(self, name):
		self.name = name

	def say_hello(self):
		print ('Hello!', self.name)



p1 = Person("Scott")
p2 = p1
p2.name ='Alex'
p1.say_hello()

