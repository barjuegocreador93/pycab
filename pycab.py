from settings import ROOT

version='0.1.0'


def migrations():
	model=raw_input ('exist model name: ')
	__import__('database.create_table_'+model)
	
def make_migration():
	model=raw_input ('through model name: ')
	
	make='''from models.'''+model.capitalize()+' import '+model.capitalize()+'''\ntable='''+model.capitalize()+'''()\n'''+model.capitalize()+'''.Migrations(\nid='''+model.capitalize()+'''.MigInteger('''+model.capitalize()+'''.MigPrimaryKey())\n)\n'''
	a=open (ROOT +"/database/create_table_"+model+".py",'w')
	a.write(make)
	a.close()
	
def make_models():
	model=raw_input ('new model name: ')
	
	make='''from resources.model import Model\nclass '''+model.capitalize()+'''(Model):\n\tColumns=Model.Columns\n\tpass'''
	a=open (ROOT +"/models/"+model.capitalize() +".py",'w')
	a.write(make)
	a.close()
	
def make_view():
	view=raw_input('new view name: ')
	ar=open(ROOT +'/views/'+view+'.tpl','w')
	ar.write ("<p>make something great!!</p>")
	ar.close()
	
def make_controller ():
	cont=raw_input('new controller name: ')
	make='''from resources.view import view\nfrom bottle import request\nimport models\ndef main ():\n\treturn view("index",title="title")'''
	ar=open (ROOT +'/controllers/'+cont+'.py','w')
	ar.write(make)
	ar.close()


def help ():
	print ("---pycab---")
	print ("make model => to crate a model")
	print ("make migration => to crate a migration of model")
	print ("migrate => to generate a table in database through a model migration")
	print ("make view => to crate a view ")
	print ("make controller => to crate a controller ")









while True:
	m=raw_input ('$ ')
	arg=m.split(" ")

	if len(arg)==1:
		print(arg[0])
		if str(arg[0]) =='migrate':
			migrations()
	if len(arg)==2:

		if arg[0]=='make':
			if str(arg[1])=='migration': make_migration()
			elif str(arg[1])=='model': make_models()
			elif str(arg[1])=='view': make_view()
			elif str(arg[1])=='controller': make_controller()
		elif arg[0] =='run':
			if str(arg[1])== 'server':import main
			elif str(arg[1])=='requires': import pycabRequires
