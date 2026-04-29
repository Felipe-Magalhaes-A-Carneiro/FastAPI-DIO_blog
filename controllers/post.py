from fastapi import status, APIRouter

from app.database import database
from schemas.post import PostIn, PostUpdateIn
from services.post import PostService # importação
from views.post import PostOut
from models.post import posts

router = APIRouter(prefix= "/posts")

service = PostService()

@router.get('/', response_model = list[PostOut])
async def read_posts(published: bool, limit: int, skip: int = 0, ):
    # criando a querry
    querry = posts.select()
    return await database.fetch_all(querry)

@router.post('/', status_code= status.HTTP_201_CREATED, response_model = PostOut)
async def create_post(post: PostIn):
    #atualizando criacao de posts
    command = posts.insert().values(title = post.title, content = post.content, published_at = post.published_at, published = post.published)

    last_id = await database.execute(command)
    return {**post.model_dump(), "id": last_id}

# serviço de leitura
@router.get("/{id}", response_model = PostOut)
async def read_post(id: int):
    return await service.read(id)

# serviço de alteração
@router.patch("/{id}", response_model= PostOut)
async def update_post(id: int, post: PostUpdateIn):
    return await service.update(id = id, post = post)
