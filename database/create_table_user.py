from models.User import *

def create_table():
    User.create_table(
        Column('name', String(255)),
        Column('email', String(255), unique=True),
        Column('password', String(255))
    )


def drop_table():
    User.Drop()
    pass