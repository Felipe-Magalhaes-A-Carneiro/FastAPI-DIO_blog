from fastapi import FastAPI
from datetime import datetime, UTC

# instanciando a classe FastAPI
app = FastAPI()

# Criando uma simulação de data base
fake_db = [
    {'title': 'Criando uma aplicação com Django' , 'date': datetime.now(UTC)},
    {'title': 'Internacionalizando uma app FastAPI' , 'date': datetime.now(UTC)},
    {'title': 'Internacionalizando uma app Flask' , 'date': datetime.now(UTC)},
    {'title': 'Internacionalizando uma app Starlett' , 'date': datetime.now(UTC)}

]

#Criando novo método
@app.get('/posts')
def read_posts(skip: int = 0, limit: int = len(fake_db)):
    return fake_db


# Criando rota
@app.get('/posts/{framework}')  
def read_framework_posts(framework: str): 
    return {
        "posts": [
                {'title': f'Criando uma aplicação com {framework}' , 'date': datetime.now(UTC)},
                
                {'title': f'Internacionalizando uma app {framework}' , 'date': datetime.now(UTC)}
            
            ]
    } # retorna uma lista de posts