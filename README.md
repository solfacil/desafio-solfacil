# Desafio Solfácil

## Apresentação do problema

Nosso cliente interno precisa atualizar rotineiramente os dados de nossos parceiros. O problema acontece que para atualizar, ele precisa entrar na página de edição de cada um dos parceiros. Isso é um trabalho muito tedioso e demorado.

Precisamos dar uma solução para este problema!

Nossa equipe de produtos pensou que poderíamos fazer uma atualização em lote através de um CSV.

[Baixe aqui um CSV de exemplo](assets/exemplo.csv)

## Execução

Rodando via taskfile
```
task run:docker
```
Execução com docker-compose

Para executar direto no docker-compose, basta executar os seguintes comandos

```
docker-compose build 
docker-compose up 
```

Rodando testes localmente via taskfile
```
task local:test
```

## Comportamento

A aplicação roda na porta 8008 com o docker. Além disso só inserimos no banco de dados quando o usuário possui um email valido e um cnpj de 14 números

Existem dois endpoints

Retorno de todos os registros do banco de dados
![image](https://github.com/Fernando-Erd/desafio-solfacil/assets/23130033/c7a5d95a-fdec-4029-8485-8542bd42c3c5)

Inserção/Atualização de registros via CSV
![image](https://github.com/Fernando-Erd/desafio-solfacil/assets/23130033/58bb6258-cc68-44fd-999c-06cee8e01cd3)


