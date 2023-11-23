import sys
from awsglue.transforms import *
from awsglue.utils import getResolvedOptions
from pyspark.context import SparkContext
from awsglue.context import GlueContext
from awsglue.job import Job


# @params: [JOB_NAME]
args = getResolvedOptions(sys.argv, ['JOB_NAME', 'S3_INPUT_PATH', 'S3_TARGET_PATH'])

# Initialize Spark and Glue contexts
sc = SparkContext()
glueContext = GlueContext(sc)
spark = glueContext.spark_session
job = Job(glueContext)
job.init(args['JOB_NAME'], args)

source_file = args['S3_INPUT_PATH']
target_path = args['S3_TARGET_PATH']

# Lê o arquivo CSV com o separador '|'
df = spark.read.option("header", "true").option("delimiter", "|").csv(source_file)

# Aplica o filtro de gênero
filtered_df = df.filter((df['genero'] == 'Horror') | (df['genero'] == 'Mistery'))

# Selecione apenas as colunas que você deseja manter
columns_to_keep = [
    "generoArtista",
    "nomeArtista",
    "notaMedia",
    "personagem",
    "profissao",
    "anoFalecimento",
    "numeroVotos",
    "anoNascimento",
    "id"
]

selected_df = filtered_df.select(*columns_to_keep)

# Renomeie as colunas
renamed_df = selected_df.withColumnRenamed("generoArtista", "genero_artista") \
                       .withColumnRenamed("nomeArtista", "nome_artista") \
                       .withColumnRenamed("notaMedia", "nota_media_filme") \
                       .withColumnRenamed("personagem", "personagem_artista") \
                       .withColumnRenamed("profissao", "profissao_artista") \
                       .withColumnRenamed("anoFalecimento", "ano_falecimento_artista") \
                       .withColumnRenamed("numeroVotos", "numero_votos_filme") \
                       .withColumnRenamed("anoNascimento", "ano_nascimento_artista") \
                       .withColumnRenamed("anoFalecimento", "ano_falecimento_artista") \
                       .withColumnRenamed("id", "id_imdb")

# Escreva o DataFrame resultante no formato Parquet
renamed_df.write.parquet(target_path, mode='overwrite')

job.commit()



