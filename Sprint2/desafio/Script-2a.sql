CREATE VIEW Fato_Locacao AS
SELECT idLocacao, idCliente, idCarro, idVendedor, dataLocacao, horaLocacao, qtdDiaria, vlrDiaria, dataEntrega, horaEntrega
FROM Locacao;

CREATE VIEW Dim_Data AS
SELECT idLocacao, 
       DATETIME(dataLocacao) AS dataLocacao, 
       TIME(horaLocacao) AS horaLocacao, 
       DATE(dataEntrega) AS dataEntrega, 
       TIME(horaEntrega) AS horaEntrega
FROM Locacao;

CREATE VIEW Dim_Cliente AS
SELECT idCliente, nomeCliente, cidadeCliente, estadoCliente, paisCliente
FROM Cliente;

CREATE VIEW Dim_Carro AS
SELECT c1.idCarro, c1.idcombustivel, c1.kmCarro, c1.classiCarro, c1.marcaCarro, c1.modeloCarro, c1.anoCarro, c.tipoCombustivel
FROM Carro c1
JOIN Combustivel c ON c.idcombustivel = c1.idcombustivel;

CREATE VIEW Dim_Vendedor AS
SELECT idVendedor, nomeVendedor, sexoVendedor, estadoVendedor
FROM Vendedor;

SELECT * FROM Dim_Carro dc 
SELECT * FROM Dim_Cliente dc2
SELECT * FROM Dim_Vendedor dv 
SELECT * FROM Fato_Locacao fl 
SELECT * FROM Dim_Data dd
SELECT * FROM Dim_Carro dc;