from datetime import datetime
from pydantic import BaseModel


# responsável pela detecção da saída:
class PostOut(BaseModel):
    id: int
    title: str
    content: str
    published_at: datetime | None