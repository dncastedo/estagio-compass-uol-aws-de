-- Criadas as tabelas dimensão (cliente, vendedor, carro e data)
-- Criada a tabela fato (locacao), passando os ids das outras tabelas para consulta


SELECT * FROM tb_cliente;
SELECT * FROM tb_carro;
SELECT * FROM tb_vendedor;
SELECT * FROM tb_locacao_carros;


ALTER TABLE tb_locacao_carros
ADD COLUMN idDataLocacaoEntrega INT;

CREATE TABLE dim_cliente(
	idCliente INT PRIMARY KEY,
	nomeCliente VARCHAR(100),
	cidadeCliente VARCHAR (100),
	estadoCliente VARCHAR (100),
	paisCliente VARCHAR(100)
);

CREATE VIEW view_tb_cliente AS
SELECT
    idCliente,
    nomeCliente,
    cidadeCliente,
    estadoCliente,
    paisCliente
FROM
    tb_cliente
GROUP BY
    idCliente;

INSERT INTO dim_cliente (idCliente, nomeCliente, cidadeCliente, estadoCliente, paisCliente)
SELECT idCliente, nomeCliente, cidadeCliente, estadoCliente, paisCliente
FROM view_tb_cliente;

CREATE TABLE dim_carro(
	idCarro INT PRIMARY KEY,
	kmCarro INT,
	chassiCarro VARCHAR (50),
	marcaCarro VARCHAR (50),
	modeloCarro VARCHAR (50),
	anoCarro INT,
	tipoCombustivel VARCHAR (50)
);

CREATE VIEW view_tb_carro AS
SELECT
    idCarro,
    kmCarro,
    chassiCarro,
    marcaCarro,
    modeloCarro,
    anoCarro,
    tipoCombustivel 
FROM
    tb_carro
GROUP BY
    idCarro;

INSERT INTO dim_carro (idCarro, kmCarro, chassiCarro, marcaCarro, modeloCarro, anoCarro, tipoCombustivel)
SELECT idCarro, kmCarro, chassiCarro, marcaCarro, modeloCarro, anoCarro, tipoCombustivel
FROM view_tb_carro;

CREATE TABLE dim_vendedor(
	idVendedor INT PRIMARY KEY,
	nomeVendedor VARCHAR (100),
	sexoVendedor SMALLINT,
	estadoVendedor VARCHAR (50)
);

CREATE VIEW view_tb_vendedor AS
SELECT
    idVendedor,
    nomeVendedor,
    sexoVendedor,
    estadoVendedor 
FROM
    tb_vendedor
GROUP BY
    idVendedor;

INSERT INTO dim_vendedor (idVendedor, nomeVendedor, sexoVendedor, estadoVendedor)
SELECT idVendedor, nomeVendedor, sexoVendedor, estadoVendedor
FROM view_tb_vendedor;

CREATE TABLE dim_dataLocacaoEntrega(
	idDataLocacaoEntrega INT PRIMARY KEY,
	dataLocacao DATE,
	horaLocacao TIME,
	dataEntrega DATE,
	horaEntrega TIME	
);


CREATE VIEW view_tb_locacao_carros_datas AS
SELECT
	idDataLocacaoEntrega,
    dataLocacao,
    horaLocacao,
    dataEntrega,
    horaEntrega
FROM tb_locacao_carros;

INSERT INTO dim_dataLocacaoEntrega (idDataLocacaoEntrega, dataLocacao, horaLocacao, dataEntrega, horaEntrega)
SELECT idDataLocacaoEntrega, dataLocacao, horaLocacao, dataEntrega, horaEntrega
FROM view_tb_locacao_carros_datas;

CREATE TABLE fato_locacao (
    idLocacao INT PRIMARY KEY,
    qtdDiaria INT,
    vlrDiaria DECIMAL,
    idCliente INT,
    idCarro INT,
    idVendedor INT,
    idDataLocacaoEntrega INT,
    FOREIGN KEY (idCliente) REFERENCES dim_cliente (idCliente),
    FOREIGN KEY (idCarro) REFERENCES dim_carro (idCarro),
    FOREIGN KEY (idVendedor) REFERENCES dim_vendedor (idVendedor),
    FOREIGN KEY (idDataLocacaoEntrega) REFERENCES dim_dataLocacaoEntrega (idDataLocacaoEntrega)
);


INSERT INTO fato_locacao (idDataLocacaoEntrega, idLocacao, qtdDiaria, vlrDiaria,idCliente, idCarro, idVendedor)
SELECT idDataLocacaoEntrega, idLocacao, qtdDiaria, vlrDiaria,idCliente, idCarro, idVendedor
FROM tb_locacao_carros;


DROP TABLE tb_locacao_carros;