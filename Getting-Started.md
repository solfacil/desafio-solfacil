# SolFacil Challenge API

Este projeto é uma API desenvolvida como solução para o desafio proposto pela SolFacil. A API permite gerenciar parceiros, incluindo funcionalidades como listar, criar, atualizar, deletar e pesquisar parceiros, bem como carregar parceiros a partir de um arquivo CSV.

## Requisitos

- Python 3.10
- Docker e Docker Compose

## Bibliotecas utilizadas

- FastAPI: para criar a API RESTful.
- Gunicorn: como servidor WSGI.
- SQLAlchemy: para o ORM e gerenciamento do banco de dados.
- Alembic: para migrações do banco de dados.
- PostgreSQL: como banco de dados.
- psycopg2-binary: como driver para PostgreSQL.
- python-dotenv: para gerenciamento de variáveis de ambiente.
- Unidecode: para manipulação de strings com caracteres especiais.
- validate-docbr: para validação de CNPJ.
- requests: para fazer requisições HTTP.
- commitizen, isort, flake8, black, pre-commit, pytest, pytest-cov, requests-mock e pytest-csv: para desenvolvimento e testes.

## Documentação da API

A documentação da API está disponível de três formas:

1. Documentação interativa com o Swagger UI, acessível em `http://localhost:5001/docs` após iniciar a API.
2. Documentação em markdown de todas as rotas no arquivo [Api_Documentation.md](https://github.com/PHRaulino/solfacil-challenge-ph/blob/challenge-solution/Api_Documentation.md).
3. Documentação estática gerada com o Redoc e o Swagger UI, disponível no GitHub Pages: [https://phraulino.github.io/solfacil-challenge-ph](https://phraulino.github.io/solfacil-challenge-ph). Note que esta versão estática não permite realizar requisições diretamente.

## Instruções de instalação e execução

1. Clone o repositório:

```
git clone https://github.com/phraulino/solfacil-challenge-ph.git
```

2. Entre no diretório do projeto:

```
cd solfacil-challenge-ph
```

3. Crie um arquivo `.env` com as variáveis de ambiente necessárias. Você pode usar o arquivo `.env.example` como referência.

4. Inicie a aplicação com o Docker Compose:

```
docker-compose up --build
```

A API estará disponível no endereço `http://localhost:5001`. Para acessar a documentação interativa da API, visite `http://localhost:5001/docs`.

## Rotas da API

- Listar parceiros: `GET /`
- Criar parceiro: `POST /`
- Atualizar parceiro: `PUT /{cnpj}`
- Deletar parceiro: `DELETE /{cnpj}`
- Buscar parceiro por CNPJ: `GET /{cnpj}`
- Pesquisar parceiros: `GET /?search_criteria={search_criteria}`
- Carregar parceiros via CSV: `POST /partners/`

## Licença

Este projeto está licenciado sob a Licença MIT.
