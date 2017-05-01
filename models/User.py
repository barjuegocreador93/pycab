from resources.model import Model
class User(Model):
	Columns=Model.Columns

	Columns['name']=str()
	Columns['email']=str()
	Columns['password']=str()
	pass