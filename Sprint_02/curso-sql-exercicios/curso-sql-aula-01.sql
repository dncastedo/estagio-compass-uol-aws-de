-- AULA 01 COMANDOS BÁSICOS

-- **SELECT**

-- (Exemplo 1) Seleção de uma coluna de uma tabela
-- Liste os e-mails dos clientes da tabela sales.customers
select email
from sales.customers

-- (Exemplo 2) Seleção de mais de uma coluna de uma tabela
-- Liste os emails e nomes dos clientes da tabela sales.customers
select email, first_name, last_name
from sales.customers

-- (Exemplo 3) Seleção de todas as colunas de uma tabela
-- Liste todos as informações dos clientes da tabela sales.customers
select *
from sales.customers


-- **DISTINCT**

-- (Exemplo 1) Seleção de uma coluna sem DISTINCT
-- Liste as marcas de carro que constam na tabela products
select brand
from sales.products

-- (Exemplo 2) Seleção de uma coluna com DISTINCT
-- Liste as marcas de carro distintas que constam na tabela products
select distinct brand
from sales.products

-- (Exemplo 3) Seleção de mais de uma coluna com DISTINCT
-- Liste as marcas e anos de modelo distintos que constam na tabela products
select distinct brand, model_year
from sales.products


-- **WHERE**

-- (Exemplo 1) Filtro com condição única
-- Liste os emails dos clientes da nossa base que moram no estado de Santa Catarina
select email, state
from sales.customers
where state='SC'

-- (Exemplo 2) Filtro com mais de uma condição
-- Liste os emails dos clientes da nossa base que moram no estado de Santa Catarina
-- ou Mato Grosso do Sul
select email, state
from sales.customers
where state='SC' or state='MS'

-- (Exemplo 3) Condições com datas
-- Liste os emails dos clientes da nossa base que moram no estado de Santa Catarina 
-- ou Mato Grosso do Sul e que tem mais de 30 anos
select email, state, birth_date
from sales.customers
where (state='SC' or state='MS') and birth_date < '1991-12-28'

select email, state, birth_date
from sales.customers
where (state='SC' or state='MS') and birth_date < '19911228'


-- **ORDER BY**

-- (Exemplo 1) Ordenação de valores numéricos
-- Liste produtos da tabela products na ordem crescente com base no preço
select *
from sales.products
order by price

select *
from sales.products
order by price desc -- Caso queira na ordem decrescente

-- (Exemplo 2) Ordenação de texto
-- Liste os estados distintos da tabela customers na ordem crescente
select distinct state
from sales.customers
order by state


-- **LIMIT**

-- (Exemplo 1) Seleção das N primeiras linhas usando LIMIT
-- Liste as 10 primeiras linhas da tabela funnel
select *
from sales.funnel
limit 10

-- (Exemplo 2) Seleção das N primeiras linhas usando LIMIT e ORDER BY
-- Liste os 10 produtos mais caros da tabela products
select *
from sales.products
order by price desc
limit 10


-- **DESAFIO**

-- (Exercício 1) Selecione os nomes de cidade distintas que existem no estado de
-- Minas Gerais em ordem alfabética (dados da tabela sales.customers)

select distinct city
from sales.customers
where state = 'MG'
order by city

-- (Exercício 2) Selecione o visit_id das 10 compras mais recentes efetuadas
-- (dados da tabela sales.funnel)

select visit_id 
from sales.funnel 
where paid_date is not null
order by paid_date desc
limit 10

-- (Exercício 3) Selecione todos os dados dos 10 clientes com maior score nascidos
-- após 01/01/2000 (dados da tabela sales.customers)

select *
from sales.customers
where birth_date >= '2000-01-01'
order by score desc
limit 10




