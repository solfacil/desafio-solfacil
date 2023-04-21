---
title: Your API Title v1.0.0
language_tabs:
  - shell: Shell
  - http: HTTP
  - javascript: JavaScript
  - ruby: Ruby
  - python: Python
  - php: PHP
  - java: Java
  - go: Go
toc_footers: []
includes: []
search: true
highlight_theme: darkula
headingLevel: 2

---

<!-- Generator: Widdershins v4.0.1 -->

<h1 id="your-api-title">Your API Title v1.0.0</h1>

> Scroll down for code samples, example requests and responses. Select a language for code samples from the tabs above or the mobile navigation menu.

Your API Description

<h1 id="your-api-title-padr-es">Padrões</h1>

## favicon_favicon_ico_get

<a id="opIdfavicon_favicon_ico_get"></a>

> Code samples

```shell
# You can also use wget
curl -X GET /favicon.ico \
  -H 'Accept: application/json'

```

```http
GET /favicon.ico HTTP/1.1

Accept: application/json

```

```javascript

const headers = {
  'Accept':'application/json'
};

fetch('/favicon.ico',
{
  method: 'GET',

  headers: headers
})
.then(function(res) {
    return res.json();
}).then(function(body) {
    console.log(body);
});

```

```ruby
require 'rest-client'
require 'json'

headers = {
  'Accept' => 'application/json'
}

result = RestClient.get '/favicon.ico',
  params: {
  }, headers: headers

p JSON.parse(result)

```

```python
import requests
headers = {
  'Accept': 'application/json'
}

r = requests.get('/favicon.ico', headers = headers)

print(r.json())

```

```php
<?php

require 'vendor/autoload.php';

$headers = array(
    'Accept' => 'application/json',
);

$client = new \GuzzleHttp\Client();

// Define array of request body.
$request_body = array();

try {
    $response = $client->request('GET','/favicon.ico', array(
        'headers' => $headers,
        'json' => $request_body,
       )
    );
    print_r($response->getBody()->getContents());
 }
 catch (\GuzzleHttp\Exception\BadResponseException $e) {
    // handle exception or api errors.
    print_r($e->getMessage());
 }

 // ...

```

```java
URL obj = new URL("/favicon.ico");
HttpURLConnection con = (HttpURLConnection) obj.openConnection();
con.setRequestMethod("GET");
int responseCode = con.getResponseCode();
BufferedReader in = new BufferedReader(
    new InputStreamReader(con.getInputStream()));
String inputLine;
StringBuffer response = new StringBuffer();
while ((inputLine = in.readLine()) != null) {
    response.append(inputLine);
}
in.close();
System.out.println(response.toString());

```

```go
package main

import (
       "bytes"
       "net/http"
)

func main() {

    headers := map[string][]string{
        "Accept": []string{"application/json"},
    }

    data := bytes.NewBuffer([]byte{jsonReq})
    req, err := http.NewRequest("GET", "/favicon.ico", data)
    req.Header = headers

    client := &http.Client{}
    resp, err := client.Do(req)
    // ...
}

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

```shell
# You can also use wget
curl -X GET / \
  -H 'Accept: application/json'

```

```http
GET / HTTP/1.1

Accept: application/json

```

```javascript

const headers = {
  'Accept':'application/json'
};

fetch('/',
{
  method: 'GET',

  headers: headers
})
.then(function(res) {
    return res.json();
}).then(function(body) {
    console.log(body);
});

```

```ruby
require 'rest-client'
require 'json'

headers = {
  'Accept' => 'application/json'
}

result = RestClient.get '/',
  params: {
  }, headers: headers

p JSON.parse(result)

```

```python
import requests
headers = {
  'Accept': 'application/json'
}

r = requests.get('/', headers = headers)

print(r.json())

```

```php
<?php

require 'vendor/autoload.php';

$headers = array(
    'Accept' => 'application/json',
);

$client = new \GuzzleHttp\Client();

// Define array of request body.
$request_body = array();

try {
    $response = $client->request('GET','/', array(
        'headers' => $headers,
        'json' => $request_body,
       )
    );
    print_r($response->getBody()->getContents());
 }
 catch (\GuzzleHttp\Exception\BadResponseException $e) {
    // handle exception or api errors.
    print_r($e->getMessage());
 }

 // ...

```

```java
URL obj = new URL("/");
HttpURLConnection con = (HttpURLConnection) obj.openConnection();
con.setRequestMethod("GET");
int responseCode = con.getResponseCode();
BufferedReader in = new BufferedReader(
    new InputStreamReader(con.getInputStream()));
String inputLine;
StringBuffer response = new StringBuffer();
while ((inputLine = in.readLine()) != null) {
    response.append(inputLine);
}
in.close();
System.out.println(response.toString());

```

```go
package main

import (
       "bytes"
       "net/http"
)

func main() {

    headers := map[string][]string{
        "Accept": []string{"application/json"},
    }

    data := bytes.NewBuffer([]byte{jsonReq})
    req, err := http.NewRequest("GET", "/", data)
    req.Header = headers

    client := &http.Client{}
    resp, err := client.Do(req)
    // ...
}

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

<h1 id="your-api-title-crud-parceiros">Crud Parceiros</h1>

## listar_parceiros_parceiros__get

<a id="opIdlistar_parceiros_parceiros__get"></a>

> Code samples

```shell
# You can also use wget
curl -X GET /parceiros/ \
  -H 'Accept: application/json'

```

```http
GET /parceiros/ HTTP/1.1

Accept: application/json

```

```javascript

const headers = {
  'Accept':'application/json'
};

fetch('/parceiros/',
{
  method: 'GET',

  headers: headers
})
.then(function(res) {
    return res.json();
}).then(function(body) {
    console.log(body);
});

```

```ruby
require 'rest-client'
require 'json'

headers = {
  'Accept' => 'application/json'
}

result = RestClient.get '/parceiros/',
  params: {
  }, headers: headers

p JSON.parse(result)

```

```python
import requests
headers = {
  'Accept': 'application/json'
}

r = requests.get('/parceiros/', headers = headers)

print(r.json())

```

```php
<?php

require 'vendor/autoload.php';

$headers = array(
    'Accept' => 'application/json',
);

$client = new \GuzzleHttp\Client();

// Define array of request body.
$request_body = array();

try {
    $response = $client->request('GET','/parceiros/', array(
        'headers' => $headers,
        'json' => $request_body,
       )
    );
    print_r($response->getBody()->getContents());
 }
 catch (\GuzzleHttp\Exception\BadResponseException $e) {
    // handle exception or api errors.
    print_r($e->getMessage());
 }

 // ...

```

```java
URL obj = new URL("/parceiros/");
HttpURLConnection con = (HttpURLConnection) obj.openConnection();
con.setRequestMethod("GET");
int responseCode = con.getResponseCode();
BufferedReader in = new BufferedReader(
    new InputStreamReader(con.getInputStream()));
String inputLine;
StringBuffer response = new StringBuffer();
while ((inputLine = in.readLine()) != null) {
    response.append(inputLine);
}
in.close();
System.out.println(response.toString());

```

```go
package main

import (
       "bytes"
       "net/http"
)

func main() {

    headers := map[string][]string{
        "Accept": []string{"application/json"},
    }

    data := bytes.NewBuffer([]byte{jsonReq})
    req, err := http.NewRequest("GET", "/parceiros/", data)
    req.Header = headers

    client := &http.Client{}
    resp, err := client.Do(req)
    // ...
}

```

`GET /parceiros/`

*Listar Parceiros*

<h3 id="listar_parceiros_parceiros__get-parameters">Parameters</h3>

|Name|In|Type|Required|Description|
|---|---|---|---|---|
|skip|query|integer|false|none|
|limit|query|integer|false|none|

> Example responses

> 200 Response

```json
[
  {
    "razao_social": "string",
    "nome_fantasia": "string",
    "telefone": "string",
    "email": "string",
    "cep": "string",
    "cnpj": "string",
    "id_parceiro": "string",
    "cep_info": {
      "cep": "string",
      "bairro": "string",
      "localidade": "string",
      "uf": "string",
      "data_atualizacao": "2019-08-24T14:15:22Z"
    },
    "data_atualizacao": "2019-08-24T14:15:22Z"
  }
]
```

<h3 id="listar_parceiros_parceiros__get-responses">Responses</h3>

|Status|Meaning|Description|Schema|
|---|---|---|---|
|200|[OK](https://tools.ietf.org/html/rfc7231#section-6.3.1)|Successful Response|Inline|
|422|[Unprocessable Entity](https://tools.ietf.org/html/rfc2518#section-10.3)|Validation Error|[HTTPValidationError](#schemahttpvalidationerror)|

<h3 id="listar_parceiros_parceiros__get-responseschema">Response Schema</h3>

Status Code **200**

*Response Listar Parceiros Parceiros  Get*

|Name|Type|Required|Restrictions|Description|
|---|---|---|---|---|
|Response Listar Parceiros Parceiros  Get|[[SchemaParceiro](#schemaschemaparceiro)]|false|none|none|
|» SchemaParceiro|[SchemaParceiro](#schemaschemaparceiro)|false|none|none|
|»» razao_social|string|false|none|none|
|»» nome_fantasia|string|false|none|none|
|»» telefone|string|false|none|none|
|»» email|string|false|none|none|
|»» cep|string|true|none|none|
|»» cnpj|string|true|none|none|
|»» id_parceiro|string|true|none|none|
|»» cep_info|[SchemaCepInfo](#schemaschemacepinfo)|true|none|none|
|»»» cep|string|true|none|none|
|»»» bairro|string|true|none|none|
|»»» localidade|string|true|none|none|
|»»» uf|string|true|none|none|
|»»» data_atualizacao|string(date-time)|true|none|none|
|»» data_atualizacao|string(date-time)|true|none|none|

<aside class="success">
This operation does not require authentication
</aside>

## criar_parceiro_parceiros__post

<a id="opIdcriar_parceiro_parceiros__post"></a>

> Code samples

```shell
# You can also use wget
curl -X POST /parceiros/ \
  -H 'Content-Type: application/json' \
  -H 'Accept: application/json'

```

```http
POST /parceiros/ HTTP/1.1

Content-Type: application/json
Accept: application/json

```

```javascript
const inputBody = '{
  "razao_social": "string",
  "nome_fantasia": "string",
  "telefone": "string",
  "email": "string",
  "cep": "string",
  "cnpj": "string"
}';
const headers = {
  'Content-Type':'application/json',
  'Accept':'application/json'
};

fetch('/parceiros/',
{
  method: 'POST',
  body: inputBody,
  headers: headers
})
.then(function(res) {
    return res.json();
}).then(function(body) {
    console.log(body);
});

```

```ruby
require 'rest-client'
require 'json'

headers = {
  'Content-Type' => 'application/json',
  'Accept' => 'application/json'
}

result = RestClient.post '/parceiros/',
  params: {
  }, headers: headers

p JSON.parse(result)

```

```python
import requests
headers = {
  'Content-Type': 'application/json',
  'Accept': 'application/json'
}

r = requests.post('/parceiros/', headers = headers)

print(r.json())

```

```php
<?php

require 'vendor/autoload.php';

$headers = array(
    'Content-Type' => 'application/json',
    'Accept' => 'application/json',
);

$client = new \GuzzleHttp\Client();

// Define array of request body.
$request_body = array();

try {
    $response = $client->request('POST','/parceiros/', array(
        'headers' => $headers,
        'json' => $request_body,
       )
    );
    print_r($response->getBody()->getContents());
 }
 catch (\GuzzleHttp\Exception\BadResponseException $e) {
    // handle exception or api errors.
    print_r($e->getMessage());
 }

 // ...

```

```java
URL obj = new URL("/parceiros/");
HttpURLConnection con = (HttpURLConnection) obj.openConnection();
con.setRequestMethod("POST");
int responseCode = con.getResponseCode();
BufferedReader in = new BufferedReader(
    new InputStreamReader(con.getInputStream()));
String inputLine;
StringBuffer response = new StringBuffer();
while ((inputLine = in.readLine()) != null) {
    response.append(inputLine);
}
in.close();
System.out.println(response.toString());

```

```go
package main

import (
       "bytes"
       "net/http"
)

func main() {

    headers := map[string][]string{
        "Content-Type": []string{"application/json"},
        "Accept": []string{"application/json"},
    }

    data := bytes.NewBuffer([]byte{jsonReq})
    req, err := http.NewRequest("POST", "/parceiros/", data)
    req.Header = headers

    client := &http.Client{}
    resp, err := client.Do(req)
    // ...
}

```

`POST /parceiros/`

*Criar Parceiro*

> Body parameter

```json
{
  "razao_social": "string",
  "nome_fantasia": "string",
  "telefone": "string",
  "email": "string",
  "cep": "string",
  "cnpj": "string"
}
```

<h3 id="criar_parceiro_parceiros__post-parameters">Parameters</h3>

|Name|In|Type|Required|Description|
|---|---|---|---|---|
|body|body|[SchemaJsonParceiro](#schemaschemajsonparceiro)|true|none|

> Example responses

> 201 Response

```json
{
  "razao_social": "string",
  "nome_fantasia": "string",
  "telefone": "string",
  "email": "string",
  "cep": "string",
  "cnpj": "string",
  "id_parceiro": "string",
  "cep_info": {
    "cep": "string",
    "bairro": "string",
    "localidade": "string",
    "uf": "string",
    "data_atualizacao": "2019-08-24T14:15:22Z"
  },
  "data_atualizacao": "2019-08-24T14:15:22Z"
}
```

<h3 id="criar_parceiro_parceiros__post-responses">Responses</h3>

|Status|Meaning|Description|Schema|
|---|---|---|---|
|201|[Created](https://tools.ietf.org/html/rfc7231#section-6.3.2)|Successful Response|[SchemaParceiro](#schemaschemaparceiro)|
|422|[Unprocessable Entity](https://tools.ietf.org/html/rfc2518#section-10.3)|Validation Error|[HTTPValidationError](#schemahttpvalidationerror)|

<aside class="success">
This operation does not require authentication
</aside>

## atualizar_parceiro_parceiros__cnpj__put

<a id="opIdatualizar_parceiro_parceiros__cnpj__put"></a>

> Code samples

```shell
# You can also use wget
curl -X PUT /parceiros/{cnpj} \
  -H 'Content-Type: application/json' \
  -H 'Accept: application/json'

```

```http
PUT /parceiros/{cnpj} HTTP/1.1

Content-Type: application/json
Accept: application/json

```

```javascript
const inputBody = '{
  "razao_social": "string",
  "nome_fantasia": "string",
  "telefone": "string",
  "email": "string",
  "cep": "string"
}';
const headers = {
  'Content-Type':'application/json',
  'Accept':'application/json'
};

fetch('/parceiros/{cnpj}',
{
  method: 'PUT',
  body: inputBody,
  headers: headers
})
.then(function(res) {
    return res.json();
}).then(function(body) {
    console.log(body);
});

```

```ruby
require 'rest-client'
require 'json'

headers = {
  'Content-Type' => 'application/json',
  'Accept' => 'application/json'
}

result = RestClient.put '/parceiros/{cnpj}',
  params: {
  }, headers: headers

p JSON.parse(result)

```

```python
import requests
headers = {
  'Content-Type': 'application/json',
  'Accept': 'application/json'
}

r = requests.put('/parceiros/{cnpj}', headers = headers)

print(r.json())

```

```php
<?php

require 'vendor/autoload.php';

$headers = array(
    'Content-Type' => 'application/json',
    'Accept' => 'application/json',
);

$client = new \GuzzleHttp\Client();

// Define array of request body.
$request_body = array();

try {
    $response = $client->request('PUT','/parceiros/{cnpj}', array(
        'headers' => $headers,
        'json' => $request_body,
       )
    );
    print_r($response->getBody()->getContents());
 }
 catch (\GuzzleHttp\Exception\BadResponseException $e) {
    // handle exception or api errors.
    print_r($e->getMessage());
 }

 // ...

```

```java
URL obj = new URL("/parceiros/{cnpj}");
HttpURLConnection con = (HttpURLConnection) obj.openConnection();
con.setRequestMethod("PUT");
int responseCode = con.getResponseCode();
BufferedReader in = new BufferedReader(
    new InputStreamReader(con.getInputStream()));
String inputLine;
StringBuffer response = new StringBuffer();
while ((inputLine = in.readLine()) != null) {
    response.append(inputLine);
}
in.close();
System.out.println(response.toString());

```

```go
package main

import (
       "bytes"
       "net/http"
)

func main() {

    headers := map[string][]string{
        "Content-Type": []string{"application/json"},
        "Accept": []string{"application/json"},
    }

    data := bytes.NewBuffer([]byte{jsonReq})
    req, err := http.NewRequest("PUT", "/parceiros/{cnpj}", data)
    req.Header = headers

    client := &http.Client{}
    resp, err := client.Do(req)
    // ...
}

```

`PUT /parceiros/{cnpj}`

*Atualizar Parceiro*

> Body parameter

```json
{
  "razao_social": "string",
  "nome_fantasia": "string",
  "telefone": "string",
  "email": "string",
  "cep": "string"
}
```

<h3 id="atualizar_parceiro_parceiros__cnpj__put-parameters">Parameters</h3>

|Name|In|Type|Required|Description|
|---|---|---|---|---|
|cnpj|path|string|true|none|
|body|body|[SchemaUpdateParceiro](#schemaschemaupdateparceiro)|true|none|

> Example responses

> 200 Response

```json
{
  "razao_social": "string",
  "nome_fantasia": "string",
  "telefone": "string",
  "email": "string",
  "cep": "string",
  "cnpj": "string",
  "id_parceiro": "string",
  "cep_info": {
    "cep": "string",
    "bairro": "string",
    "localidade": "string",
    "uf": "string",
    "data_atualizacao": "2019-08-24T14:15:22Z"
  },
  "data_atualizacao": "2019-08-24T14:15:22Z"
}
```

<h3 id="atualizar_parceiro_parceiros__cnpj__put-responses">Responses</h3>

|Status|Meaning|Description|Schema|
|---|---|---|---|
|200|[OK](https://tools.ietf.org/html/rfc7231#section-6.3.1)|Successful Response|[SchemaParceiro](#schemaschemaparceiro)|
|422|[Unprocessable Entity](https://tools.ietf.org/html/rfc2518#section-10.3)|Validation Error|[HTTPValidationError](#schemahttpvalidationerror)|

<aside class="success">
This operation does not require authentication
</aside>

## deletar_parceiro_parceiros__cnpj__delete

<a id="opIddeletar_parceiro_parceiros__cnpj__delete"></a>

> Code samples

```shell
# You can also use wget
curl -X DELETE /parceiros/{cnpj} \
  -H 'Accept: application/json'

```

```http
DELETE /parceiros/{cnpj} HTTP/1.1

Accept: application/json

```

```javascript

const headers = {
  'Accept':'application/json'
};

fetch('/parceiros/{cnpj}',
{
  method: 'DELETE',

  headers: headers
})
.then(function(res) {
    return res.json();
}).then(function(body) {
    console.log(body);
});

```

```ruby
require 'rest-client'
require 'json'

headers = {
  'Accept' => 'application/json'
}

result = RestClient.delete '/parceiros/{cnpj}',
  params: {
  }, headers: headers

p JSON.parse(result)

```

```python
import requests
headers = {
  'Accept': 'application/json'
}

r = requests.delete('/parceiros/{cnpj}', headers = headers)

print(r.json())

```

```php
<?php

require 'vendor/autoload.php';

$headers = array(
    'Accept' => 'application/json',
);

$client = new \GuzzleHttp\Client();

// Define array of request body.
$request_body = array();

try {
    $response = $client->request('DELETE','/parceiros/{cnpj}', array(
        'headers' => $headers,
        'json' => $request_body,
       )
    );
    print_r($response->getBody()->getContents());
 }
 catch (\GuzzleHttp\Exception\BadResponseException $e) {
    // handle exception or api errors.
    print_r($e->getMessage());
 }

 // ...

```

```java
URL obj = new URL("/parceiros/{cnpj}");
HttpURLConnection con = (HttpURLConnection) obj.openConnection();
con.setRequestMethod("DELETE");
int responseCode = con.getResponseCode();
BufferedReader in = new BufferedReader(
    new InputStreamReader(con.getInputStream()));
String inputLine;
StringBuffer response = new StringBuffer();
while ((inputLine = in.readLine()) != null) {
    response.append(inputLine);
}
in.close();
System.out.println(response.toString());

```

```go
package main

import (
       "bytes"
       "net/http"
)

func main() {

    headers := map[string][]string{
        "Accept": []string{"application/json"},
    }

    data := bytes.NewBuffer([]byte{jsonReq})
    req, err := http.NewRequest("DELETE", "/parceiros/{cnpj}", data)
    req.Header = headers

    client := &http.Client{}
    resp, err := client.Do(req)
    // ...
}

```

`DELETE /parceiros/{cnpj}`

*Deletar Parceiro*

<h3 id="deletar_parceiro_parceiros__cnpj__delete-parameters">Parameters</h3>

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

<h3 id="deletar_parceiro_parceiros__cnpj__delete-responses">Responses</h3>

|Status|Meaning|Description|Schema|
|---|---|---|---|
|204|[No Content](https://tools.ietf.org/html/rfc7231#section-6.3.5)|Successful Response|None|
|422|[Unprocessable Entity](https://tools.ietf.org/html/rfc2518#section-10.3)|Validation Error|[HTTPValidationError](#schemahttpvalidationerror)|

<aside class="success">
This operation does not require authentication
</aside>

<h1 id="your-api-title-pesquisa-parceiros">Pesquisa Parceiros</h1>

## buscar_cnpj_parceiro_buscar__cnpj__get

<a id="opIdbuscar_cnpj_parceiro_buscar__cnpj__get"></a>

> Code samples

```shell
# You can also use wget
curl -X GET /buscar/{cnpj} \
  -H 'Accept: application/json'

```

```http
GET /buscar/{cnpj} HTTP/1.1

Accept: application/json

```

```javascript

const headers = {
  'Accept':'application/json'
};

fetch('/buscar/{cnpj}',
{
  method: 'GET',

  headers: headers
})
.then(function(res) {
    return res.json();
}).then(function(body) {
    console.log(body);
});

```

```ruby
require 'rest-client'
require 'json'

headers = {
  'Accept' => 'application/json'
}

result = RestClient.get '/buscar/{cnpj}',
  params: {
  }, headers: headers

p JSON.parse(result)

```

```python
import requests
headers = {
  'Accept': 'application/json'
}

r = requests.get('/buscar/{cnpj}', headers = headers)

print(r.json())

```

```php
<?php

require 'vendor/autoload.php';

$headers = array(
    'Accept' => 'application/json',
);

$client = new \GuzzleHttp\Client();

// Define array of request body.
$request_body = array();

try {
    $response = $client->request('GET','/buscar/{cnpj}', array(
        'headers' => $headers,
        'json' => $request_body,
       )
    );
    print_r($response->getBody()->getContents());
 }
 catch (\GuzzleHttp\Exception\BadResponseException $e) {
    // handle exception or api errors.
    print_r($e->getMessage());
 }

 // ...

```

```java
URL obj = new URL("/buscar/{cnpj}");
HttpURLConnection con = (HttpURLConnection) obj.openConnection();
con.setRequestMethod("GET");
int responseCode = con.getResponseCode();
BufferedReader in = new BufferedReader(
    new InputStreamReader(con.getInputStream()));
String inputLine;
StringBuffer response = new StringBuffer();
while ((inputLine = in.readLine()) != null) {
    response.append(inputLine);
}
in.close();
System.out.println(response.toString());

```

```go
package main

import (
       "bytes"
       "net/http"
)

func main() {

    headers := map[string][]string{
        "Accept": []string{"application/json"},
    }

    data := bytes.NewBuffer([]byte{jsonReq})
    req, err := http.NewRequest("GET", "/buscar/{cnpj}", data)
    req.Header = headers

    client := &http.Client{}
    resp, err := client.Do(req)
    // ...
}

```

`GET /buscar/{cnpj}`

*Buscar Cnpj Parceiro*

<h3 id="buscar_cnpj_parceiro_buscar__cnpj__get-parameters">Parameters</h3>

|Name|In|Type|Required|Description|
|---|---|---|---|---|
|cnpj|path|string|true|none|

> Example responses

> 200 Response

```json
{
  "razao_social": "string",
  "nome_fantasia": "string",
  "telefone": "string",
  "email": "string",
  "cep": "string",
  "cnpj": "string",
  "id_parceiro": "string",
  "cep_info": {
    "cep": "string",
    "bairro": "string",
    "localidade": "string",
    "uf": "string",
    "data_atualizacao": "2019-08-24T14:15:22Z"
  },
  "data_atualizacao": "2019-08-24T14:15:22Z"
}
```

<h3 id="buscar_cnpj_parceiro_buscar__cnpj__get-responses">Responses</h3>

|Status|Meaning|Description|Schema|
|---|---|---|---|
|200|[OK](https://tools.ietf.org/html/rfc7231#section-6.3.1)|Successful Response|[SchemaParceiro](#schemaschemaparceiro)|
|422|[Unprocessable Entity](https://tools.ietf.org/html/rfc2518#section-10.3)|Validation Error|[HTTPValidationError](#schemahttpvalidationerror)|

<aside class="success">
This operation does not require authentication
</aside>

## pesquisar_parceiros_buscar__get

<a id="opIdpesquisar_parceiros_buscar__get"></a>

> Code samples

```shell
# You can also use wget
curl -X GET /buscar/?criterio=string \
  -H 'Accept: application/json'

```

```http
GET /buscar/?criterio=string HTTP/1.1

Accept: application/json

```

```javascript

const headers = {
  'Accept':'application/json'
};

fetch('/buscar/?criterio=string',
{
  method: 'GET',

  headers: headers
})
.then(function(res) {
    return res.json();
}).then(function(body) {
    console.log(body);
});

```

```ruby
require 'rest-client'
require 'json'

headers = {
  'Accept' => 'application/json'
}

result = RestClient.get '/buscar/',
  params: {
  'criterio' => 'string'
}, headers: headers

p JSON.parse(result)

```

```python
import requests
headers = {
  'Accept': 'application/json'
}

r = requests.get('/buscar/', params={
  'criterio': 'string'
}, headers = headers)

print(r.json())

```

```php
<?php

require 'vendor/autoload.php';

$headers = array(
    'Accept' => 'application/json',
);

$client = new \GuzzleHttp\Client();

// Define array of request body.
$request_body = array();

try {
    $response = $client->request('GET','/buscar/', array(
        'headers' => $headers,
        'json' => $request_body,
       )
    );
    print_r($response->getBody()->getContents());
 }
 catch (\GuzzleHttp\Exception\BadResponseException $e) {
    // handle exception or api errors.
    print_r($e->getMessage());
 }

 // ...

```

```java
URL obj = new URL("/buscar/?criterio=string");
HttpURLConnection con = (HttpURLConnection) obj.openConnection();
con.setRequestMethod("GET");
int responseCode = con.getResponseCode();
BufferedReader in = new BufferedReader(
    new InputStreamReader(con.getInputStream()));
String inputLine;
StringBuffer response = new StringBuffer();
while ((inputLine = in.readLine()) != null) {
    response.append(inputLine);
}
in.close();
System.out.println(response.toString());

```

```go
package main

import (
       "bytes"
       "net/http"
)

func main() {

    headers := map[string][]string{
        "Accept": []string{"application/json"},
    }

    data := bytes.NewBuffer([]byte{jsonReq})
    req, err := http.NewRequest("GET", "/buscar/", data)
    req.Header = headers

    client := &http.Client{}
    resp, err := client.Do(req)
    // ...
}

```

`GET /buscar/`

*Pesquisar Parceiros*

<h3 id="pesquisar_parceiros_buscar__get-parameters">Parameters</h3>

|Name|In|Type|Required|Description|
|---|---|---|---|---|
|criterio|query|string|true|none|
|skip|query|integer|false|none|
|limit|query|integer|false|none|

> Example responses

> 200 Response

```json
[
  {
    "razao_social": "string",
    "nome_fantasia": "string",
    "telefone": "string",
    "email": "string",
    "cep": "string",
    "cnpj": "string",
    "id_parceiro": "string",
    "cep_info": {
      "cep": "string",
      "bairro": "string",
      "localidade": "string",
      "uf": "string",
      "data_atualizacao": "2019-08-24T14:15:22Z"
    },
    "data_atualizacao": "2019-08-24T14:15:22Z"
  }
]
```

<h3 id="pesquisar_parceiros_buscar__get-responses">Responses</h3>

|Status|Meaning|Description|Schema|
|---|---|---|---|
|200|[OK](https://tools.ietf.org/html/rfc7231#section-6.3.1)|Successful Response|Inline|
|422|[Unprocessable Entity](https://tools.ietf.org/html/rfc2518#section-10.3)|Validation Error|[HTTPValidationError](#schemahttpvalidationerror)|

<h3 id="pesquisar_parceiros_buscar__get-responseschema">Response Schema</h3>

Status Code **200**

*Response Pesquisar Parceiros Buscar  Get*

|Name|Type|Required|Restrictions|Description|
|---|---|---|---|---|
|Response Pesquisar Parceiros Buscar  Get|[[SchemaParceiro](#schemaschemaparceiro)]|false|none|none|
|» SchemaParceiro|[SchemaParceiro](#schemaschemaparceiro)|false|none|none|
|»» razao_social|string|false|none|none|
|»» nome_fantasia|string|false|none|none|
|»» telefone|string|false|none|none|
|»» email|string|false|none|none|
|»» cep|string|true|none|none|
|»» cnpj|string|true|none|none|
|»» id_parceiro|string|true|none|none|
|»» cep_info|[SchemaCepInfo](#schemaschemacepinfo)|true|none|none|
|»»» cep|string|true|none|none|
|»»» bairro|string|true|none|none|
|»»» localidade|string|true|none|none|
|»»» uf|string|true|none|none|
|»»» data_atualizacao|string(date-time)|true|none|none|
|»» data_atualizacao|string(date-time)|true|none|none|

<aside class="success">
This operation does not require authentication
</aside>

<h1 id="your-api-title-upload-parceiros">Upload Parceiros</h1>

## upload_parceiros_upload_parceiros__post

<a id="opIdupload_parceiros_upload_parceiros__post"></a>

> Code samples

```shell
# You can also use wget
curl -X POST /upload/parceiros/ \
  -H 'Content-Type: multipart/form-data' \
  -H 'Accept: application/json'

```

```http
POST /upload/parceiros/ HTTP/1.1

Content-Type: multipart/form-data
Accept: application/json

```

```javascript
const inputBody = '{
  "file": "string"
}';
const headers = {
  'Content-Type':'multipart/form-data',
  'Accept':'application/json'
};

fetch('/upload/parceiros/',
{
  method: 'POST',
  body: inputBody,
  headers: headers
})
.then(function(res) {
    return res.json();
}).then(function(body) {
    console.log(body);
});

```

```ruby
require 'rest-client'
require 'json'

headers = {
  'Content-Type' => 'multipart/form-data',
  'Accept' => 'application/json'
}

result = RestClient.post '/upload/parceiros/',
  params: {
  }, headers: headers

p JSON.parse(result)

```

```python
import requests
headers = {
  'Content-Type': 'multipart/form-data',
  'Accept': 'application/json'
}

r = requests.post('/upload/parceiros/', headers = headers)

print(r.json())

```

```php
<?php

require 'vendor/autoload.php';

$headers = array(
    'Content-Type' => 'multipart/form-data',
    'Accept' => 'application/json',
);

$client = new \GuzzleHttp\Client();

// Define array of request body.
$request_body = array();

try {
    $response = $client->request('POST','/upload/parceiros/', array(
        'headers' => $headers,
        'json' => $request_body,
       )
    );
    print_r($response->getBody()->getContents());
 }
 catch (\GuzzleHttp\Exception\BadResponseException $e) {
    // handle exception or api errors.
    print_r($e->getMessage());
 }

 // ...

```

```java
URL obj = new URL("/upload/parceiros/");
HttpURLConnection con = (HttpURLConnection) obj.openConnection();
con.setRequestMethod("POST");
int responseCode = con.getResponseCode();
BufferedReader in = new BufferedReader(
    new InputStreamReader(con.getInputStream()));
String inputLine;
StringBuffer response = new StringBuffer();
while ((inputLine = in.readLine()) != null) {
    response.append(inputLine);
}
in.close();
System.out.println(response.toString());

```

```go
package main

import (
       "bytes"
       "net/http"
)

func main() {

    headers := map[string][]string{
        "Content-Type": []string{"multipart/form-data"},
        "Accept": []string{"application/json"},
    }

    data := bytes.NewBuffer([]byte{jsonReq})
    req, err := http.NewRequest("POST", "/upload/parceiros/", data)
    req.Header = headers

    client := &http.Client{}
    resp, err := client.Do(req)
    // ...
}

```

`POST /upload/parceiros/`

*Upload Parceiros*

> Body parameter

```yaml
file: string

```

<h3 id="upload_parceiros_upload_parceiros__post-parameters">Parameters</h3>

|Name|In|Type|Required|Description|
|---|---|---|---|---|
|body|body|[Body_upload_parceiros_upload_parceiros__post](#schemabody_upload_parceiros_upload_parceiros__post)|true|none|

> Example responses

> 200 Response

```json
null
```

<h3 id="upload_parceiros_upload_parceiros__post-responses">Responses</h3>

|Status|Meaning|Description|Schema|
|---|---|---|---|
|200|[OK](https://tools.ietf.org/html/rfc7231#section-6.3.1)|Successful Response|Inline|
|422|[Unprocessable Entity](https://tools.ietf.org/html/rfc2518#section-10.3)|Validation Error|[HTTPValidationError](#schemahttpvalidationerror)|

<h3 id="upload_parceiros_upload_parceiros__post-responseschema">Response Schema</h3>

<aside class="success">
This operation does not require authentication
</aside>

# Schemas

<h2 id="tocS_Body_upload_parceiros_upload_parceiros__post">Body_upload_parceiros_upload_parceiros__post</h2>
<!-- backwards compatibility -->
<a id="schemabody_upload_parceiros_upload_parceiros__post"></a>
<a id="schema_Body_upload_parceiros_upload_parceiros__post"></a>
<a id="tocSbody_upload_parceiros_upload_parceiros__post"></a>
<a id="tocsbody_upload_parceiros_upload_parceiros__post"></a>

```json
{
  "file": "string"
}

```

Body_upload_parceiros_upload_parceiros__post

### Properties

|Name|Type|Required|Restrictions|Description|
|---|---|---|---|---|
|file|string(binary)|true|none|none|

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

<h2 id="tocS_SchemaCepInfo">SchemaCepInfo</h2>
<!-- backwards compatibility -->
<a id="schemaschemacepinfo"></a>
<a id="schema_SchemaCepInfo"></a>
<a id="tocSschemacepinfo"></a>
<a id="tocsschemacepinfo"></a>

```json
{
  "cep": "string",
  "bairro": "string",
  "localidade": "string",
  "uf": "string",
  "data_atualizacao": "2019-08-24T14:15:22Z"
}

```

SchemaCepInfo

### Properties

|Name|Type|Required|Restrictions|Description|
|---|---|---|---|---|
|cep|string|true|none|none|
|bairro|string|true|none|none|
|localidade|string|true|none|none|
|uf|string|true|none|none|
|data_atualizacao|string(date-time)|true|none|none|

<h2 id="tocS_SchemaJsonParceiro">SchemaJsonParceiro</h2>
<!-- backwards compatibility -->
<a id="schemaschemajsonparceiro"></a>
<a id="schema_SchemaJsonParceiro"></a>
<a id="tocSschemajsonparceiro"></a>
<a id="tocsschemajsonparceiro"></a>

```json
{
  "razao_social": "string",
  "nome_fantasia": "string",
  "telefone": "string",
  "email": "string",
  "cep": "string",
  "cnpj": "string"
}

```

SchemaJsonParceiro

### Properties

|Name|Type|Required|Restrictions|Description|
|---|---|---|---|---|
|razao_social|string|false|none|none|
|nome_fantasia|string|false|none|none|
|telefone|string|false|none|none|
|email|string|false|none|none|
|cep|string|true|none|none|
|cnpj|string|true|none|none|

<h2 id="tocS_SchemaParceiro">SchemaParceiro</h2>
<!-- backwards compatibility -->
<a id="schemaschemaparceiro"></a>
<a id="schema_SchemaParceiro"></a>
<a id="tocSschemaparceiro"></a>
<a id="tocsschemaparceiro"></a>

```json
{
  "razao_social": "string",
  "nome_fantasia": "string",
  "telefone": "string",
  "email": "string",
  "cep": "string",
  "cnpj": "string",
  "id_parceiro": "string",
  "cep_info": {
    "cep": "string",
    "bairro": "string",
    "localidade": "string",
    "uf": "string",
    "data_atualizacao": "2019-08-24T14:15:22Z"
  },
  "data_atualizacao": "2019-08-24T14:15:22Z"
}

```

SchemaParceiro

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
|cep_info|[SchemaCepInfo](#schemaschemacepinfo)|true|none|none|
|data_atualizacao|string(date-time)|true|none|none|

<h2 id="tocS_SchemaUpdateParceiro">SchemaUpdateParceiro</h2>
<!-- backwards compatibility -->
<a id="schemaschemaupdateparceiro"></a>
<a id="schema_SchemaUpdateParceiro"></a>
<a id="tocSschemaupdateparceiro"></a>
<a id="tocsschemaupdateparceiro"></a>

```json
{
  "razao_social": "string",
  "nome_fantasia": "string",
  "telefone": "string",
  "email": "string",
  "cep": "string"
}

```

SchemaUpdateParceiro

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

