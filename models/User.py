from resources.model import *

class User(Model):

	def __init__(self,*arg):
		super.__init__(arg[0])

		self.name=str(arg[1])
		self.email=str(arg[2])
		self.password=str(arg[3])


	def __str__(self):
		return "Nombre: {} \nEmail: {}".format(self.name,self.email)

	pass
