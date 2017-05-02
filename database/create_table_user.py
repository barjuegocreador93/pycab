from models.User import User
table=User().TableSchema()
User.Migrations(
    id=table.Integer().PrimaryKey().AutoIncrement().Column,
    name=table.String(255).NotEmpty().Column,
    email=table.String(255).NotEmpty().Unique().Column,
    password=table.String(255).NotEmpty().Column
)

User.Create(name='cab',email='cab331@hotmail.com',password='1234')
print User.Where(email='cab331@hotmail.com')