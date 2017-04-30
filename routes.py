from bottle import Bottle, static_file

import settings
APP=Bottle ()

from controllers.controller import home


'''  web routes '''


APP.route ('/')(home)




''' files-routes '''

def pub (filename):
	return static_file (filename, root=settings.ROOT+"/public")
	
APP.route ('/public/:filename')(pub)

def pub (filename,dirname):
	return static_file (filename, root=settings.ROOT+"/public/"+dirname)
	
APP.route ('/public/:dirname/:filename')(pub)

def pub (filename,dirname,framework):
	return static_file (filename, root=settings.ROOT+"/public/"+framework+"/"+dirname)
	
APP.route ('/public/:framework/:dirname/:filename')(pub)

def pub (filename,dirname,framework,required):
	return static_file (filename, root=settings.ROOT+"/public/"+required+"/"+framework+"/"+dirname)
	
APP.route ('/public/:required/:framework/:dirname/:filename')(pub)



if not settings.HOST_DEBUG :
	def error (rq):
		return "page not found!"
		
	APP.error (404)(error)