from sqlalchemy import *
from settings import DATABASE

def init_connection():
	if 'engine' in DATABASE.keys():
		if DATABASE['engine']=='sqlite3' and 'path' in DATABASE.keys():
			return create_engine('sqlite://'+DATABASE['path'])


	return object()

from sqlalchemy.ext.declarative import declarative_base

Base = declarative_base()
def typer(data):
	if isinstance(data,str):
		return "'"+(data)+"'"
	return str(data)

def Equals(key,data):
	return " {} = {}".format(key,typer(data))

def Max(key,data):
	return " {} > {} ".format(key,typer(data))

def Min(key,data):
	return " {} < {} " .format (key, typer(data))

def MinE(key,data):
	return " {} <= {} ".format(key, typer(data))

def MaxE(key,data):
	return " {} >= {} ".format(key, typer(data))

def And(*ops):
	qry=""
	for i in ops:
		qry+=' and '+i
	return qry
def Or(ops):
	qry = ""
	for i in ops:
		qry += ' or ' + i
	return qry


class Model(object):
	@staticmethod
	def props():
		pass





	def __init__(self,*arg):
		self.id=int(arg[0])

	@classmethod
	def Create(cls,**args):
		e=init_connection()
		m=MetaData(reflect=True,bind=e)
		table=m.tables[cls.__name__]
		ins=table.insert().values(**args)
		e.execute(ins)


	@classmethod
	def Columns(cls):
		e = init_connection()
		m = MetaData(e, reflect=True)
		return  m.tables[cls.__name__].c

	@classmethod
	def Where(cls, qry):
		e = init_connection()
		m = MetaData(bind=e, reflect=True)
		t=m.tables[cls.__name__]

		#sera=select([t]).where(qry)

		select_m = "SELECT * FROM '"+cls.__name__+"' WHERE "+(str(qry))+""
		return [(cls(*i))for i in e.execute(select_m)]




	def Update(self):

		#update=select([sql[0]]).set(**self.__class__.__dict__).where()
		e = init_connection()
		m = MetaData(e, reflect=True)
		set=''
		i=0
		for k,v in self.__dict__.iteritems():
			if k != 'id' and isinstance(k,str):
				data=''
				if not isinstance(v,str):
					data+= " {} = {} ".format(k,str(v))
				else:
					data+= " {} = '{}' ".format(k, v)
				if i>0 :
					data=' , '+data
				set+=data
				i+=1

		update = "UPDATE '" + self.__class__.__name__ + "' SET " + set + " WHERE id = "+str(self.id)
		e.execute(update)
		pass




	@classmethod
	def Drop(cls):
		e=init_connection()
		m=MetaData(bind=e,reflect=True)
		table=m.tables[cls.__name__]
		table.drop(e)
		pass

	@classmethod
	def create_table(cls,*args):
		e=init_connection()
		m=MetaData(e)
		print args
		t=Table(cls.__name__,m,Column('id', Integer, primary_key=True, autoincrement=True),*args)
		t.create(e)


	@classmethod
	def Create_Migration(cls):
		pass


	#relational methods

	def addOne(self,item,fkey="defaultfk",ToOne=False):

		if isinstance(item,Model) and isinstance(fkey,str):

			if self.__dict__.has_key(fkey):
				self.__dict__.__setitem__(fkey,item.id)
				self.Update()

			else:
				fkey=item.__class__.__name__+"_id"
				if self.__dict__.has_key(fkey):
					self.__dict__.__setitem__(fkey, item.id)
					self.Update()

			if ToOne : item.addOne(self)

	def GetOne(self,typemodel,fkey="defaultfk"):

		if isinstance(typemodel,Model):
			if self.__dict__.has_key(fkey):
				return typemodel.Where(Equals("id",self.__dict__.__getitem__(fkey)))[0]
			else:
				fkey = typemodel.__class__.__name__ + "_id"
				if self.__dict__.has_key(fkey):
					return typemodel.Where(Equals("id", self.__dict__.__getitem__(fkey)))[0]
		return 0




		





