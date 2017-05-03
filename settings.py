import os

APP_NAME="PyCab"

ROOT= os.path.dirname(os.path.abspath(__file__) )

DATABASE={
    'engine':'sqlite3',
    'path':''
}

HOST_NAME='localhost'
HOST_PORT= 8000
HOST_DEBUG=True