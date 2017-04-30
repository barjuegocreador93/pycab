from models.User import User

table=User()
table.Migrations(id='INTEGER PRIMARY KEY',
name='CHARACTER(255) NOT NULL',
email='CHARACTER(255) NOT NULL UNIQUE',
password='CHARACTER(255) NOT NULL'
)