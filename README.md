# Desafio Solfácil

## Apresentação do problema

Nosso cliente interno precisa atualizar rotineiramente os dados de nossos parceiros. O problema acontece que para atualizar, ele precisa entrar na página de edição de cada um dos parceiros. Isso é um trabalho muito tedioso e demorado.

Precisamos dar uma solução para este problema!

Nossa equipe de produtos pensou que poderíamos fazer uma atualização em lote através de um CSV.

[Baixe aqui um CSV de exemplo](assets/exemplo.csv)

## Requisitos

- Criar um endpoint que irá receber um CSV por upload e ao processar este CSV, vamos atualizar um parceiro já existente e/ou criar um novo parceiro;
- Criar um endpoint de listagem dos parceiros;
- Documentação de como rodar aplicação;
- Testes unitários e/ou de integração.

## Bônus

- Validações dos campos, não queremos que um CPF entre no lugar de um CNPJ;
- Seria interessante se tivéssemos as informações de Cidade e Estado de nossos parceiros em nosso banco de dados, esses dados podem ser adquiridos nesse ws https://viacep.com.br/ws/CEP_DO_PARCEIRO/json/;
- Envio de boas vindas para os novos parceiros (o envio de email não precisa acontecer de fato, pode ser apenas logado);
- Utilizar docker, seria legal subir o seu sistema com apenas uma linha de comando.
- Interface em HTML
- Documentação dinamica (Swagger/Openapi)

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
