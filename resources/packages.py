'''
@autor Camilo Barbosa 

@ref github barjuegocreador93

'''

import os,sys,os.path
import pip


def pathexist(path):
	return os.path.exists(path)
	

		
def modcmd(*arg):
	pip.main([arg[0],arg[1]])

		
def pipinstall(module):
	modcmd('install',module)
	return True

	