-- EXERCICIO 08
-- Apresente a query para listar o código e o nome do vendedor com maior número de vendas (contagem), e que estas vendas estejam com o status concluída. 
-- As colunas presentes no resultado devem ser, portanto, cdvdd e nmvdd.

SELECT 
    vr.cdvdd, 
    vr.nmvdd
FROM 
    tbvendedor AS vr
INNER JOIN 
    tbvendas AS vs ON vr.cdvdd = vs.cdvdd 
WHERE 
    vs.status = 'Concluído'
GROUP BY 
    vr.nmvdd
ORDER BY 
    COUNT(cdven) DESC
LIMIT 1;


-- EXERCICIO 09
-- Apresente a query para listar o código e nome do produto mais vendido entre as datas de 2014-02-03 até 2018-02-02, e que estas vendas estejam com o status concluída. 
-- As colunas presentes no resultado devem ser cdpro e nmpro.

SELECT 
    cdpro, 
    nmpro
FROM 
    tbvendas
WHERE 
    (status = 'Concluído') 
    AND 
    (dtven BETWEEN '2014-02-03 00:00:00' AND '2018-02-02 00:00:00')
GROUP BY 
    nmpro
ORDER BY 
    sum(qtd) DESC
LIMIT 1;


-- EXERCICIO 10
-- A comissão de um vendedor é definida a partir de um percentual sobre o total de vendas (quantidade * valor unitário) por ele realizado. 
-- O percentual de comissão de cada vendedor está armazenado na coluna perccomissao, tabela tbvendedor. 
-- Com base em tais informações, calcule a comissão de todos os vendedores, considerando todas as vendas armazenadas na base de dados com status concluído.
-- As colunas presentes no resultado devem ser vendedor, valor_total_vendas e comissao. O valor de comissão deve ser apresentado em ordem decrescente arredondado na segunda casa decimal.

SELECT 
    nmvdd AS vendedor, 
    ROUND(SUM(vs.qtd * vs.vrunt), 2) AS valor_total_vendas, 
    ROUND(SUM(vs.qtd * vs.vrunt * vr.perccomissao) / 100, 2) as comissao
FROM 
    tbvendedor AS vr
INNER JOIN 
    tbvendas AS vs ON vs.cdvdd = vr.cdvdd
WHERE 
    vs.status = 'Concluído'
GROUP BY 
    vendedor
ORDER BY 
    comissao DESC;


-- EXERCICIO 11
-- Apresente a query para listar o código e nome cliente com maior gasto na loja. 
-- As colunas presentes no resultado devem ser cdcli, nmcli e gasto, esta última representando o somatório das vendas (concluídas) atribuídas ao cliente.

SELECT 
    cdcli, 
    nmcli, 
    sum(qtd*vrunt) AS gasto
FROM 
    tbvendas 
WHERE 
    status = 'Concluído'
GROUP BY 
    cdcli
ORDER BY 
    gasto DESC
LIMIT 1;


-- EXERCICIO 12
-- Apresente a query para listar código, nome e data de nascimento dos dependentes do vendedor com menor valor total bruto em vendas (não sendo zero). 
-- As colunas presentes no resultado devem ser cddep, nmdep, dtnasc e valor_total_vendas.
-- Observação: Apenas vendas com status concluído.

SELECT 
    cddep, 
    nmdep, 
    dtnasc, 
    SUM(vs.qtd*vs.vrunt) AS valor_total_vendas
FROM 
    tbdependente AS tbdep
LEFT JOIN 
    tbvendedor AS vr ON tbdep.cdvdd = vr.cdvdd 
INNER JOIN 
    tbvendas AS vs ON vr.cdvdd = vs.cdvdd
WHERE 
    vs.status = 'Concluído'
GROUP BY 
    cddep
ORDER BY 
    valor_total_vendas ASC 
LIMIT 1;


-- EXERCICIO 13
-- Apresente a query para listar os 10 produtos menos vendidos pelos canais de E-Commerce ou Matriz (Considerar apenas vendas concluídas).  
-- As colunas presentes no resultado devem ser cdpro, nmcanalvendas, nmpro e quantidade_vendas.

SELECT 
    cdpro, 
    nmcanalvendas, 
    nmpro, 
    SUM(qtd) AS quantidade_vendas 
FROM 
  tbvendas 
WHERE 
  status  = 'Concluído' 
GROUP BY 
  cdpro,
  nmcanalvendas,
  nmpro
ORDER BY 
  quantidade_vendas ASC
LIMIT 10;


-- EXERCICIO 14
-- Apresente a query para listar o gasto médio por estado da federação. 
-- As colunas presentes no resultado devem ser estado e gastomedio. 
-- Considere apresentar a coluna gastomedio arredondada na segunda casa decimal e ordenado de forma decrescente.
-- Observação: Apenas vendas com status concluído.

SELECT 
    estado, 
    ROUND(AVG(qtd*vrunt), 2) AS gastomedio
FROM 
    tbvendas 
WHERE 
    status = 	'Concluído'
GROUP BY 
    estado 
ORDER BY 
    gastomedio DESC;


-- EXERCICIO 15
-- Apresente a query para listar os códigos das vendas identificadas como deletadas. 
-- Apresente o resultado em ordem crescente.

SELECT 
    cdven 
FROM 
    tbvendas 
WHERE 
    deletado = '1'
ORDER BY 
    cdven ASC;

   
-- EXERCICIO 16
-- Apresente a query para listar a quantidade média vendida de cada produto agrupado por estado da federação. 
-- As colunas presentes no resultado devem ser estado e nmprod e quantidade_media. 
-- Considere arredondar o valor da coluna quantidade_media na quarta casa decimal. 
-- Ordene os resultados pelo estado (1º) e nome do produto (2º).
-- Obs: Somente vendas concluídas.

SELECT 
    estado, 
    nmpro, 
    ROUND(AVG(qtd), 4) AS quantidade_media
FROM 
    tbvendas
WHERE 
    status = 'Concluído'
GROUP BY 
    estado, 
    nmpro 
ORDER BY 
    estado, 
    nmpro ;

