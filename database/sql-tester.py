'''

Unsing to testing
'''

from models.User import User
from settings import DB_NAME

import sqlite3

User.Create(name='foo',email='da@jo.co',password='secret')
