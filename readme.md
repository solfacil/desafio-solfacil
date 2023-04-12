## Como rodar aplicação:
- Python na versão 3.11.2
    - Caso não saiba como alterar versão do python, utilize o pyenv
    - Instale o pyenv[pyenv](https://github.com/pyenv/pyenv)
    - pyenv install 3.11.2
    - pyenv global 3.11.2
    - python3 -V
        - Output esperado: ```Python 3.11.2```
        - Caso dê erro e não altere a versão do python, rode o seguinte comando para atualizar o pyenv no path da sua maquina:
            - ```export PATH="$HOME/.pyenv/versions/3.11.2/bin:$PATH```

- PostgreSQL instalado na sua maquina
    - Necessário criar um banco de dados com o nome de sua preferencia
    - Adicionar o nome desse banco e os acessos no .env


- Crie um ambiente virtual 
    - Navegue até a root do projeto
    - python3 -m venv <nome_do_seu_ambiente>
    - source .venv/bin/activate
    - pip install -U pip
    - pip install -m requirements.txt
- Crie seu arquivo .env no root do projeto
  - Os campos necessários para criar o .env estão no env-example

- Agora tente rodar o python manage.py runserver
 