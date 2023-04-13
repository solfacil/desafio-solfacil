# Autenticação

Todas as APIs estão protegidas com uma autenticação, após você ter iniciado a aplicação e subi os migrations (caso ainda não tenha feito isso, acesse [esse link](docs/instalacao.md))

Para fazer a autenticação siga esses passos:
- No projeto você precisa criar um super usuário, usuário esse que será necessário para fazer a autenticação:
    - No root do projeto (aonde ta o manage.py)
        - python manage.py createsuperuser
            - coloque o nome que preferir e de enter (se deixar em branco ele pegar o do proprio PC)
            - Não precisa de email, só dar enter
            - Escolha uma senha
                - Se você colocou uma senha fácil como por exemplo: root, no fim ele vai perguntar se você realmente quer criar uma com senha fácil, só digitar y 
- Com o super user criado, vamos utilizar ele na requisição do token.
    - acesse o endpoint localhost:<sua_porta>/api/token/
    - Coloque como requisição de post passando no body:
        ```
        {
            "username": "usuario_que_vc_criou",
            "password": "senha_braba_que_vc_criou"
        }
        ```
    - O output disso será um token e um refresh token, vamos precisar do token
- Com o token em mão, vamos colocar o endpoint que vamos acessar
    - Dentro do header no seu aplicativo ou CURL você coloca:
        - A key vai ser: Authorization
        - o value vai ser Bearer <seu_token_aqui>
        - Como por exemplo:
            - ```curl -H "Authorization: Bearer seu_token" http://127.0.0.1:8000/api/parceiro/```
- Prontinho, você já tem o auth do seu endpoint