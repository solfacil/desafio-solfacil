<!-- Title -->

<h1 align="center">
   Solfácil
</h1>

<!-- Description -->

<h3 align="center">
   Projeto de atualização em lote de parceiros via API
</h3>

<br>

<!-- Table of content -->

Conteúdos
=================
- [Sobre o projeto](#sobre-o-projeto)
- [Funcionalidades](#funcionalidades)
- [Rodando a aplicação](#rodando-a-aplicação)
   - [Docker](#docker)
- [Exemplo API](#exemplo-da-api)
- [Tecnologias utilizadas no projeto](#tecnologias-utilizadas-no-projeto)
- [Autor](#autor)

---

## 💻 Sobre o projeto

Projeto para atualização rotineira dos dados dos parceiros da Solfácil.

<p align="center">
   <img alt="Solfácil" width="800" src="./assests/images/solfacil_logo.png">
</p>

---

## Funcionalidades

- [x] Endpoint para upload de arquivo csv (criar ou atualizar parceiro)
- [x] Endpoint para listagem dos parceiros

---

## Rodando a aplicação

```bash
# Clone this repository
$ git clone https://github.com/IgorFreitasCruz/desafio_solfacil-api.git .

# Access the project folder 
$ cd desafio_solfacil
```

---

### Docker

```bash
# run the container
$ docker-compose up -d
```

---

## Acessando a aplicação

Para ter acesso à aplicação va para ```http://localhost:8000/parceiros/upload```

<p align="center">
   <img alt="admin" width="800" src="static/images/admin.png">
</p>

---

### Exemplo da API
Para exibir os resultados formatados adicione `| python -m json.tool` no final do comando

```bash
$ curl -H "Content-Type: application/javascript" http://localhost:8000/parceiros/
```

<p align="center">
   <img alt="api" width="800" src="static/images/api.png">
</p>

---

## Tecnologias utilizadas no projeto

-   FastAPI
-   Flask
-   Docker
-   Postgresql

---

## Autor
<a>
 <img style="border-radius: 50%;" src="static/images/igor.jpeg" width="100px;" alt=""/>
 <br />
 <sub><b>Igor de Freitas Cruz</b></sub></a> 🚀
 <br />

[![Linkedin Badge](https://img.shields.io/badge/-Igor-blue?style=flat-square&logo=Linkedin&logoColor=white&link=https://www.linkedin.com/in/igorfreitascruz/)](https://www.linkedin.com/in/igorfreitascruz/)
[![Apple Badge](https://img.shields.io/badge/-igor.freitas.cruz@icloud.com-c14438?style=flat-square&logo=iCloud&logoColor=white&link=mailto:igor.freitas.cruz@icloud.com)](mailto:igor.freitas.cruz@icloud.com)

---

Made with ❤️ by Igor Cruz 👋🏻 [Contact me!](https://www.linkedin.com/in/igorfreitascruz/)