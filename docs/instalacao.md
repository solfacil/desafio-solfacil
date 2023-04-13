# Instalaçao da aplicação e como rodar aplicação

### O que vamos precisar? 
- Python na versão 3.11.2
    - Caso não saiba como alterar versão do python, utilize o pyenv
    - Instale o pyenv[pyenv](https://github.com/pyenv/pyenv)
    - pyenv install 3.11.2
    - pyenv global 3.11.2
    - python3 -V
        - Output esperado: ```Python 3.11.2```
        - Caso dê erro e não altere a versão do python, rode o seguinte comando para atualizar o pyenv no path da sua maquina:
            - ```export PATH="$HOME/.pyenv/versions/3.11.2/bin:$PATH"```

- Crie um ambiente virtual 
    - Navegue até a root do projeto
    - python3 -m venv <nome_do_seu_ambiente>
    - source .venv/bin/activate
    - pip install -U pip
    - pip install -r requirements.txt

- Crie seu arquivo .env no root do projeto
  - Os campos necessários para criar o .env estão no env-example
  - Os valores no .env muito importantes, com eles você vai fazer a conexão tanto da aplicação, quanto do postgres e pgadmin.

- Docker instalado na maquina
    - Com o docker instalado na maquina rode o comando ```docker-compose up``` esse comando vai subir o banco de dados postgres e o pgadmin, o postgres vai rodar na porta 5433
    - **Esse passo não é obrigatorio** mas caso queira rodar o banco em um gerenciador como pg admin:
        - Caso queira usar o pgadmin 4 que foi usado no docker acesse esse [link](docs/config-pgadmin4)
        - Se não, só usar o gerenciador de banco de dados de sua preferencia

- Com o docker up, agora suba as migrations com ``` python manage.py migrate```
- Após sucesso, rode o ``` python manage.py runserver ```