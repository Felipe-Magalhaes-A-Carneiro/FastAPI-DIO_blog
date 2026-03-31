from fastapi import FastAPI
from datetime import datetime, UTC

# instanciando a classe FastAPI
app = FastAPI()

# Criando rota
@app.get('/posts/{framework}')  # definimos o verbo HTTP que vamos usar
def read_posts():
    return {"posts": [
                {'title': 'Criando uma aplicação com {framework}' , 'date': datetime.now(UTC)},
                
                {'title': 'Internacionalizando uma app {framework}' , 'date': datetime.now(UTC)}
            
            ]
    } # retorna uma lista de posts