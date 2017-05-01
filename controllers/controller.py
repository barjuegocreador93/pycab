from resources.view import view
from bottle import response,request


def home():
	return view('home',title='Home')

