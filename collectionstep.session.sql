create database CollectionStep;

use CollectionStep;

CREATE TABLE usuarios (
    id_usuario int PRIMARY KEY,
    nome_usuario varchar(100),
    telefone_usuario varchar(20),
    email_usuario varchar(100),
    senha_usuario varchar(50),
    rua_usu varchar(100),
    complemento_usu varchar(100),
    fk_produtos_id_produto int
);

CREATE TABLE postos (
    id_posto int PRIMARY KEY,
    cpf_fun varchar(20),
    telefone_fun varchar(20),
    endereco_fun varchar(100),
    rua_posto varchar(100),
    complemento_posto varchar(100),
    telefone_posto bigint,
    horario_posto varchar(100)
);

CREATE TABLE produtos (
    rastreio_pedido varchar(50),
    id_produto int PRIMARY KEY,
    datareceb_prod varchar(20),
    tipo_prod varchar(50),
    desc_prod varchar(255),
    tamanho_prod boolean,
    status_prod boolean
);

ALTER TABLE usuarios 
ADD CONSTRAINT fk_usuarios_produtos 
FOREIGN KEY (fk_produtos_id_produto) 
REFERENCES produtos (id_produto) 
ON DELETE RESTRICT;
