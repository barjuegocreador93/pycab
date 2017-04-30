from settings import ROOT



def migrations():
	model=raw_input ('model: ')
	__import__('database.create_table_'+model)
	
def make_migration():
	model=raw_input ('model: ')
	
	make='''from models.'''+model.capitalize()+' import '+model.capitalize()+'''\ntable='''+model.capitalize()+'''()\ntable.Migrations(\nid="INTEGER PRIMARY KEY"\n)\n'''
	a=open (ROOT +"/database/create_table_"+model+".py",'w')
	a.write(make)
	a.close()
	
def make_models():
	model=raw_input ('model: ')
	
	make='''from resources.model import Model\nclass '''+model.capitalize()+'''(Model)\n\tpass'''
	a=open (ROOT +"/models/"+model.capitalize() +".py",'w')
	a.write(make)
	a.close()
	
def make_view():
	view=raw_input('view name: ')
	ar=open(ROOT +'/views/'+view+'.tpl','w')
	ar.write ("<p>make something great!!</p>")
	ar.close()

def help ():
	print ("---pycab---")
	print ("make model => to crate a model")
	print ("make migration => to crate a migration of model")
	print ("migrate => to generate a table in database through a model migration")
	print ("make view => to crate a view ")
	
	

while True:
    arg=raw_input ('$ ')
    if arg == 'migrate':
    	migrations ()
    	
    elif arg == 'make migration':
    	make_migration()
    	
    elif arg == 'make model':
    	make_models()
    	
    elif arg == 'help':
    	help()
    	
    elif arg == 'make view':
    	make_view()
    	
    else: print (arg+" it's not found")
    	