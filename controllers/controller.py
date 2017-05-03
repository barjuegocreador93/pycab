from resources.view import view
from resources.routes import request,response


def home():
	return view('home',title='Home',mylist=['jquery','bootstrap'])

