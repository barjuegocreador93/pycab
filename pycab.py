from settings import ROOT



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
    arg=raw_input ('$ ')
    arg=arg.replace (" ","")
    if arg == 'migrate':
    	migrations ()
    	
    elif arg == 'makemigration':
    	make_migration()
    	
    elif arg == 'makemodel':
    	make_models()
    	
    elif arg == 'help':
    	help()
    	
    elif arg == 'makeview':
    	make_view()
    	
    elif arg == 'makecontroller':
    	make_controller()
    	
    elif arg == 'runserver':
    	import main
    	
    else: print (arg+" it's not found")
    	