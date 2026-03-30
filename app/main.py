from fastapi import FastAPI

# instanciando a classe FastAPI
app = FastAPI()

# Criando rota
@app.get('/')  # definimos o verbo HTTP que vamos usar
def read_root():
    return {"message": "Hello, Word!"}