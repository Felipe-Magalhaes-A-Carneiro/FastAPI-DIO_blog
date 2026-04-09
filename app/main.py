from fastapi import Response, Cookie, Header, FastAPI, status
from typing import Annotated
from pydantic import BaseModel

from datetime import datetime, UTC

# instanciando a classe FastAPI
app = FastAPI()

# Criando uma simulação de data base
fake_db = [
    {'title': 'Criando uma aplicação com Django' , 'date': datetime.now(UTC), "published": True},
    {'title': 'Internacionalizando uma app FastAPI' , 'date': datetime.now(UTC), "published": True},
    {'title': 'Internacionalizando uma app Flask' , 'date': datetime.now(UTC), "published": True},
    {'title': 'Internacionalizando uma app Starlett' , 'date': datetime.now(UTC), "published": False}
]


class Post(BaseModel):
    title: str
    date: datetime = datetime.now(UTC)
    published: bool = False
    author: str

# implementando um teste:
class Foo(BaseModel): 
    bar: str
    message: str

# criando um endpoing teste
@app.get('/foobar/', response_model= Foo)
def foobar() -> Foo:
    return {'bar': "foo", "message": "Hello, Word"}



@app.post('/posts/', status_code= status.HTTP_201_CREATED)
def create_post(post: Post):
    fake_db.append(post.model_dump())
    return post

@app.get('/posts/')
def read_posts(
    response: Response, 
    published: bool, 
    limit: int, 
    skip: int = 0, 
    ads_id: Annotated[str | None, Cookie()] = None,
    user_agent: Annotated[str | None, Header()] = None
    
    ):

    response.set_cookie(key= 'user_felipe', value= 'felipe.arq@inlook.com')
    print(f"Cookie: '{ads_id}'")
    print(f"User-agent: '{user_agent}'")

    filtered = [p for p in fake_db if p["published"] == published]
    posts = filtered[skip: skip + limit]  

    return posts


@app.get('/posts/{framework}')  
def read_framework_posts(framework: str): 
    return {
        "posts": [
                {'title': f'Criando uma aplicação com {framework}' , 'date': datetime.now(UTC)},
                
                {'title': f'Internacionalizando uma app {framework}' , 'date': datetime.now(UTC)}
            
            ]
    }