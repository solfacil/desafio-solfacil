# Desafio Solfácil

## Apresentação do problema

Nosso cliente interno precisa atualizar rotineiramente os dados de nossos parceiros. O problema acontece que para atualizar, ele precisa entrar na página de edição de cada um dos parceiros. Isso é um trabalho muito tedioso e demorado.

Precisamos dar uma solução para este problema!

Nossa equipe de produtos pensou que poderíamos fazer uma atualização em lote através de um CSV.

[Baixe aqui um CSV de exemplo](assets/exemplo.csv)

## Requisitos

- Criar um endpoint que irá receber um CSV por upload e ao processar este CSV, vamos atualizar um parceiro já existente e/ou criar um novo parceiro;
- Criar um endpoint de listagem dos parceiros;
- Documentação de como rodar aplicação.

## Bônus

- Validações dos campos, não queremos que um CPF entre no lugar de um CNPJ;
- Seria interessante se tivéssemos as informações de Cidade e Estado de nossos parceiros em nosso banco de dados, esses dados podem ser adquiridos nesse ws https://viacep.com.br/ws/CEP_DO_PARCEIRO/json/;
- Envio de boas vindas para os novos parceiros (o envio de email não precisa acontecer de fato, pode ser apenas logado);
- Testes unitários e de integração serão um diferencial;
- Utilizar docker, seria legal subir o seu sistema com apenas uma linha de comando.

## Tecnologias usadas

- Preferencialmente utilizar Python como linguagem;

## Dicas

- Aproveite os recursos das ferramentas que você está usando. Diversifique e mostre que você domina cada uma delas;
- Tente escrever seu código o mais claro e limpo possível. Código deve ser legível assim como qualquer texto dissertativo;
- Documentação sucinta e explicativa de como rodar seu código e levantar os ambientes;
- OBS: Não precisa criar um front-end para aplicação.

## Objetivo

- O objetivo é avaliar sua experiência em escrever código de fácil manutenção e alta coesão.

## Envio

Para nos enviar seu código, faça um fork desse repositório e nos envie um pull-request.

Qualquer dúvida técnica, envie uma mensagem para recrutamento@solfacil.com.br.

Você terá 7 dias para fazer esse teste, a partir do recebimento deste desafio. Sucesso!

# Como rodar o projeto (Linux)?

**Importante:** Para rodar o projeto é necessário ter instalado o docker e o docker-compose.

Renomei o arquivo `.env.dev.example` para `.env.dev`. No arquivo `.env.dev.example` tem as váriaveis de ambientes necessárias com exemplos de valores preenchidos.

É possível subir o ambiente de dev com apenas um comando, caso o seu sistema operacional tenha suporte para rodar comando de bash:

```
$ bash up.dev.sh
```

Se não tiver suporte basta rodar:

```
$ docker-compose -f docker-compose.dev.yml --env-file .env.dev up -d --build --remove-orphans
```

**O arquivo Desafio.postman_collection.json contém os endpoints necessário em Postman**

Básicamente são esses:

```
[GET] {{host}}/api/partner/
```

```
[POST] {{host}}/api/partner/upload/
```

# Como rodar os testes unitários e de integração ?

Para rodar o teste de cobertura é necessário instalar a biblioteca coverage que está no requirements_dev.txt:

- Exemplo usando pip e venv

  [Crie um ambiente virtual e ative-o:](https://docs.python.org/pt-br/3.5/tutorial/venv.html)

  ```
  pyvenv .env
  source .env/bin/activate
  pip install -r requirements.txt
  ```

- [Com o poetry crie um ambiente virtual e ative-o:](https://python-poetry.org/)

  ```
  $ poetry shell
  $ poetry install
  ```

Para rodar os testes usando o bash script:

```
$ bash test.sh
```

Sem o bash script:

```
python -m unittest discover -v -s . -p "*test*.py"
```

Ao instalar a a biblioteca coverage:

Rode a cobertura de testes com bash script:

```
$ bash coverage.sh
```

Sem o bash script:

```
$ python -m coverage run -m unittest
$ python -m coverage report
$ python -m coverage html
```

**Importante: para o teste de integração rodar é necessário que o ambiente esteja levantado e rodando**
