import sqlite3
import settings 

DB_ROOT=settings.DB_NAME

def qrys(*props,**vars):
	result={}
	
	for i in props:
		if i == 'vars-sql':
			result ['vars']='('
			
			for key,value in vars.iteritems():
				result ['vars']+=key + ','
				
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
	
	return result
	
	
class Model():

	def Migrations(self,**columns):
		table=sqlite3.connect(DB_ROOT)
		self.tablename=self.__class__.__name__
		data=qrys('init-sql',**columns)
		print ('creating a table '+self.tablename)
		print(data['init'])
		table.execute('CREATE TABLE '+self.tablename+' '+data['init']+';')
		table.commit()
				
	def Create (self,**columns):
		db=sqlite3.connect(DB_ROOT)
		data=qrys('vars-sql','values-sql',**columns)
		db.execute('INSERT INTO '+self.tablename+' '+data['vars']+' VALUES '+data ['values'])
		db.commit()
		
	def Where(self,**qry):
		db=sqlite3.connect(DB_NAME)
		c=db.cursor()
		data=qrys('vars-sql','e-and-sql',**qry)
		c.execute('SELECT '+data['vars']+' FROM '+self.tablename+' WHERE '+data['e-and'])
		return c.fletchall()


		 	
		