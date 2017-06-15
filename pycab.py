from settings import ROOT
from resources.roots import MODEL_ROOT,CONTROLLER_ROOT,VIEW_ROOT,DATABASE_ROOT
version='0.1.5.1'
from main import run_server
import pycabRequires


def migrations():
	model=raw_input ('exist model name: ')
	__import__('database.create_table_'+model)
	
def make_migration():
	model=raw_input ('through model name: ')
	make='''from models.'''+model.capitalize()+''' import *\ndef create_table():\n\t'''+model.capitalize()+'''.create_table( Column('name', String(255) ) )\n\ndef drop_table():\n\t'''+model.capitalize()+'''.Drop()\n'''
	a=open (DATABASE_ROOT+"create_table_"+model.lower()+".py",'w')
	a.write(make)
	a.close()
	
def make_models():
	model=raw_input ('new model name: ')
	
	make='''from resources.model import *\nclass '''+model.capitalize()+'''(Model):\n\tdef __init__(self,*args): \n\t\tsuper.__init__(args[0])\n\t\t'''
	a=open (MODEL_ROOT+model.capitalize() +".py",'w')
	a.write(make)
	a.close()
	
def make_view():
	view=raw_input('new view name: ')
	ar=open(VIEW_ROOT+view+'.tpl','w')
	ar.write ("<p>make something great!!</p>")
	ar.close()
	
def make_controller ():
	cont=raw_input('new controller name: ')
	make='''from resources.view import view\nfrom bottle import request\nimport models\ndef main ():\n\treturn view("index",title="title")'''
	ar=open (CONTROLLER_ROOT+cont+'.py','w')
	ar.write(make)
	ar.close()


def help ():
	print ("---pycab---")
	print ("make model => to crate a model.")
	print ("make migration => to crate a migration of model.")
	print ("migrate => to generate a table in database through a model migration.")
	print ("make view => to crate a view. ")
	print ("make controller => to crate a controller. ")
	print ("exit => exit")









while True:
	m=raw_input ('$ ')
	arg=m.split(" ")
	error=False
	if len(arg)==1:

		if str(arg[0]) =='migrate':
			migrations()
		elif arg[0] == 'help':
			help()
		elif arg[0] == 'exit':
			break
		elif arg[0] == 'install':
			import install
		else : error=True
	elif len(arg)==2:

		if arg[0]=='make':
			if str(arg[1])=='migration': make_migration()
			elif str(arg[1])=='model': make_models()
			elif str(arg[1])=='view': make_view()
			elif str(arg[1])=='controller': make_controller()
			else: error= True
		elif arg[0] =='run':
			if str(arg[1])== 'server': run_server()
			elif str(arg[1])=='requires':  pycabRequires.requires()
			else:error=True

	else: error=True

	if error: print('Command no exit please try to see the command help')
