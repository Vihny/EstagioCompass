-- Passo a passo da Normalização
-- Primeiramente, comecei criando a tabela Cliente com idCliente como chave e incluí os atributos nomeCliente, cidadeCliente, estadoCliente e paisCliente nessa tabela.
-- Ademais, criei a tabela Carros onde a chave primária ficou sendo o idCarro e nessa tabela icluí o kmCarro, classiCarro, marcaCarro, modeloCarro,anocarro e teve como chave estrangeira idCombustivel.
-- Logo após, criei a tabela Combustivel que teve cheve primária idCombustivel e o atributo tipoCombustivel.
-- Depois criei a tabela Vendedor que teve isVendedor como chave primária e incluí nomeVendedor, sexovendedor, estadoVendedor nessa tabela.
-- Por último, criei a tabela Locacao que tem como chave primária o idLocação, tem como chave estrangeira o idCliente, idCarro e o idVendedor, tem como outros atributos a dataLocação, horaLocação, qtdDiaria, vlrDiaria, dataEntrega e horaEntrega.


CREATE TABLE Cliente (
    idCliente INT PRIMARY KEY,
    nomeCliente VARCHAR(100),
    cidadeCliente VARCHAR(40),
    estadoCliente VARCHAR(40),
    paisCliente VARCHAR(40)
);

INSERT OR IGNORE INTO Cliente (idCliente, nomeCliente, cidadeCliente, estadoCliente, paisCliente)
SELECT DISTINCT idCliente, nomeCliente, cidadeCliente, estadoCliente, paisCliente
FROM tb_locacao;

CREATE TABLE Carro (
    idCarro INT PRIMARY KEY,
    idcombustivel,
    kmCarro INT,
    classiCarro VARCHAR(50),
    marcaCarro VARCHAR(80),
    modeloCarro VARCHAR(80),
    anoCarro INT,
    FOREIGN KEY (idcombustivel) REFERENCES Combustivel(idcombustivel)
);

INSERT OR IGNORE INTO Carro (idCarro,idcombustivel, kmCarro, classiCarro, marcaCarro, modeloCarro, anoCarro)
SELECT DISTINCT idCarro,idcombustivel, kmCarro, classiCarro, marcaCarro, modeloCarro, anoCarro
FROM tb_locacao;

CREATE TABLE Combustivel (
    idcombustivel INT PRIMARY KEY,
    tipoCombustivel VARCHAR(20)
);

INSERT OR IGNORE INTO Combustivel (idcombustivel, tipoCombustivel)
SELECT DISTINCT idcombustivel, tipoCombustivel
FROM tb_locacao;

CREATE TABLE Vendedor (
    idVendedor INT PRIMARY KEY,
    nomeVendedor VARCHAR(15),
    sexoVendedor SMALLINT,
    estadoVendedor VARCHAR(40)
);

INSERT OR IGNORE INTO Vendedor (idVendedor, nomeVendedor, sexoVendedor, estadoVendedor)
SELECT DISTINCT idVendedor, nomeVendedor, sexoVendedor, estadoVendedor
FROM tb_locacao;

CREATE TABLE Locacao (
    idLocacao INT PRIMARY KEY,
    idCliente INT,
    idCarro INT,
    idVendedor INT,
    dataLocacao DATETIME,
    horaLocacao TIME,
    qtdDiaria INT,
    vlrDiaria DECIMAL(18,2),
    dataEntrega DATE,
    horaEntrega TIME,
    FOREIGN KEY (idCliente) REFERENCES Cliente(idCliente),
    FOREIGN KEY (idCarro) REFERENCES Carro(idCarro),
    FOREIGN KEY (idVendedor) REFERENCES Vendedor(idVendedor)
);

INSERT OR IGNORE INTO Locacao (idLocacao, idCliente, idCarro, idVendedor, dataLocacao, horaLocacao, qtdDiaria, vlrDiaria, dataEntrega, horaEntrega)
SELECT DISTINCT idLocacao, idCliente, idCarro, idVendedor, dataLocacao, horaLocacao, qtdDiaria, vlrDiaria, dataEntrega, horaEntrega
FROM tb_locacao;