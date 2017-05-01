# pycab
Micro framework web App with python bottle

# install

1. requires

    1.1 python 2.7

    1.2 pip

2. run install.py

        $python install.py

3. run pycab-requires.py

        $python pycab-requires.py



# Usage

Make a great web page with this framework in easy way

to run a localhost:

    $python main.py

or

    $python pycab.py

    $ run server

# settings.py

in this file you can find all of basical configurations of a project

##### ROOT => Is the path of our project

##### HOST_NAME is the site url name. 'localhost'
  
##### HOST_PORT is the site url port. 8000

##### HOST_DEBUG is to know the problems of our site if it takes some else.

##### DB_NAME is the name of sqlite3 database




# controllers

Is a principal function of a route, it's used to intereact with 
our clients and interact with our site logic. 

Controller return a view.

1. ### locate:

        ROOT/controllers
    
2. ### Create controller template:

        $python pycab.py    
        $ make controller
        
3. ### Usage

        from resources.view import view
        
        def main():
            return vew('home',title='home')

# routes.py

Is the way to impement a exists controller 

Routes run a controllers functions using a http methods: GET, POST, PUT...

1. ### locate:

        ROOT
    
2. ### Create route:

        APP.route(nameofroute,method=method)(controller)
        
3. ### Usage

        from controllers import controller.main as home
        
        APP.route('/',method='GET')(home)

# views

# models

# migrationss






