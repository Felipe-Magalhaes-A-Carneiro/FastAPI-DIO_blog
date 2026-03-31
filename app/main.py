from fastapi import FastAPI
from datetime import datetime, UTC

# instanciando a classe FastAPI
app = FastAPI()

# Criando rota
@app.get('/posts/{framework}')  # definimos que o framework que utilizaremos é qualquer um que dermos no path
def read_posts(framework: str): # definimos que o framework usado é uma string, o que ele aceita até um string como '10' como um path
    return {
        "posts": [
                {'title': f'Criando uma aplicação com {framework}' , 'date': datetime.now(UTC)},
                
                {'title': f'Internacionalizando uma app {framework}' , 'date': datetime.now(UTC)}
            
            ]
    } # retorna uma lista de posts