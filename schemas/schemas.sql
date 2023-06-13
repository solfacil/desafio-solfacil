CREATE DATABASE api;

\c api

CREATE table partners (
	id serial PRIMARY KEY,
	cnpj VARCHAR (14) UNIQUE,
	registered_name VARCHAR (100),
	fantasy_name VARCHAR (100),
	telephone VARCHAR (20),
	email VARCHAR (100),
	CEP VARCHAR (10),
	email_has_send boolean
);

CREATE table address (
	id serial PRIMARY KEY,
	CEP VARCHAR (10) UNIQUE,
	street VARCHAR(100),
	complement VARCHAR(100),
	district VARCHAR(100),
	city VARCHAR(100),
	uf VARCHAR(2),
	city_ibge VARCHAR(7)
);

\dt