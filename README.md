# 🚀 FASTAPI BLOG API (DIO PROJECT)

Descrição
Este projeto consiste no desenvolvimento de uma API REST para um sistema de blog, utilizando o framework FastAPI. O objetivo é aplicar boas práticas de desenvolvimento back-end, organização de código e construção de aplicações modernas e performáticas.

O projeto foi desenvolvido como parte da trilha da Digital Innovation One (DIO), com foco em APIs, arquitetura de software e manipulação de dados.

--------------------------------------------------

## 🎯 Objetivos do Projeto

- Construir uma API REST utilizando FastAPI
- Aplicar operações CRUD (Create, Read, Update, Delete)
- Organizar rotas e estrutura da aplicação
- Aplicar boas práticas de desenvolvimento back-end
- Trabalhar com integração entre aplicação e banco de dados

--------------------------------------------------

## 🛠️ Tecnologias Utilizadas

- Python
- FastAPI
- Uvicorn (servidor ASGI)
- Pydantic (validação de dados)
- SQL (banco de dados relacional)
- Git e GitHub

--------------------------------------------------

## 📁 Estrutura do Projeto

    FastAPI-DIO_blog/
    │
    ├── app/
    │   └── main.py         -> Arquivo principal da aplicação
    ├── models/         -> Modelos de dados
    │   ├── schemas/        -> Validação com Pydantic
    │   ├── database/       -> Configuração do banco
    │   └── tests/          -> Testes
    │
    ├── requirements.txt    -> Dependências do projeto
    └── README.txt

--------------------------------------------------

## ⚙️ Funcionalidades

- Criação de posts
- Listagem de posts
- Atualização de posts
- Remoção de posts
- Estruturação de endpoints REST
- Validação de dados com Pydantic

--------------------------------------------------

## 🔗 Exemplo de Endpoints

    GET    /posts         -> Lista todos os posts
    GET    /posts/{id}    -> Retorna um post específico
    POST   /posts         -> Cria um novo post
    PUT    /posts/{id}    -> Atualiza um post
    DELETE /posts/{id}    -> Remove um post

--------------------------------------------------

## ▶️ Como Executar o Projeto

    1. Clonar o repositório:
    git clone https://github.com/Felipe-Magalhaes-A-Carneiro/FastAPI-DIO_blog

    2. Acessar a pasta:
    cd FastAPI-DIO_blog

    3. Criar ambiente virtual:
    python -m venv venv

    4. Ativar ambiente:
    Windows: venv\Scripts\activate
    Linux/Mac: source venv/bin/activate

    5. Instalar dependências:
    pip install -r requirements.txt

    6. Executar o servidor:
    uvicorn app.main:app --reload

--------------------------------------------------

## 📌 Documentação da API

FastAPI gera documentação automática:

Swagger:
http://127.0.0.1:8000/docs

Redoc:
http://127.0.0.1:8000/redoc

--------------------------------------------------

## 📚 Aprendizados Aplicados

- Construção de APIs REST
- Organização de código e separação de responsabilidades
- Validação de dados com Pydantic
- Integração com banco de dados
- Versionamento com Git

--------------------------------------------------

## 🚀 Próximas Melhorias

- Implementar autenticação (JWT)
- Conectar com banco real (PostgreSQL ou MySQL)
- Criar testes automatizados
- Containerização com Docker
- Deploy em cloud (AWS, Azure ou GCP)

--------------------------------------------------

## 👨‍💻 Autor

Felipe Magalhães de Araujo Carneiro
- GitHub: https://github.com/Felipe-Magalhaes-A-Carneiro
- LinkedIn: https://www.linkedin.com/in/felipe-magalhaes-arq/