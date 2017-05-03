# pycab
## v.0.1.5 | dev
Micro framework web App with python bottle

# install

1. requires

    1.1 python 2.7

    1.2 pip

2. run install.py

        $python install.py

3. run pycabRequires.py

        $python pycab.py
        $ run requires



# Usage

Make a great web page with this framework in easy way

to run a localhost:

    $python run_server.py

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
```python

from resources.view import view
     
def main():
    return view('home',title='home')
```

# routes.py

Is the way to impement a exists controller 

Routes run a controllers functions using a http methods: GET, POST, PUT...

1. ### locate:

        ROOT/routes/web.py
    
2. ### Create route:

        Route.get(nameofroute)(controller)
        
        
        
3. ### Usage
 ```python
    
  from resources.routes import Route
  from controllers.controller import home
           
  Route.get('/')(home)
  ```
  
  dynamic routing
 ```python
   
  from resources.routes import Route
    
  Route.get('/<id :int>')()
  
  Route.get('/<ids :list>')()
 ```
  


# views

# models

# migrationss






