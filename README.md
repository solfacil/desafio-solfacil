# Desafio Solfácil

Esse é um teste focado em design de código e conhecimento em programação funcional. O objetivo é avaliar sua experiênica em escrever código de fácil manutenção e alta coesão.

## Apresentação do problema

Nosso cliente interno precisa atualizar rotineramente os dados de nossos parceiros. O problema acontece que para atualizar, ele precisa entrar na página de edição de cada um dos parceiros. Isso é um trabalho muito tedioso e demorado.

Precisamos dar uma solução para este problema!

Nossa equipe de produtos pensou que poderíamos fazer uma atualização em lote através de um CSV. Então, o desafio consiste em criar um endpoint que irá receber um CSV por upload e ao processar este CSV, vamos atualizar um parceiro já existente e/ou criar um novo parceiro.

[Baixe aqui um CSV de exemplo](assets/exemplo.csv)

## Tecnologias usadas

Os pré-requisitos para a aplicação:

- Use o Elixir como linguagem;
- O Banco deve ser relacional, de preferência POSTGRESQL;
- Docker não é obrigatório, mas seria legal subir o seu sistema com apenas uma linha de comando.

## Avaliação

Para nos enviar seu código, você poderá escolher as 2 opções abaixo:

- Fazer um fork desse repositório e nos mandar um pull-request
- Enviar o projeto compactado para o e-mail recrutamento@solfacil.com.br.

## Dicas

- Aproveite os recursos das ferramentas que você está usando. Diversifique e mostre que você domina cada uma delas;
- Tente escrever seu código o mais claro e limpo possível. Código deve ser legível assim como qualquer texto dissertativo;
- Documentação sucinta e explicativa de como rodar seu código e levantar os ambientes.
- Teste unitários será um diferencial;
- Validações dos campos, não queremos que um CPF entre no lugar de um CNPJ.
- Seria interessante se tivéssemos as informações de cidade e Estado de nossos parceiros em nosso banco de dados.

Qualquer dúvida técnica, envie uma mensagem para recrutamento@solfacil.com.br.

Você terá 7 dias para fazer esse teste, a partir do recebimento deste desafio. Sucesso!
