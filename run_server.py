from pycab_routes import Route as APP
from settings import HOST_DEBUG, HOST_NAME,HOST_PORT

APP.run(host=HOST_NAME,port=HOST_PORT,debug=HOST_DEBUG)