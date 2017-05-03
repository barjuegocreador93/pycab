from sqlalchemy import *
from settings import DATABASE

def init_connection():
	if 'engine' in DATABASE.keys():
		if DATABASE['engine']=='sqlite3' and 'path' in DATABASE.keys():
			return create_engine('sqlite://'+DATABASE['path'])
	return object()

from sqlalchemy.ext.declarative import declarative_base

Base = declarative_base()

class Model(object):
	__tablename__=''
	id=Column(Integer,primary_key=True,autoincrement=True)

	def Create(self,**args):
		self.__class__.__dict__.update(**args)
		e=init_connection()
		table=Table(self.__tablename__)
		ins=table.insert().values(**args)
		e.execute(ins)

	@property
	def Columns(self):
		e = init_connection()
		meta = MetaData(e, reflect=True)
		return  meta.tables[self.__tablename__].c

	def Where(self,qry):
		e=init_connection()
		meta=MetaData(e,reflect=True)
		table = meta.tables[self.__tablename__]
		select_m = select([self.__tablename__]).where(qry)
		return e.execute(select_m)






def create_model():
	e=init_connection()
	Base.metadata.create_all(bind=e)
