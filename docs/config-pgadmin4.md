# Configurando o pgadmin 4 do docker

Configurar o PGadmin é bem simples, segue o passo a passo:

- Acesse o ```localhost:5050```
- Acesse com o email e senha que você colocou no .env
- Ao acessar, clique com o botão direito na parte de servers
    - Clique em "Register"
        - Clique em "Server"
    - Dê o nome que você preferir ao server
    - Na aba connection faça o seguinte:
        - No host name/address tem que ser o nome da instancia do postgres do seu docker, no caso vai ser "pg_container"
            - Seria possível utilizar o ip do container docker, mas vamos usaro  nome mesmo
        - username será o username que você definiu no DB_USER na sua .env
        - password será a passwdor que você definiu no DB_PASSWORD na sua .env
- Ta pronto o sorvetinho 🍦 