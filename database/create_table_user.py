from models.User import User
table=User().TableSchema()
User.Migrations(
    id=table.Integer().PrimaryKey().AutoIncrement().Column,
    name=table.String(255).NotEmpty().Column,
    email=table.String(255).NotEmpty().Unique().Column,
    password=table.String(255).NotEmpty().Column
)

