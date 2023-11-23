import sys
from pyspark.context import SparkContext
from awsglue.context import GlueContext
from awsglue.transforms import *
from awsglue.utils import getResolvedOptions
from awsglue.job import Job

args = getResolvedOptions(sys.argv, ['JOB_NAME', 'S3_INPUT_PATH', 'S3_TARGET_PATH'])

sc = SparkContext()
glueContext = GlueContext(sc)
spark = glueContext.spark_session
job = Job(glueContext)
job.init(args['JOB_NAME'], args)

source_path = args['S3_INPUT_PATH']
target_path = args['S3_TARGET_PATH']

df = spark.read.option("multiline", "true").json(source_path)

# Lista das colunas a serem excluídas
columns_to_drop = [
    "backdrop_path", "homepage", "id", "original_title", "poster_path", "video",
]

# Excluir as colunas especificadas
df = df.drop(*columns_to_drop)

# Renomear colunas
column_rename_map = {
    "release_date": "data_lancamento_filme",
    "adult": "filme_conteudo_adulto",
    "belongs_to_collection": "pertence_coletanea",
    "budget": "orcamento_filme",
    "genres": "genero_filme",
    "imdb_id": "imdb_id",
    "original_language":"idioma_original_filme",
    "overview": "enredo_filme",
    "popularity": "popularidade_filme",
    "production_companies": "produtora_filme",
    "production_countries": "pais_producao",
    "release_date": "data_lancamento_filme",
    "revenue": "rendimento_filme",
    "runtime": "tempo_execucao_filme",
    "spoken_languages": "idioma_falado_filme",
    "status": "situacao_filme",
    "tagline": "tagline_filme",
    "title": "titulo_filme",
    "vote_average": "media_votos_filme",
    "vote_count": "contagem_votos_filme",
}

for old_col, new_col in column_rename_map.items():
    df = df.withColumnRenamed(old_col, new_col)

df.write.parquet(target_path, mode='overwrite')

job.commit()

