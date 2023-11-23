-- EXERCICIO 01
-- Apresente a query para listar todos os livros publicados após 2014.
-- Ordenar pela coluna cod, em ordem crescente, as linhas.
-- Atenção às colunas esperadas no resultado final: cod, titulo, autor, editora, valor, publicação, edição e idioma.

SELECT *
FROM 
    livro
WHERE 
    publicacao > '2014-12-31'
ORDER BY 
    cod ASC;
   

-- EXERCICIO 02
-- Apresente a query para listar os 10 livros mais caros.
-- Ordenar as linhas pela coluna valor, em ordem decrescente.
-- Atenção às colunas esperadas no resultado final: titulo e valor.

   SELECT 
    titulo, 
    valor
FROM 
    livro
ORDER BY 
    valor DESC
LIMIT 10;


-- EXERCICIO 03
-- Apresente a query para listar as 5 editoras com mais livros na biblioteca.
-- O resultado deve conter apenas as colunas quantidade, nome, estado e cidade.
-- Ordenar as linhas pela coluna que representa a quantidade livros em ordem decrescente.

SELECT 
    COUNT(titulo) AS quantidade, 
    nome, 
    estado, 
    cidade
FROM 
    editora AS e
INNER JOIN 
    livro AS l ON e.codeditora = l.editora
INNER JOIN 
    endereco AS endr ON endr.codendereco = e.endereco 
GROUP BY 
    nome 
ORDER BY 
    quantidade DESC
LIMIT 5;


-- EXERCICIO 04
-- Apresente a query para listar a quantidade de livros publicada por cada autor. 
-- Ordenar as linhas pela coluna nome (autor), em ordem crescente. 
-- Além desta, apresentar as colunas codautor, nascimento e quantidade (total de livros de sua autoria)

SELECT 
    a.nome, 
    a.codautor, 
    a.nascimento, 
    count(l.autor) AS quantidade 
FROM 
    autor AS a
LEFT JOIN 
    livro AS l ON l.autor = a.codautor 
GROUP BY 
    a.nome
ORDER BY 
    a.nome ASC;


-- EXERCICIO 05
-- Apresente a query para listar o nome dos autores que publicaram livros através de editoras NÃO situadas na região sul do Brasil.
-- Ordene o resultado pela coluna nome, em ordem crescente. Não pode haver nomes repetidos em seu retorno.

SELECT 
    DISTINCT a.nome  
FROM 
    autor AS a
INNER JOIN 
    livro  AS l ON l.autor = a.codautor 
INNER JOIN 
    editora AS e ON e.codeditora = l.editora 
INNER JOIN 
    endereco AS e2 ON e.endereco = e2.codendereco 
WHERE 
    e2.estado NOT IN
    (
        'PARANÁ', 
        'RIO GRANDE DO SUL', 
        'SANTA CATARINA'
        )
ORDER BY 
    a.nome ASC;


-- EXERCICIO 06
-- Apresente a query para listar o autor com maior número de livros publicados. O resultado deve conter apenas as colunas codautor, nome, quantidade_publicações

SELECT 
    codautor, 
    nome, 
    COUNT(titulo) AS quantidade_publicacoes 
FROM 
    autor AS a  
INNER JOIN 
    livro AS l ON a.codautor = l.autor 
GROUP BY 
    nome
ORDER BY 
    quantidade_publicacoes DESC
LIMIT 1;


-- EXERCICIO 07
-- Apresente a query para listar o nome dos autores com nenhuma publicação.
-- Apresentá-los em ordem crescente.

SELECT 
    nome
FROM 
    autor AS a
LEFT JOIN 
    livro AS l ON a.codautor  = l.autor 
WHERE 
    l.autor is null
ORDER BY 
    nome ASC;

