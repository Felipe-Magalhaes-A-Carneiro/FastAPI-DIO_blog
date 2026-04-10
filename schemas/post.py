from datetime import datetime, UTC

from pydantic import BaseModel

# Responsável pela detecção da entrada
class PostIn(BaseModel):
    title: str
    date: datetime = datetime.now(UTC)
    published: bool = False