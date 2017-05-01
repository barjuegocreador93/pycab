'''
@autor Camilo Barbosa 

@ref github barjuegocreador93

'''

from bottle import template
from settings import ROOT,APP_NAME 

def viewroot(name):
	return ROOT+'/views/'+name+'.tpl'

def view(name,**variables):
	return template(viewroot(name),variables,APP_NAME=APP_NAME,template=viewroot)