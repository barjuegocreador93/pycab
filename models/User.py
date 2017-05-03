from resources.model import *

class User(Model,Base):

	__tablename__='User'
	email=Column(String(255),unique=True)
	name=Column(String(255))
	password=Column(String(255))


create_model()
