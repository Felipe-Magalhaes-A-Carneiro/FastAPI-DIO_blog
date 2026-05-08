from contextlib import asynccontextmanager

from fastapi import FastAPI
from src.controllers import post
from src.app.database import database, engine, metadata
from src.controllers import auth


@asynccontextmanager
async def lifespan(app: FastAPI):
    from src.models.post import posts # noqa

    await database.connect()
    # utiliza a engine:
    metadata.create_all(engine)
    yield
    await database.disconnect()

app = FastAPI(lifespan= lifespan)
app.include_router(auth.router)
app.include_router(post.router)
