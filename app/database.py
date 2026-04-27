import databases 
import sqlalchemy 

DATABASE_URL = 'sqlite:///./blog.db'

# cria database
database = databases.Database(DATABASE_URL)
# instanciando a classe SQLalchemmy
metadata = sqlalchemy.MetaData()
engine = sqlalchemy.create_engine(DATABASE_URL, connect_args = {"check_same_thread": False})