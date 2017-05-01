from models.User import User
table=User()
User.Migrations(
    id=User.MigInteger(User.MigPrimaryKey()),
    name=User.MigString(255,User.MigUnique(),User.MigNotEmpty()),
    email=User.MigString(255,User.MigNotEmpty()),
    password=User.MigString(255,User.MigNotEmpty())
)
