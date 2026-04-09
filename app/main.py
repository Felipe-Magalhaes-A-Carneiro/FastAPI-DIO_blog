from fastapi import FastAPI

# instanciando a classe FastAPI
app = FastAPI()

# implementando um teste:
class Foo(BaseModel): 
    bar: str
    message: str

# criando um endpoing teste
@app.get('/foobar/', response_model= Foo)
def foobar() -> Foo:
    return {'bar': "foo", "message": "Hello, Word"}




