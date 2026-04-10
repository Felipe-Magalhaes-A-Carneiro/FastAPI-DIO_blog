from datetime import datetime, UTC
from pydantic import BaseModel


# responsável pela detecção da saída:
class PostOut(BaseModel):
    title: str
    date: datetime