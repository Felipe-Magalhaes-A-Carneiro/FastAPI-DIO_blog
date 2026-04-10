from fastapi import FastAPI

from controllers import post

# instanciando a classe FastAPI
app = FastAPI()
app.include_router(post.router)








# # implementando um teste:
# class Foo(BaseModel): 
#     bar: str
#     message: str

# # criando um endpoing teste
# @app.get('/foobar/', response_model= Foo)
# def foobar() -> Foo:
#     return {'bar': "foo", "message": "Hello, Word"}




