from fastapi import FastAPI, status
from pydantic import BaseModel

from datetime import datetime, UTC

# instanciando a classe FastAPI
app = FastAPI()

# Criando uma simulação de data base
fake_db = [
    {'title': 'Criando uma aplicação com Django' , 'date': datetime.now(UTC), "published": True},
    {'title': 'Internacionalizando uma app FastAPI' , 'date': datetime.now(UTC), "published": True},
    {'title': 'Internacionalizando uma app Flask' , 'date': datetime.now(UTC), "published": True},
    {'title': 'Internacionalizando uma app Starlett' , 'date': datetime.now(UTC), "published": True}
]

#Criando mapeamento
class Post(BaseModel):
    title: str
    date: datetime = datetime.now(UTC)
    published: bool = False
    author: str


#Criando novo método
@app.post('/posts/', status_code= status.HTTP_201_CREATED)
def create_post(post: Post):

    return post


@app.get('/posts/')
def read_posts(published: bool, skip: int = 0, limit: int = len(fake_db)):
    return [post for post in fake_db[skip: skip + limit] if post["published"] is published]


@app.get('/posts/{framework}')  
def read_framework_posts(framework: str): 
    return {
        "posts": [
                {'title': f'Criando uma aplicação com {framework}' , 'date': datetime.now(UTC)},
                
                {'title': f'Internacionalizando uma app {framework}' , 'date': datetime.now(UTC)}
            
            ]
    }