from database.create_table_user import *



data= User.Where(User.Columns().id == 4)

for i in data:
    print i