import sqlalchemy
from app.main import metadata

posts = sqlalchemy.Table(
    "posts",
    metadata,
    sqlalchemy.Column("id", sqlalchemy.Integer, primary_key= True),
    sqlalchemy.Column("title", sqlalchemy.String(150), null = False, unique = False),
    sqlalchemy.Column("content", sqlalchemy.String, nullable = False),
    sqlalchemy.Column("published_at", sqlalchemy.DateTime, nullable = True),
    sqlalchemy.Column("published", sqlalchemy.Boolean, default = False)

)