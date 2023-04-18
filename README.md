# Desafio Solfácil

## Apresentação do problema

Nosso cliente interno precisa atualizar rotineiramente os dados de nossos parceiros. O problema acontece que para atualizar, ele precisa entrar na página de edição de cada um dos parceiros. Isso é um trabalho muito tedioso e demorado.

Precisamos dar uma solução para este problema!

Nossa equipe de produtos pensou que poderíamos fazer uma atualização em lote através de um CSV.

[Baixe aqui um CSV de exemplo](assets/exemplo.csv)

## Requisitos

- python 3.10+
- [poetry](https://python-poetry.org/docs/#installation)

## Instalando as dependências

Com o poetry instalado, execute o comando abaixo, o poetry irá verificar se o sistema atende aos requisitos e instalar 
as dependências.

```bash
poetry install
```

## Configurando o projeto

### Variáveis de ambiente

A applicação está configurada para aceitar os seguintes arquivos .env: `.env.dev`, `.env.prod`. Cada um deles representa
um ambiente de execução.

O arquivo `.env.dev` é utilizado para executar a aplicação em modo de desenvolvimento, já o `.env.prod` é utilizado para
produção.

A aplicação sempre irá preferir o arquivo `.env.prod`.

Um exemplo de arquivo `.env` pode ser encontrado em `.env.example`.

Caso nenhum arquivo `.env` seja encontrado, a aplicação irá utilizar as variáveis de ambiente do sistema e caso não encontre
nenhuma delas, irá utilizar os valores padrões.

### Migrations
Para executar as migrations, execute o comando abaixo:

```bash
poetry shell
python manage.py migrate
```

## Iniciando django em modo de desenvolvimento

```bash
poetry shell
python manage.py runserver
```

## Executando os testes

```bash
poetry shell
python manage.py test
```

## Executando o lint

```bash
poetry shell
black --config ./pyproject.toml --check .
flake8
```

## Executando em modo de produção

```bash
poetry shell
gunicorn --bind :8000 desafio_solfacil.wsgi:application --workers 3
```

## Docker

O projeto está configurado para rodar em um container docker. Para executar o projeto em um container docker.

### Executando em modo de desenvolvimento

```bash
docker-compose -f docker-compose.dev.yml up -d
```

### Executando em modo de produção

```bash
docker-compose -f docker-compose.prod.yml up -d
```

## Bibliotecas utilizadas
- [Django](https://www.djangoproject.com/)
- [Django Rest Framework](https://www.django-rest-framework.org/)
- [Django Phonenumbers Field](https://django-phonenumber-field.readthedocs.io/en/latest/)
- [Drf-yasg](https://drf-yasg.readthedocs.io/en/stable/)