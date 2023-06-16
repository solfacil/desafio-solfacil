CREATE TABLE parceiros.clientes (
	cliente_id INT UNSIGNED auto_increment NOT NULL,
	razao_social varchar(255) NOT NULL,
	nome_fantasia varchar(500) DEFAULT NULL NULL,
	telefone varchar(18) DEFAULT NULL NULL,
	email varchar(255) DEFAULT NULL NULL,
	cpf varchar(14) DEFAULT NULL NULL,
	cnpj varchar(18) DEFAULT NULL NULL,
	data_cadastro DATETIME DEFAULT CURRENT_TIMESTAMP NULL,
	data_alteracao DATETIME DEFAULT CURRENT_TIMESTAMP ON UPDATE CURRENT_TIMESTAMP NOT NULL,
	CONSTRAINT clientes_UN UNIQUE KEY (razao_social),
	CONSTRAINT clientes_PK PRIMARY KEY (cliente_id)
)
ENGINE=InnoDB
DEFAULT CHARSET=utf8mb3
COLLATE=utf8mb3_general_ci;

CREATE TABLE parceiros.enderecos (
	endereco_id INT UNSIGNED auto_increment NOT NULL,
    cliente_id INT UNSIGNED NOT NULL,
	cep varchar(9) NOT NULL,
	logradouro varchar(500) DEFAULT NULL NULL,
	complemento varchar(500) DEFAULT NULL NULL,
	bairro varchar(500) DEFAULT NULL NULL,
	localidade varchar(500) DEFAULT NULL NULL,
	uf varchar(2) DEFAULT NULL NULL,
	ibge INT DEFAULT NULL NULL,
	data_cadastro DATETIME DEFAULT CURRENT_TIMESTAMP NOT NULL,
	data_alteracao DATETIME DEFAULT CURRENT_TIMESTAMP ON UPDATE CURRENT_TIMESTAMP NOT NULL,
	CONSTRAINT enderecos_PK PRIMARY KEY (endereco_id),
	CONSTRAINT enderecos_FK FOREIGN KEY (cliente_id) REFERENCES parceiros.clientes(cliente_id) ON DELETE CASCADE
)
ENGINE=InnoDB
DEFAULT CHARSET=utf8mb3
COLLATE=utf8mb3_general_ci;