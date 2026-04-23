from contextlib import asynccontextmanager

import databases # importacao necessaria
from fastapi import FastAPI
import sqlalchemy # importacao necessaria
from controllers import post


DATABASE_URL = 'sqlite:///./blog.db'

# cria database
database = databases.Database(DATABASE_URL)
# instanciando a classe SQLalchemmy
metadata = sqlalchemy.MetaData()
engine = sqlalchemy.create_engine(DATABASE_URL, connect_args = {"check_same_thread": False})

@asynccontextmanager
async def lifespan(app: FastAPI):
    from models.post import posts # noqa

    await database.connect()
    # utiliza a engine:
    metadata.create_all(engine)
    yield
    await database.disconnect()

app = FastAPI(lifespan= None)
app.include_router(post.router)
