-- PROCESSO SELETIVO - Grupo de Resposta a Incidentes de Segurança

-- Nome: Fernanda Veiga Gomes da Fonseca
-- TAG - Banco de Dados II - Entrega: 09/03/2020

-- Questão 1 -> RESPOSTA: 50000
SELECT idCompra FROM compra
ORDER BY idCompra DESC;

-- Questão 2 -> RESPOSTA: Ingride
SELECT nome, data_nasc FROM fregueses
WHERE data_nasc > '1990-12-31'
ORDER BY
	data_nasc ASC,
    nome ASC;

-- Questão 3 -> RESPOSTA: Miranda
SELECT nome, data_nasc FROM fregueses
ORDER BY
	data_nasc DESC;

-- Questão 4 -> RESPOSTA: idproduto = 5999, item = CAMISA Glen Arbor 1878
SELECT nota FROM `avaliacao produto`
ORDER BY
	nota DESC;

SELECT t1.idproduto, t1.item, t1.preco, t2.nota
FROM produto AS t1 INNER JOIN `avaliacao produto` AS t2
ON t1.idproduto = t2.produto AND t2.nota = 9
ORDER BY
	t1.preco ASC;

-- Questão 5 -> RESPOSTA: idvendedor = 49, nome = franciely
SELECT t1.vendedor, COUNT(t1.vendedor) AS qt_vendas, AVG(CAST(t2.nota AS UNSIGNED)) AS nt_media
FROM produto AS t1 INNER JOIN `avaliacao vendedor` AS t2
ON t1.vendedor = t2.vendedor
GROUP BY t1.vendedor
ORDER BY
	nt_media DESC,
	qt_vendas DESC;
    
SELECT * FROM vendedor WHERE idvendedor = 49;

-- Questão 5 -> RESPOSTA: idvendedor = 135, nome = amauri
-- Outra interpretação: quantidade de vendas com maior peso.
SELECT t1.vendedor, COUNT(t1.vendedor) AS qt_vendas, AVG(CAST(t2.nota AS UNSIGNED)) AS nt_media
FROM produto AS t1 INNER JOIN `avaliacao vendedor` AS t2
ON t1.vendedor = t2.vendedor
GROUP BY t1.vendedor
ORDER BY
	qt_vendas DESC,
	nt_media DESC;
    
SELECT * FROM vendedor WHERE idvendedor = 135;