'''
@autor Camilo Barbosa 

@ref github barjuegocreador93

'''

import sqlite3
import settings

version='0.1.4'

DB_ROOT=settings.DB_NAME

def qrys(*props,**vars):
	result={}
	
	for i in props:
		if i == 'vars-sql':
			result ['vars']='( '
			
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
				if len(vars.keys()) > 1: result['values'] = '( '
				else: result['values']=''
				for key, value in vars.iteritems():
					if not isinstance(i['columns-values-sql'][key],str):
						result['values'] +=str(value) + ' , '
					else:
						result['values'] +="'" + value + "' , "

				result['values'] = result['values'][:len(result['values']) - 2]
				if len(vars.keys()) > 1:result['values'] += ')'


			elif 'columns-key-values-sql' in i.keys():
				if len(vars.keys()) > 1: result['values'] = '( '
				else: result['values']=''
				for key, value in vars.iteritems():
					if not isinstance(i['columns-key-values-sql'][key], str):
						result['values'] +=key+' = '+ str(value) + ' , '
					else:
						result['values'] += key+" = '" + value + "' , "

				result['values'] = result['values'][:len(result['values']) - 2]
				if len(vars.keys()) > 1:result['values'] += ')'

			elif 'columns-e-and-sql' in i.keys():
				if len(vars.keys()) > 1: result['e-and'] = '( '
				else: result['e-and']=''
				for key, value in vars.iteritems():
					if not isinstance(i['columns-e-and-sql'][key], str):
						result['e-and'] += key + ' = ' + str(value) + ' & '
					else:
						result['e-and'] += key + " = '" + value + "' & "

				result['e-and'] = result['e-and'][:len(result['e-and']) - 2]
				if len(vars.keys()) > 1: result['e-and'] += ')'

	return result

class Table():
	Column=''

	@classmethod
	def String(cls,quat):
		cls.Column='varchar(' + str(quat) + ') '
		return cls


	@classmethod
	def Integer(cls):
		cls.Column='INTEGER '
		return cls

	@classmethod
	def Bool(cls):
		cls.Column='bool '
		return cls

	@classmethod
	def NotEmpty(cls):
		cls.Column += 'NOT NULL '
		return cls

	@classmethod
	def AutoIncrement(cls):
		cls.Column += "AUTOINCREMENT "
		return cls

	@classmethod
	def Unique(cls):
		cls.Column += 'unique '
		return cls

	@classmethod
	def PrimaryKey(cls):
		cls.Column += 'primary key '
		return cls



	
	
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
	def TableSchema():
		return Table()


	@classmethod
	def Create (cls,**columns):
		db=sqlite3.connect(DB_ROOT)
		cls.tablename=cls.__name__
		dd={}
		dd['columns-values-sql']=cls.Columns
		data=qrys('vars-sql',dd,**columns)
		db.execute('INSERT INTO '+cls.tablename+' '+data['vars']+' VALUES '+data ['values'])
		db.commit()

	@classmethod
	def Where(cls,**qry):
		db=sqlite3.connect(DB_ROOT)
		cls.tablename = cls.__name__
		c=db.cursor()
		dd={}
		dd['columns-e-and-sql'] = cls.Columns
		data=qrys(dd,**qry)
		qry=cls.Columns
		data2=qrys('vars-sql',**qry)
		print data2
		print data
		c.execute('SELECT '+data2['vars']+' FROM '+cls.tablename+' WHERE '+data['e-and'])
		resultA= c.fetchall()
		resultB=[]
		n=cls.Columns

		for i in resultA:
			new={}
			w=0
			for k in n.keys():
				new[k]=i[w]
				w+=1
			resultB.append(new)

		return resultB


	@classmethod
	def Update(cls,values=dict,**qry):
		db=sqlite3.connect(DB_ROOT)
		cls.tablename = cls.__name__
		dd={}
		dd['columns-key-values-sql']=cls.Columns
		mm={}
		mm['columns-e-and-sql']=cls.Columns
		data2 = qrys(mm, **qry)
		qry=values
		data1=qrys(dd,**qry)
		db.execute('UPDATE '+cls.tablename+' SET '+data1['values']+' WHERE '+data2['e-and'])
		db.commit()


