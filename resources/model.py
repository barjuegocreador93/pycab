'''
@autor Camilo Barbosa 

@ref github barjuegocreador93

'''

import sqlite3
import settings

version='0.1.0'

DB_ROOT=settings.DB_NAME

def qrys(*props,**vars):
	result={}
	
	for i in props:
		if i == 'vars-sql':
			result ['vars']='('
			
			for key,value in vars.iteritems():
				result ['vars']+=key + ', '

			result['vars'] = result['vars'][:len(result['vars']) - 2]
			result['vars']+=')'
			
		elif i == 'init-sql':
		 	result ['init']='('
		 	for key,value in vars.iteritems():
		 		result ['init']+=key+' '+value + ' , '
		 	result['init']=result['init'][:len (result['init'])-2]
		 	result['init']+=')'
		 	
		elif i == 'values-sql':
			result ['vaules']='('
		 	for key,value in vars.iteritems():
		 		result ['values']+=key+' = '+value + ' , '
		 	
		 	result['values']=result['values'][:len (result['values'])-2]
		 	result['values']+=')'
		 
		elif i == 'e-and-sql':
			result ['e-and']+='('
			for key,value in vars.iteritems():
		 		result['e-and']+=key+' = '+value + ' & '
		 	result['e-and']=result['e-and'][:len (result['e-and'])-2]	
		 	result['e-and']+=')'

		elif isinstance(i,dict):
			if 'columns-values-sql' in i.keys():
				result['values'] = '('
				for key, value in vars.iteritems():
					if not isinstance(i['columns-values-sql'][key],str):
						result['values'] +=str(value) + ' , '
					else:
						result['values'] +="'" + value + "' , "

				result['values'] = result['values'][:len(result['values']) - 2]
				result['values'] += ')'

			elif 'columns-e-and-sql' in i.keys():
				result['e-and'] = '('
				for key, value in vars.iteritems():
					if not isinstance(i['columns-e-and-sql'][key], str):
						result['e-and'] += key + ' = ' + str(value) + ' & '
					else:
						result['e-and'] += key + " = '" + value + "' & "

				result['e-and'] = result['e-and'][:len(result['e-and']) - 2]
				result['e-and'] += ')'

	
	return result
	
	
class Model():

	Columns={}
	Columns['id']=int()
	tablename=''

	@classmethod
	def Migrations(cls,**columns):
		table=sqlite3.connect(DB_ROOT)
		cls.tablename= cls.__name__
		data=qrys('init-sql',**columns)
		table.execute('CREATE TABLE '+cls.tablename+' '+data['init']+';')
		table.commit()
		print ('creating a table ' + cls.tablename)
		print(data['init'])

	@staticmethod
	def MigString(quat,*args):
		return 'varchar('+str(quat)+') '+''.join(args)

	@staticmethod
	def MigNotEmpty():
		return 'NOT NULL '

	@staticmethod
	def MigInteger(*args):
		return 'int '.join(args)

	@staticmethod
	def MigPrimaryKey():
		return 'primary key '

	@staticmethod
	def MigUnique():
		return 'unique '


	@classmethod
	def Create (cls,**columns):
		db=sqlite3.connect(DB_ROOT)
		dd={}
		dd['columns-values-sql']=cls.Columns
		data=qrys('vars-sql',dd,**columns)
		db.execute('INSERT INTO '+cls.tablename+' '+data['vars']+' VALUES '+data ['values'])
		db.commit()

	@classmethod
	def Where(cls,**qry):
		db=sqlite3.connect(DB_ROOT)
		c=db.cursor()
		dd={}
		dd['columns-e-and-sql'] = cls.Columns
		data=qrys('vars-sql',dd,**qry)
		c.execute('SELECT '+'*'+' FROM '+cls.tablename+' WHERE '+data['e-and'])
		return c.fetchall()


