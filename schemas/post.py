from datetime import datetime

from pydantic import BaseModel

# Responsável pela detecção da entrada
class PostIn(BaseModel):
    title: str
    content: str
    published_at: datetime | None = None
    published: bool = False