from datetime import datetime

from pydantic import BaseModel

# Responsável pela detecção da entrada
class PostIn(BaseModel):
    title: str
    content: str
    published_at: datetime | None = None
    published: bool = False

# Recebe e aceita os seguintes parâmetros para serem atualizados
class PostUpdateIn(BaseModel):
    title: str | None = None
    content: str | None = None
    published_at: datetime | None = None
    published: bool | None = None