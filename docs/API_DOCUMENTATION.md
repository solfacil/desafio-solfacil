<!-- Generator: Widdershins v4.0.1 -->

<h1 id="parceiros-api">Parceiros API v1.0.0</h1>

> Scroll down for code samples, example requests and responses. Select a language for code samples from the tabs above or the mobile navigation menu.

Uma API para gerenciamento de parceiros, permitindo atualizar e criar novos parceiros a partir de arquivos CSV e listar os parceiros existentes.

Email: <a href="mailto:phraulino@outlook.com">Paulo Henrique Silva</a> Web: <a href="https://phraulino.super.site/">Paulo Henrique Silva</a> 
License: <a href="https://opensource.org/licenses/MIT">MIT</a>

<h1 id="parceiros-api-padr-es">Padrões</h1>

## favicon_favicon_ico_get

<a id="opIdfavicon_favicon_ico_get"></a>

> Code samples

```python
import requests
headers = {
  'Accept': 'application/json'
}

r = requests.get('/favicon.ico', headers = headers)

print(r.json())

```

`GET /favicon.ico`

*Favicon*

> Example responses

> 200 Response

```json
null
```

<h3 id="favicon_favicon_ico_get-responses">Responses</h3>

|Status|Meaning|Description|Schema|
|---|---|---|---|
|200|[OK](https://tools.ietf.org/html/rfc7231#section-6.3.1)|Successful Response|Inline|

<h3 id="favicon_favicon_ico_get-responseschema">Response Schema</h3>

<aside class="success">
This operation does not require authentication
</aside>

## root__get

<a id="opIdroot__get"></a>

> Code samples

```python
import requests
headers = {
  'Accept': 'application/json'
}

r = requests.get('/', headers = headers)

print(r.json())

```

`GET /`

*Root*

> Example responses

> 200 Response

```json
null
```

<h3 id="root__get-responses">Responses</h3>

|Status|Meaning|Description|Schema|
|---|---|---|---|
|200|[OK](https://tools.ietf.org/html/rfc7231#section-6.3.1)|Successful Response|Inline|

<h3 id="root__get-responseschema">Response Schema</h3>

<aside class="success">
This operation does not require authentication
</aside>

<h1 id="parceiros-api-crud-parceiros">Crud Parceiros</h1>

## listar_parceiros_partners__get

<a id="opIdlistar_parceiros_partners__get"></a>

> Code samples

```python
import requests
headers = {
  'Accept': 'application/json'
}

r = requests.get('/partners/', headers = headers)

print(r.json())

```

`GET /partners/`

*Listar parceiros*

Recupera uma lista de parceiros, com paginação.

<h3 id="listar_parceiros_partners__get-parameters">Parameters</h3>

|Name|In|Type|Required|Description|
|---|---|---|---|---|
|skip|query|integer|false|Número de registros para pular na listagem|
|limit|query|integer|false|Limite de registros a serem retornados na listagem|

> Example responses

> 200 Response

```json
[
  {
    "razao_social": "Empresa razao social",
    "nome_fantasia": "Empresa exemplo",
    "telefone": "(12) 3456-7890",
    "email": "exemplo@email.com",
    "cep": "12345-678",
    "cnpj": "01.234.567/8912-34",
    "id_parceiro": "hash uuid",
    "zip_code_info": {
      "cep": "22783115",
      "bairro": "Centro",
      "localidade": "São Paulo",
      "uf": "SP",
      "last_update": "2019-08-24T14:15:22Z"
    },
    "last_update": "2019-08-24T14:15:22Z"
  }
]
```

<h3 id="listar_parceiros_partners__get-responses">Responses</h3>

|Status|Meaning|Description|Schema|
|---|---|---|---|
|200|[OK](https://tools.ietf.org/html/rfc7231#section-6.3.1)|Successful Response|Inline|
|422|[Unprocessable Entity](https://tools.ietf.org/html/rfc2518#section-10.3)|Validation Error|[HTTPValidationError](#schemahttpvalidationerror)|

<h3 id="listar_parceiros_partners__get-responseschema">Response Schema</h3>

Status Code **200**

*Response Listar Parceiros Partners  Get*

|Name|Type|Required|Restrictions|Description|
|---|---|---|---|---|
|Response Listar Parceiros Partners  Get|[[PartnerSchema](#schemapartnerschema)]|false|none|none|
|» PartnerSchema|[PartnerSchema](#schemapartnerschema)|false|none|none|
|»» razao_social|string|false|none|none|
|»» nome_fantasia|string|false|none|none|
|»» telefone|string|false|none|none|
|»» email|string|false|none|none|
|»» cep|string|true|none|none|
|»» cnpj|string|true|none|none|
|»» id_parceiro|string|true|none|none|
|»» zip_code_info|[ZipCodeSchema](#schemazipcodeschema)|true|none|none|
|»»» cep|string|true|none|none|
|»»» bairro|string|true|none|none|
|»»» localidade|string|true|none|none|
|»»» uf|string|true|none|none|
|»»» last_update|string(date-time)|true|none|none|
|»» last_update|string(date-time)|true|none|none|

<aside class="success">
This operation does not require authentication
</aside>

## criar_parceiro_partners__post

<a id="opIdcriar_parceiro_partners__post"></a>

> Code samples

```python
import requests
headers = {
  'Content-Type': 'application/json',
  'Accept': 'application/json'
}

r = requests.post('/partners/', headers = headers)

print(r.json())

```

`POST /partners/`

*Criar parceiro*

Cria um novo parceiro com as informações fornecidas.

> Body parameter

```json
{
  "razao_social": "Empresa razao social",
  "nome_fantasia": "Empresa exemplo",
  "telefone": "(12) 3456-7890",
  "email": "exemplo@email.com",
  "cep": "12345-678",
  "cnpj": "01.234.567/8912-34"
}
```

<h3 id="criar_parceiro_partners__post-parameters">Parameters</h3>

|Name|In|Type|Required|Description|
|---|---|---|---|---|
|body|body|[PartnerJsonSchema](#schemapartnerjsonschema)|true|none|

> Example responses

> 201 Response

```json
{
  "razao_social": "Empresa razao social",
  "nome_fantasia": "Empresa exemplo",
  "telefone": "(12) 3456-7890",
  "email": "exemplo@email.com",
  "cep": "12345-678",
  "cnpj": "01.234.567/8912-34",
  "id_parceiro": "hash uuid",
  "zip_code_info": {
    "cep": "22783115",
    "bairro": "Centro",
    "localidade": "São Paulo",
    "uf": "SP",
    "last_update": "2019-08-24T14:15:22Z"
  },
  "last_update": "2019-08-24T14:15:22Z"
}
```

<h3 id="criar_parceiro_partners__post-responses">Responses</h3>

|Status|Meaning|Description|Schema|
|---|---|---|---|
|201|[Created](https://tools.ietf.org/html/rfc7231#section-6.3.2)|Successful Response|[PartnerSchema](#schemapartnerschema)|
|422|[Unprocessable Entity](https://tools.ietf.org/html/rfc2518#section-10.3)|Validation Error|[HTTPValidationError](#schemahttpvalidationerror)|

<aside class="success">
This operation does not require authentication
</aside>

## atualizar_parceiro_partners__cnpj__put

<a id="opIdatualizar_parceiro_partners__cnpj__put"></a>

> Code samples

```python
import requests
headers = {
  'Content-Type': 'application/json',
  'Accept': 'application/json'
}

r = requests.put('/partners/{cnpj}', headers = headers)

print(r.json())

```

`PUT /partners/{cnpj}`

*Atualizar parceiro*

Atualiza as informações do parceiro com o CNPJ fornecido.

> Body parameter

```json
{
  "razao_social": "Empresa razao social",
  "nome_fantasia": "Empresa exemplo",
  "telefone": "(12) 3456-7890",
  "email": "exemplo@email.com",
  "cep": "string"
}
```

<h3 id="atualizar_parceiro_partners__cnpj__put-parameters">Parameters</h3>

|Name|In|Type|Required|Description|
|---|---|---|---|---|
|cnpj|path|string|true|none|
|body|body|[PartnerUpdateSchema](#schemapartnerupdateschema)|true|none|

> Example responses

> 200 Response

```json
{
  "razao_social": "Empresa razao social",
  "nome_fantasia": "Empresa exemplo",
  "telefone": "(12) 3456-7890",
  "email": "exemplo@email.com",
  "cep": "12345-678",
  "cnpj": "01.234.567/8912-34",
  "id_parceiro": "hash uuid",
  "zip_code_info": {
    "cep": "22783115",
    "bairro": "Centro",
    "localidade": "São Paulo",
    "uf": "SP",
    "last_update": "2019-08-24T14:15:22Z"
  },
  "last_update": "2019-08-24T14:15:22Z"
}
```

<h3 id="atualizar_parceiro_partners__cnpj__put-responses">Responses</h3>

|Status|Meaning|Description|Schema|
|---|---|---|---|
|200|[OK](https://tools.ietf.org/html/rfc7231#section-6.3.1)|Successful Response|[PartnerSchema](#schemapartnerschema)|
|422|[Unprocessable Entity](https://tools.ietf.org/html/rfc2518#section-10.3)|Validation Error|[HTTPValidationError](#schemahttpvalidationerror)|

<aside class="success">
This operation does not require authentication
</aside>

## deletar_parceiro_partners__cnpj__delete

<a id="opIddeletar_parceiro_partners__cnpj__delete"></a>

> Code samples

```python
import requests
headers = {
  'Accept': 'application/json'
}

r = requests.delete('/partners/{cnpj}', headers = headers)

print(r.json())

```

`DELETE /partners/{cnpj}`

*Deletar parceiro*

Deleta o parceiro com o CNPJ fornecido.

<h3 id="deletar_parceiro_partners__cnpj__delete-parameters">Parameters</h3>

|Name|In|Type|Required|Description|
|---|---|---|---|---|
|cnpj|path|string|true|none|

> Example responses

> 422 Response

```json
{
  "detail": [
    {
      "loc": [
        "string"
      ],
      "msg": "string",
      "type": "string"
    }
  ]
}
```

<h3 id="deletar_parceiro_partners__cnpj__delete-responses">Responses</h3>

|Status|Meaning|Description|Schema|
|---|---|---|---|
|204|[No Content](https://tools.ietf.org/html/rfc7231#section-6.3.5)|Successful Response|None|
|422|[Unprocessable Entity](https://tools.ietf.org/html/rfc2518#section-10.3)|Validation Error|[HTTPValidationError](#schemahttpvalidationerror)|

<aside class="success">
This operation does not require authentication
</aside>

<h1 id="parceiros-api-pesquisa-parceiros">Pesquisa Parceiros</h1>

## buscar_cnpj_parceiro_search__cnpj__get

<a id="opIdbuscar_cnpj_parceiro_search__cnpj__get"></a>

> Code samples

```python
import requests
headers = {
  'Accept': 'application/json'
}

r = requests.get('/search/{cnpj}', headers = headers)

print(r.json())

```

`GET /search/{cnpj}`

*Buscar parceiro por CNPJ*

Recupera as informações do parceiro com o CNPJ fornecido.

<h3 id="buscar_cnpj_parceiro_search__cnpj__get-parameters">Parameters</h3>

|Name|In|Type|Required|Description|
|---|---|---|---|---|
|cnpj|path|string|true|none|

> Example responses

> 200 Response

```json
{
  "razao_social": "Empresa razao social",
  "nome_fantasia": "Empresa exemplo",
  "telefone": "(12) 3456-7890",
  "email": "exemplo@email.com",
  "cep": "12345-678",
  "cnpj": "01.234.567/8912-34",
  "id_parceiro": "hash uuid",
  "zip_code_info": {
    "cep": "22783115",
    "bairro": "Centro",
    "localidade": "São Paulo",
    "uf": "SP",
    "last_update": "2019-08-24T14:15:22Z"
  },
  "last_update": "2019-08-24T14:15:22Z"
}
```

<h3 id="buscar_cnpj_parceiro_search__cnpj__get-responses">Responses</h3>

|Status|Meaning|Description|Schema|
|---|---|---|---|
|200|[OK](https://tools.ietf.org/html/rfc7231#section-6.3.1)|Successful Response|[PartnerSchema](#schemapartnerschema)|
|422|[Unprocessable Entity](https://tools.ietf.org/html/rfc2518#section-10.3)|Validation Error|[HTTPValidationError](#schemahttpvalidationerror)|

<aside class="success">
This operation does not require authentication
</aside>

## pesquisar_parceiros_search__get

<a id="opIdpesquisar_parceiros_search__get"></a>

> Code samples

```python
import requests
headers = {
  'Accept': 'application/json'
}

r = requests.get('/search/', params={
  'search_criteria': 'Empresa Exemplo'
}, headers = headers)

print(r.json())

```

`GET /search/`

*Pesquisar parceiros*

Realiza uma pesquisa nos parceiros com base nos critérios fornecidos, podendo buscar por qualquer informação presente nas colunas.

<h3 id="pesquisar_parceiros_search__get-parameters">Parameters</h3>

|Name|In|Type|Required|Description|
|---|---|---|---|---|
|search_criteria|query|string|true|none|
|skip|query|integer|false|none|
|limit|query|integer|false|none|

> Example responses

> 200 Response

```json
[
  {
    "razao_social": "Empresa razao social",
    "nome_fantasia": "Empresa exemplo",
    "telefone": "(12) 3456-7890",
    "email": "exemplo@email.com",
    "cep": "12345-678",
    "cnpj": "01.234.567/8912-34",
    "id_parceiro": "hash uuid",
    "zip_code_info": {
      "cep": "22783115",
      "bairro": "Centro",
      "localidade": "São Paulo",
      "uf": "SP",
      "last_update": "2019-08-24T14:15:22Z"
    },
    "last_update": "2019-08-24T14:15:22Z"
  }
]
```

<h3 id="pesquisar_parceiros_search__get-responses">Responses</h3>

|Status|Meaning|Description|Schema|
|---|---|---|---|
|200|[OK](https://tools.ietf.org/html/rfc7231#section-6.3.1)|Successful Response|Inline|
|422|[Unprocessable Entity](https://tools.ietf.org/html/rfc2518#section-10.3)|Validation Error|[HTTPValidationError](#schemahttpvalidationerror)|

<h3 id="pesquisar_parceiros_search__get-responseschema">Response Schema</h3>

Status Code **200**

*Response Pesquisar Parceiros Search  Get*

|Name|Type|Required|Restrictions|Description|
|---|---|---|---|---|
|Response Pesquisar Parceiros Search  Get|[[PartnerSchema](#schemapartnerschema)]|false|none|none|
|» PartnerSchema|[PartnerSchema](#schemapartnerschema)|false|none|none|
|»» razao_social|string|false|none|none|
|»» nome_fantasia|string|false|none|none|
|»» telefone|string|false|none|none|
|»» email|string|false|none|none|
|»» cep|string|true|none|none|
|»» cnpj|string|true|none|none|
|»» id_parceiro|string|true|none|none|
|»» zip_code_info|[ZipCodeSchema](#schemazipcodeschema)|true|none|none|
|»»» cep|string|true|none|none|
|»»» bairro|string|true|none|none|
|»»» localidade|string|true|none|none|
|»»» uf|string|true|none|none|
|»»» last_update|string(date-time)|true|none|none|
|»» last_update|string(date-time)|true|none|none|

<aside class="success">
This operation does not require authentication
</aside>

<h1 id="parceiros-api-upload-parceiros">Upload Parceiros</h1>

## carregar_parceiros_upload_partners__post

<a id="opIdcarregar_parceiros_upload_partners__post"></a>

> Code samples

```python
import requests
headers = {
  'Content-Type': 'multipart/form-data',
  'Accept': 'application/json'
}

r = requests.post('/upload/partners/', headers = headers)

print(r.json())

```

`POST /upload/partners/`

*Carregar parceiros via CSV*

Carregar parceiros a partir de um arquivo CSV enviado. O arquivo deve ter o seguinte formato: CNPJ, Nome, E-mail e Telefone.Exemplo de conteúdo CSV:

CNPJ, Razão Social, Nome Fantasia, Telefone, Email, CEP 
12.345.678/9123-45,Sol Eterno,Sol Eterno LTDA,(21) 98207-9901,teste@test.com,22783-115

> Body parameter

```yaml
file: string

```

<h3 id="carregar_parceiros_upload_partners__post-parameters">Parameters</h3>

|Name|In|Type|Required|Description|
|---|---|---|---|---|
|body|body|[Body_carregar_parceiros_upload_partners__post](#schemabody_carregar_parceiros_upload_partners__post)|true|none|

> Example responses

> 200 Response

```json
null
```

<h3 id="carregar_parceiros_upload_partners__post-responses">Responses</h3>

|Status|Meaning|Description|Schema|
|---|---|---|---|
|200|[OK](https://tools.ietf.org/html/rfc7231#section-6.3.1)|Successful Response|Inline|
|422|[Unprocessable Entity](https://tools.ietf.org/html/rfc2518#section-10.3)|Validation Error|[HTTPValidationError](#schemahttpvalidationerror)|

<h3 id="carregar_parceiros_upload_partners__post-responseschema">Response Schema</h3>

<aside class="success">
This operation does not require authentication
</aside>

# Schemas

<h2 id="tocS_Body_carregar_parceiros_upload_partners__post">Body_carregar_parceiros_upload_partners__post</h2>
<!-- backwards compatibility -->
<a id="schemabody_carregar_parceiros_upload_partners__post"></a>
<a id="schema_Body_carregar_parceiros_upload_partners__post"></a>
<a id="tocSbody_carregar_parceiros_upload_partners__post"></a>
<a id="tocsbody_carregar_parceiros_upload_partners__post"></a>

```json
{
  "file": "string"
}

```

Body_carregar_parceiros_upload_partners__post

### Properties

|Name|Type|Required|Restrictions|Description|
|---|---|---|---|---|
|file|string(binary)|true|none|Arquivo CSV contendo os dados dos parceiros a serem carregados.|

<h2 id="tocS_HTTPValidationError">HTTPValidationError</h2>
<!-- backwards compatibility -->
<a id="schemahttpvalidationerror"></a>
<a id="schema_HTTPValidationError"></a>
<a id="tocShttpvalidationerror"></a>
<a id="tocshttpvalidationerror"></a>

```json
{
  "detail": [
    {
      "loc": [
        "string"
      ],
      "msg": "string",
      "type": "string"
    }
  ]
}

```

HTTPValidationError

### Properties

|Name|Type|Required|Restrictions|Description|
|---|---|---|---|---|
|detail|[[ValidationError](#schemavalidationerror)]|false|none|none|

<h2 id="tocS_PartnerJsonSchema">PartnerJsonSchema</h2>
<!-- backwards compatibility -->
<a id="schemapartnerjsonschema"></a>
<a id="schema_PartnerJsonSchema"></a>
<a id="tocSpartnerjsonschema"></a>
<a id="tocspartnerjsonschema"></a>

```json
{
  "razao_social": "Empresa razao social",
  "nome_fantasia": "Empresa exemplo",
  "telefone": "(12) 3456-7890",
  "email": "exemplo@email.com",
  "cep": "12345-678",
  "cnpj": "01.234.567/8912-34"
}

```

PartnerJsonSchema

### Properties

|Name|Type|Required|Restrictions|Description|
|---|---|---|---|---|
|razao_social|string|false|none|none|
|nome_fantasia|string|false|none|none|
|telefone|string|false|none|none|
|email|string|false|none|none|
|cep|string|true|none|none|
|cnpj|string|true|none|none|

<h2 id="tocS_PartnerSchema">PartnerSchema</h2>
<!-- backwards compatibility -->
<a id="schemapartnerschema"></a>
<a id="schema_PartnerSchema"></a>
<a id="tocSpartnerschema"></a>
<a id="tocspartnerschema"></a>

```json
{
  "razao_social": "Empresa razao social",
  "nome_fantasia": "Empresa exemplo",
  "telefone": "(12) 3456-7890",
  "email": "exemplo@email.com",
  "cep": "12345-678",
  "cnpj": "01.234.567/8912-34",
  "id_parceiro": "hash uuid",
  "zip_code_info": {
    "cep": "22783115",
    "bairro": "Centro",
    "localidade": "São Paulo",
    "uf": "SP",
    "last_update": "2019-08-24T14:15:22Z"
  },
  "last_update": "2019-08-24T14:15:22Z"
}

```

PartnerSchema

### Properties

|Name|Type|Required|Restrictions|Description|
|---|---|---|---|---|
|razao_social|string|false|none|none|
|nome_fantasia|string|false|none|none|
|telefone|string|false|none|none|
|email|string|false|none|none|
|cep|string|true|none|none|
|cnpj|string|true|none|none|
|id_parceiro|string|true|none|none|
|zip_code_info|[ZipCodeSchema](#schemazipcodeschema)|true|none|none|
|last_update|string(date-time)|true|none|none|

<h2 id="tocS_PartnerUpdateSchema">PartnerUpdateSchema</h2>
<!-- backwards compatibility -->
<a id="schemapartnerupdateschema"></a>
<a id="schema_PartnerUpdateSchema"></a>
<a id="tocSpartnerupdateschema"></a>
<a id="tocspartnerupdateschema"></a>

```json
{
  "razao_social": "Empresa razao social",
  "nome_fantasia": "Empresa exemplo",
  "telefone": "(12) 3456-7890",
  "email": "exemplo@email.com",
  "cep": "string"
}

```

PartnerUpdateSchema

### Properties

|Name|Type|Required|Restrictions|Description|
|---|---|---|---|---|
|razao_social|string|false|none|none|
|nome_fantasia|string|false|none|none|
|telefone|string|false|none|none|
|email|string|false|none|none|
|cep|string|false|none|none|

<h2 id="tocS_ValidationError">ValidationError</h2>
<!-- backwards compatibility -->
<a id="schemavalidationerror"></a>
<a id="schema_ValidationError"></a>
<a id="tocSvalidationerror"></a>
<a id="tocsvalidationerror"></a>

```json
{
  "loc": [
    "string"
  ],
  "msg": "string",
  "type": "string"
}

```

ValidationError

### Properties

|Name|Type|Required|Restrictions|Description|
|---|---|---|---|---|
|loc|[anyOf]|true|none|none|

anyOf

|Name|Type|Required|Restrictions|Description|
|---|---|---|---|---|
|» *anonymous*|string|false|none|none|

or

|Name|Type|Required|Restrictions|Description|
|---|---|---|---|---|
|» *anonymous*|integer|false|none|none|

continued

|Name|Type|Required|Restrictions|Description|
|---|---|---|---|---|
|msg|string|true|none|none|
|type|string|true|none|none|

<h2 id="tocS_ZipCodeSchema">ZipCodeSchema</h2>
<!-- backwards compatibility -->
<a id="schemazipcodeschema"></a>
<a id="schema_ZipCodeSchema"></a>
<a id="tocSzipcodeschema"></a>
<a id="tocszipcodeschema"></a>

```json
{
  "cep": "22783115",
  "bairro": "Centro",
  "localidade": "São Paulo",
  "uf": "SP",
  "last_update": "2019-08-24T14:15:22Z"
}

```

ZipCodeSchema

### Properties

|Name|Type|Required|Restrictions|Description|
|---|---|---|---|---|
|cep|string|true|none|none|
|bairro|string|true|none|none|
|localidade|string|true|none|none|
|uf|string|true|none|none|
|last_update|string(date-time)|true|none|none|

