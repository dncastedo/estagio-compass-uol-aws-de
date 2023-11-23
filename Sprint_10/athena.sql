CREATE TABLE IF NOT EXISTS tb_generos_filme
WITH (format='PARQUET', external_location='s3://data-lake-diane-nascimento-castedo/Refined/Queries/tb_generos_filme/') AS
SELECT
  "id_genero_filme", "nome_genero_filme"
FROM
  movies;

CREATE TABLE IF NOT EXISTS tb_produtora_filmes
WITH (format='PARQUET', external_location='s3://data-lake-diane-nascimento-castedo/Refined/Queries/tb_produtora_filmes/') AS
SELECT
  "id_produtora_filme", "logo_produtora_filme", "nome_produtora_filme", "pais_origem_produtora"
FROM
  movies;

CREATE TABLE IF NOT EXISTS tb_coletanea_filme
WITH (format='PARQUET', external_location='s3://data-lake-diane-nascimento-castedo/Refined/Queries/tb_coletanea_filme/') AS
SELECT
  "id_coletanea", "nome_coletanea"
FROM
  movies;

CREATE TABLE IF NOT EXISTS tb_idioma_filme
WITH (format='PARQUET', external_location='s3://data-lake-diane-nascimento-castedo/Refined/Queries/tb_idioma_filme/') AS
SELECT
  ROW_NUMBER() OVER () as id_idioma_filme, "idioma_original_filme", "nome_idioma_filme", "sigla_idioma_filme", "nome_ingles_filme"
FROM
  movies;

CREATE TABLE IF NOT EXISTS tb_profissao_artista
WITH (format='PARQUET', external_location='s3://data-lake-diane-nascimento-castedo/Refined/Queries/tb_profissao_artista/') AS
SELECT
  ROW_NUMBER() OVER () as id_profissao, "profissao_artista"
FROM
  movies;

CREATE TABLE IF NOT EXISTS tb_pais_producao
WITH (format='PARQUET', external_location='s3://data-lake-diane-nascimento-castedo/Refined/Queries/tb_pais_producao/') AS
SELECT
  ROW_NUMBER() OVER () as id_pais_producao, "nome_pais_producao", "sigla_pais_producao"
FROM
  movies;


CREATE TABLE IF NOT EXISTS tb_artista
WITH (
  format='PARQUET',
  external_location='s3://data-lake-diane-nascimento-castedo/Refined/Queries/tb_artista/'
) AS
SELECT
  ROW_NUMBER() OVER () as id_artista,
  "nome_artista",
  "genero_artista",
  "ano_nascimento_artista",
  "ano_falecimento_artista"
  --tb_profissao_artista."id_profissao"  -- Coluna referenciada de outra tabela
FROM
  movies;

CREATE TABLE IF NOT EXISTS tb_personagem
WITH (
  format='PARQUET',
  external_location='s3://data-lake-diane-nascimento-castedo/Refined/Queries/tb_personagem/'
) AS
SELECT
  ROW_NUMBER() OVER () as id_personagem,
  "nome_artista",
  "genero_artista",
  "ano_nascimento_artista",
  "ano_falecimento_artista"
  --tb_artista."id_artista"  -- Coluna referenciada de outra tabela
FROM
  movies;

CREATE TABLE IF NOT EXISTS tb_filmes
WITH (format='PARQUET', external_location='s3://data-lake-diane-nascimento-castedo/Refined/Queries/tb_filmes/') AS
SELECT
    "imdb_id", 
    "filme_conteudo_adulto", 
    "enredo_filme", 
    "titulo_filme", 
    "tagline_filme", 
    "tempo_execucao_filme", 
    "situacao_filme", 
    "data_lancamento_filme"
    --tb_produtora_filmes."id_produtora_filme",
    --tb_generos_filme."id_genero_filme",
    --tb_idioma_filme."id_idioma_filme",
    --tb_pais_producao."id_pais_producao",
    --tb_coletanea_filme."id_coletanea",
    --tb_personagem."id_personagem"

FROM
  movies;

CREATE TABLE IF NOT EXISTS tb_metricas_filme
WITH (format='PARQUET', external_location='s3://data-lake-diane-nascimento-castedo/Refined/Queries/tb_metricas/') AS
SELECT
  ROW_NUMBER() OVER () as id_metrica_filme,
  "nota_media_filme", 
  "numero_votos_filme", 
  "orcamento_filme", 
  "popularidade_filme", 
  "rendimento_filme", 
  "media_votos_filme", 
  "contagem_votos_filme"
  --tb_filmes."imdb_id"

FROM
  movies;
