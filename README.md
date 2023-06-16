# Importação de clientes para parceiros

Criação de API e interface web para importação de clientes em arquivo no formato CSV.

O sistema utiliza uma API externa com para obtenção de dados de endereço por meio de um CEP [Viacep](https://viacep.com.br/)

## Apresentação do problema

Nosso cliente interno precisa atualizar rotineiramente os dados de nossos parceiros. O problema acontece que para atualizar, ele precisa entrar na página de edição de cada um dos parceiros. Isso é um trabalho muito tedioso e demorado.

Precisamos dar uma solução para este problema!

Nossa equipe de produtos pensou que poderíamos fazer uma atualização em lote através de um CSV.

Para maiores informações sobre o escopo do projeto, acesse a [descrição completa](assets/README.md)

## Recursos utilizados

- [Python](https://www.python.org/)
- [FastAPI](https://fastapi.tiangolo.com/)
- [MariaDB](https://mariadb.org/)
- [Sqlite](https://www.sqlite.org/index.html) - Utilizado no conjunto de testes do App
- [Docker](https://www.docker.com/)
- [Bootstrap](https://getbootstrap.com/docs/5.0/getting-started/introduction/)

O conjunto de recursos Python, FastAPI e Bootstrap formam o App, ou dashboard, e a API criados para o projeto.

O Sqlite está sendo utilizado para mock da base e realização de testes do App.

O banco relacional MariaDB está sendo utilizado para armazenar os dados de clientes e endereços.

## Configuração do ambiente

Para iniciar o uso do sistema é necessário possuir o docker e o docker compose em seu ambiente. As portas de conexão utilizadas pelos contêineres por default são:

- FastAPI :9092
- MySQL :3306

É necessário manter essas portas disponíveis em seu ambiente para que a rede utilizada pelos contêineres seja criada e funcione corretamente.

Baixe os arquivos deste repositório e acesse o diretório que será criado.

Execute o comando para inicar os serviços por meio do docker e aguarde alguns minutos. Se não quiser observar os logs das operações que estão sendo realizadas no uso do sistema, adicione ao final do comando a opção -d. Após a configuraçã do ambiente você será capaz de acessar o dashboard na URL: http://0.0.0.0:9092

```bash
$ docker-compose up
```
## Documentação

É possível acessar a documentação gerada para a aplicação nas URL's http://0.0.0.0:9092/docs e http://0.0.0.0:9092/redoc

### Testes

Para executar os testes criados para o sistema é necessário acessar o contâiner que roda o App e executar o comando para iniciar os testes.

```bash
$ docker exec -it nome_do_container bash
$ pytest -v
```
