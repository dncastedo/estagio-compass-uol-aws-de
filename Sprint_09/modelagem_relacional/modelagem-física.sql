-- Tabela locação já está na 1FN, uma vez que não possui atributos multivalorados ou compostos
-- 2FN - A tabela locação possui chave primária composta, foram criadas novas tabelas (tb_cliente, tb_carro, tb_vendedor) 
-- para armazenar os atributos que não estão diretamente ligados a chave primária idLocação
-- 3FN - Identificado o atributo não-chave que depende de outro atributo não-chave foi excluído o id_combustivel e passado tipoCombustivel diretamente
-- para a tabela tb_carros.
-- Criadas as chaves estrangeiras para acesso dos dados na tabela principal tb_locacao_carros

SELECT * FROM tb_locacao

UPDATE tb_locacao
SET dataLocacao = 
    substr(dataLocacao, 1, 4) || '-' ||
    substr(dataLocacao, 5, 2) || '-' ||
    substr(dataLocacao, 7, 2);

UPDATE tb_locacao
SET dataEntrega = 
    substr(dataEntrega, 1, 4) || '-' ||
    substr(dataEntrega, 5, 2) || '-' ||
    substr(dataEntrega, 7, 2);

CREATE TABLE tb_cliente(
	idCliente INT PRIMARY KEY,
	nomeCliente VARCHAR(100),
	cidadeCliente VARCHAR (100),
	estadoCliente VARCHAR (100),
	paisCliente VARCHAR(100)
);

CREATE VIEW view_cliente AS
SELECT
    idCliente,
    nomeCliente,
    cidadeCliente,
    estadoCliente,
    paisCliente
FROM
    tb_locacao
GROUP BY
    idCliente;

INSERT INTO tb_cliente (idCliente, nomeCliente, cidadeCliente, estadoCliente, paisCliente)
SELECT idCliente, nomeCliente, cidadeCliente, estadoCliente, paisCliente
FROM view_cliente;

CREATE TABLE tb_carro(
	idCarro INT PRIMARY KEY,
	kmCarro INT,
	chassiCarro VARCHAR (50),
	marcaCarro VARCHAR (50),
	modeloCarro VARCHAR (50),
	anoCarro INT,
    tipoCombustivel VARCHAR(50)
);

CREATE VIEW view_carro AS
SELECT
    idCarro,
    kmCarro,
    classiCarro,
    marcaCarro,
    modeloCarro,
    anoCarro,
    tipoCombustivel
FROM
    tb_locacao
GROUP BY
    idCarro;

INSERT INTO tb_carro (idCarro, kmCarro, chassiCarro, marcaCarro, modeloCarro, anoCarro, tipoCombustivel)
SELECT idCarro, kmCarro, classiCarro, marcaCarro, modeloCarro, anoCarro, tipoCombustivel
FROM view_carro;


CREATE TABLE tb_vendedor(
	idVendedor INT PRIMARY KEY,
	nomeVendedor VARCHAR (100),
	sexoVendedor SMALLINT,
	estadoVendedor VARCHAR (50)
);

CREATE VIEW view_vendedor AS
SELECT
    idVendedor,
    nomeVendedor,
    sexoVendedor,
    estadoVendedor 
FROM
    tb_locacao
GROUP BY
    idVendedor;

INSERT INTO tb_vendedor (idVendedor, nomeVendedor, sexoVendedor, estadoVendedor)
SELECT idVendedor, nomeVendedor, sexoVendedor, estadoVendedor
FROM view_vendedor;


CREATE TABLE tb_locacao_carros (
    idLocacao INT PRIMARY KEY,
    dataLocacao DATE,
    horaLocacao TIME,
    qtdDiaria INT,
    vlrDiaria DECIMAL,
    dataEntrega DATE,
    horaEntrega TIME,
    idCliente INT,
    idCarro INT,
    idVendedor INT,
    FOREIGN KEY (idCliente) REFERENCES tb_cliente (idCliente),
    FOREIGN KEY (idCarro) REFERENCES tb_carro (idCarro),
    FOREIGN KEY (idVendedor) REFERENCES tb_vendedor (idVendedor)
);


INSERT INTO tb_locacao_carros (idLocacao, dataLocacao, horaLocacao, qtdDiaria, vlrDiaria, dataEntrega,
								horaEntrega, idCliente, idCarro, idVendedor)
SELECT idLocacao, dataLocacao, horaLocacao, qtdDiaria, vlrDiaria, dataEntrega, 
		horaEntrega, idCliente, idCarro, idVendedor
FROM tb_locacao;


DROP TABLE tb_locacao;



