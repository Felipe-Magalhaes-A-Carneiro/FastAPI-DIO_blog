import asyncio
import os

import pytest_asyncio
from httpx import ASGITransport, AsyncClient

os.environ.setdefault("DATABASE_URL", f"sqlite:///tests.db")


# Primeira função - Retorna o banco de dados
@pytest_asyncio.fixture
async def db(request):
    from src.app.database import database, engine, metadata
    from src.models.post import posts

    await database.connect()
    metadata.create_all(engine)

    def teardown():
        async def _teardown():
            await database.disconnect()
            metadata.drop_all(engine)

        asyncio.run(_teardown())

    request.addfinalizer(teardown)


# Segunda função - Retorna o http client
@pytest_asyncio.fixture
async def client(db):
    from src.app.main import app

    transport = ASGITransport(app = app)
    headers = {
        "Accept": "application/json",
        "Content-Type": "application/json",
    }

    async with AsyncClient(base_url = "http://test", transport= transport, headers= headers) as client:
        yield client



# Terceira função - Facilita o access_token
async def access_token(client: AsyncClient):
    response = await client.post("/auth/login", json={"user_id": 1})
    return response.json()["access_token"]