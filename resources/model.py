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
	qry=ops[0]
	for i in ops:
		qry+=' and '+i
	return qry
def Or(ops):
	qry = ops[0]
	for i in ops:
		qry += ' or ' + i
	return qry
class Model(object):
	@staticmethod
	def props():
		pass


	def __init__(self,**args):
		self.__class__.__dict__.update(**args)

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

		sera=select([t]).where(qry)
		print qry
		print qry.__dict__
		select_m = "SELECT * FROM '"+cls.__name__+"' WHERE "+(str(qry))+""
		return e.execute(sera)




	def Update(self):

		update=select([sql[0]]).set(**self.__class__.__dict__).where()
		sql[1].execute(update)
		pass


	@classmethod
	def Drop(cls):
		e=init_connection()
		m=MetaData()
		table=m.tables[cls.__name__]
		table.drop(e)
		pass

	@classmethod
	def create_table(cls,*args):
		e=init_connection()
		m=MetaData(e)
		print args
		t=Table(cls.__name__,m,*args)
		t.create(e)

