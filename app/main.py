from fastapi import FastAPI
from datetime import datetime, UTC

# instanciando a classe FastAPI
app = FastAPI()

# Criando rota
@app.get('/posts/{framework}')  # definimos o verbo HTTP que vamos usar
def read_posts(framework):
    return {
        "posts": [
                {'title': f'Criando uma aplicação com {framework}' , 'date': datetime.now(UTC)},
                
                {'title': f'Internacionalizando uma app {framework}' , 'date': datetime.now(UTC)}
            
            ]
    } # retorna uma lista de posts