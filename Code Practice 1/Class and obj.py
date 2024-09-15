class Car():
	def __init__(self,name,age):
		self.name=name
		self.age=age
	def statement(self):
		return '{} is {} years old'.format(self.name,self.age)

obj=Car("ABC",19)
obj.statement()
