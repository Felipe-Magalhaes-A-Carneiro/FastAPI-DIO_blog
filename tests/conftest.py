import asyncio
import os

import pytest_asyncio
from httpx import ASGITransport, AsyncClient

os.environ.setdefault("DATABASE_URL", "sqlite:///tests.db")


@pytest_asyncio.fixture
async def db(request):
    from app.database import database, engine, metadata
    from models.post import posts  # ✅ sem 'src.'

    await database.connect()
    metadata.create_all(engine)

    def teardown():
        async def _teardown():
            await database.disconnect()
            metadata.drop_all(engine)

        asyncio.run(_teardown())

    request.addfinalizer(teardown)


@pytest_asyncio.fixture
async def client(db):
    from app.main import app  # ✅ sem 'src.'

    transport = ASGITransport(app=app)
    headers = {
        "Accept": "application/json",
        "Content-Type": "application/json",
    }

    async with AsyncClient(base_url="http://test", transport=transport, headers=headers) as client:
        yield client


async def access_token(client: AsyncClient):
    response = await client.post("/auth/login", json={"user_id": 1})
    return response.json()["access_token"]